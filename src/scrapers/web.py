"""Small, bounded collectors for public news pages and product changelogs."""

from __future__ import annotations

import hashlib
import json
import logging
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup
from dateutil.parser import parse
import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, WebSourceConfig

logger = logging.getLogger(__name__)


class WebScraper(BaseScraper):
    def __init__(self, sources, http_client, state_path="data/web-source-state.json"):
        super().__init__({}, http_client)
        self.sources = sources
        self.state_path = Path(state_path)
        self.diagnostics = {}

    async def fetch(self, since):
        items = []
        for source in self.sources:
            if not source.enabled:
                continue
            try:
                self._article_failures = 0
                soup = await self._page(str(source.url))
                if source.mode == "snapshot":
                    found = self._snapshot(source, soup)
                elif source.mode == "changelog":
                    found = self._changelog(source, soup)
                else:
                    found = await self._articles(source, soup)
                recent = [i for i in found if since <= i.published_at <= datetime.now(timezone.utc)]
                items.extend(sorted(recent, key=lambda i: i.published_at, reverse=True)[:source.max_items])
                logger.info("Web %s: %d recent items", source.name, len(recent))
                self.diagnostics[source.name] = {"status": "partial" if self._article_failures else "ok", "items": len(recent), "skipped_articles": self._article_failures}
            except (httpx.HTTPError, ValueError) as exc:
                self.diagnostics[source.name] = {"status": "unavailable", "error": str(exc)}
                logger.warning("Web %s unavailable: %s", source.name, exc)
            except Exception:
                self.diagnostics[source.name] = {"status": "error"}
                logger.exception("Web %s collection failed", source.name)
        return items

    async def _page(self, url):
        response = await self.client.get(url, follow_redirects=True, headers={
            "User-Agent": "Horizon/0.1 (+https://github.com/jareyxu/Horizon)"
        })
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.select_one("#challenge-running, #challenge-form") or "Enable JavaScript and cookies to continue" in soup.get_text(" ", strip=True):
            raise ValueError("Challenge page returned instead of public content")
        return soup

    @staticmethod
    def _date(value):
        if not value:
            return None
        try:
            date = parse(str(value))
            return date.replace(tzinfo=timezone.utc) if date.tzinfo is None else date.astimezone(timezone.utc)
        except (ValueError, TypeError, OverflowError):
            return None

    @classmethod
    def _published(cls, soup):
        # Publication only: a site's modification time is not a new story date.
        meta = soup.select_one('meta[property="article:published_time"], meta[name="datePublished"]')
        if meta and (date := cls._date(meta.get("content"))):
            return date
        for script in soup.select('script[type="application/ld+json"]'):
            try:
                nodes = json.loads(script.get_text())
                stack = nodes if isinstance(nodes, list) else [nodes]
                while stack:
                    node = stack.pop()
                    if not isinstance(node, dict):
                        continue
                    if date := cls._date(node.get("datePublished")):
                        return date
                    stack.extend(node.get("@graph", []))
            except (ValueError, TypeError):
                continue
        time = soup.select_one("time")
        if time and (date := cls._date(time.get("datetime") or time.get_text(strip=True))):
            return date
        # AIBase publishes a Chinese local timestamp in its article body.
        match = re.search(r"发布时间\s*[:：]?\s*(\d{4})年(\d{1,2})月(\d{1,2})[号日]\s*(\d{1,2}):(\d{2})", soup.get_text(" ", strip=True))
        if match:
            return datetime(*map(int, match.groups()), tzinfo=ZoneInfo("Asia/Shanghai")).astimezone(timezone.utc)
        return None

    @staticmethod
    def _text(soup, selector):
        root = soup.select_one(selector)
        if root is None:
            return ""
        root = BeautifulSoup(str(root), "html.parser")
        for element in root.select("script, style, nav, footer, header, form"):
            element.decompose()
        return root.get_text(" ", strip=True)[:12000]

    @staticmethod
    def _item(source, title, url, content, date, **metadata):
        digest = hashlib.sha256(url.encode()).hexdigest()[:20]
        return ContentItem(id=f"web:{digest}", source_type=SourceType.WEB,
            title=title, url=url, content=content, author=source.name, published_at=date,
            metadata={"feed_name": source.name, "category": source.category, **metadata})

    async def _articles(self, source, soup):
        items, seen = [], set()
        for link in soup.select(source.link_selector):
            if source.title_include_keywords and not any(
                keyword.casefold() in link.get_text(" ", strip=True).casefold()
                for keyword in source.title_include_keywords
            ):
                continue
            target = urljoin(str(source.url), link.get("href", ""))
            parts = urlsplit(target)
            if parts.scheme not in {"http", "https"}:
                continue
            target = urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))
            if target in seen:
                continue
            seen.add(target)
            if len(seen) > source.max_items:
                break
            if source.mode == "cards":
                date_node = link.select_one(source.date_selector or "time")
                raw = (date_node.get("datetime") or date_node.get_text(strip=True)) if date_node else ""
                date = self._date(raw)
                precision = "publication"
                # Relative times are explicitly identified, never called exact publication times.
                if date is None and (m := re.fullmatch(r"(\d+)([hm]) ago", raw)):
                    count = int(m[1])
                    date = datetime.now(timezone.utc) - timedelta(minutes=count if m[2] == "m" else count * 60)
                    precision = "relative"
                if date is None:
                    continue
                title = link.select_one("h2, h3")
                items.append(self._item(source, title.get_text(" ", strip=True) if title else link.get_text(" ", strip=True)[:200], target, link.get_text(" ", strip=True), date, date_precision=precision))
                continue
            try:
                article = await self._page(target)
                date = self._published(article)
                title = article.select_one("h1")
                content = self._text(article, source.content_selector)
                if date and title and content:
                    items.append(self._item(source, title.get_text(" ", strip=True), target, content, date))
                else:
                    self._article_failures += 1
                    logger.info("Web %s skipped undated/empty article: %s", source.name, target)
            except httpx.HTTPError as exc:
                self._article_failures += 1
                logger.warning("Web %s article unavailable: %s", source.name, exc)
            except ValueError as exc:
                self._article_failures += 1
                logger.warning("Web %s article unusable: %s", source.name, exc)
        return items

    def _changelog(self, source, soup):
        root = soup.select_one(source.content_selector)
        if root is None:
            return []
        items = []
        for heading in root.select("h1, h2"):
            label = heading.get_text(" ", strip=True)
            # Only explicit full-date headings, never product versions or generic headings.
            if not re.fullmatch(r"[A-Za-z]+ \d{1,2}, \d{4}", label):
                continue
            date = self._date(label)
            if date is None:
                continue
            body = []
            for sibling in heading.next_siblings:
                if getattr(sibling, "name", None) in {"h1", "h2"} and re.fullmatch(r"[A-Za-z]+ \d{1,2}, \d{4}", sibling.get_text(" ", strip=True)):
                    break
                if hasattr(sibling, "get_text"):
                    body.append(sibling.get_text(" ", strip=True))
            if body:
                url = f"{source.url}#horizon-{date.date().isoformat()}"
                item = self._item(source, f"{source.name} · {label}", str(source.url), " ".join(body)[:12000], date)
                item.id = "web:changelog:" + hashlib.sha256(url.encode()).hexdigest()[:20]
                items.append(item)
        return items

    def _snapshot(self, source, soup):
        content = self._text(soup, source.content_selector)
        if len(content) < 100:
            raise ValueError("No usable product content; baseline not updated")
        digest = hashlib.sha256(content.encode()).hexdigest()
        state = json.loads(self.state_path.read_text()) if self.state_path.exists() else {}
        previous = state.get(str(source.url))
        if previous == digest:
            return []
        state[str(source.url)] = digest
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.state_path.with_suffix(".tmp")
        temporary.write_text(json.dumps(state))
        temporary.replace(self.state_path)
        if previous is None:
            logger.info("Web %s: first baseline stored; no launch date inferred", source.name)
            return []
        content = "这是官网内容变化线索，观察时间不是产品发布日期；尚未核实是否为新功能，不应直接称为今日发布。\n" + content
        item = self._item(source, f"{source.name}：页面内容变化（待核实）", str(source.url), content, datetime.now(timezone.utc), observed_change=True, requires_verification=True)
        item.id += ":" + digest[:12]
        return [item]
