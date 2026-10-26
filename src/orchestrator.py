"""Main orchestrator coordinating the entire workflow."""

import asyncio
import re
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional
from urllib.parse import parse_qsl, urlencode, urlparse
from zoneinfo import ZoneInfo
import httpx
from rich.console import Console

from .models import Config, ContentItem
from .storage.manager import StorageManager
from .services.email import EmailManager
from .services.webhook import WebhookNotifier
from .services.verification import SourceVerifier
from .scrapers.github import GitHubScraper
from .scrapers.hackernews import HackerNewsScraper
from .scrapers.rss import RSSScraper
from .scrapers.web import WebScraper
from .scrapers.reddit import RedditScraper
from .scrapers.telegram import TelegramScraper
from .scrapers.twitter import TwitterScraper
from .scrapers.twitter_playwright import TwitterPlaywrightScraper
from .scrapers.twitter_rapidapi import TwitterRapidAPIScraper
from .scrapers.openbb import OpenBBScraper
from .scrapers.ossinsight import OSSInsightScraper
from .scrapers.gdelt import GDELTScraper
from .scrapers.google_news import GoogleNewsScraper
from .scrapers.aihot import AIHotScraper
from .scrapers.follow_builders import FollowBuildersScraper
from .ai.client import create_ai_client
from .ai.analyzer import ContentAnalyzer
from .ai.summarizer import DailySummarizer
from .ai.enricher import ContentEnricher
from .ai.tokens import get_usage_snapshot, reset_usage, usage_stage
from .ai.longform import LongFormProcessor


@dataclass
class BalancedDigestResult:
    """Items and selection statistics from balanced digest filtering."""

    items: List[ContentItem]
    enabled: bool = False
    group_counts: Dict[str, int] = field(default_factory=dict)
    group_limits: Dict[str, Optional[int]] = field(default_factory=dict)
    duplicate_categories: List[str] = field(default_factory=list)


class HorizonOrchestrator:
    """Orchestrates the complete workflow for content aggregation and analysis."""

    def __init__(
        self,
        config: Config,
        storage: StorageManager,
        *,
        delivery_enabled: bool = True,
    ):
        """Initialize orchestrator.

        Args:
            config: Application configuration
            storage: Storage manager
        """
        self.config = config
        self.report_timezone = ZoneInfo(config.report_timezone)
        self.storage = storage
        self.delivery_enabled = delivery_enabled
        self.console = Console()
        self.source_health = {}
        self._source_health_path = None
        self.email_manager = (
            EmailManager(config.email, console=self.console)
            if delivery_enabled and config.email
            else None
        )
        self.webhook_notifier = (
            WebhookNotifier(config.webhook, console=self.console)
            if delivery_enabled and config.webhook and config.webhook.enabled
            else None
        )

    async def run(self, force_hours: int = None) -> None:
        """Execute the complete workflow.

        Args:
            force_hours: Optional override for time window in hours
        """
        reset_usage()
        self.console.print(
            "[bold cyan]🌅 Horizon - Starting aggregation...[/bold cyan]\n"
        )

        # Check email subscriptions if configured
        if (
            self.email_manager
            and self.config.email
            and self.config.email.enabled
            and self.config.email.imap_enabled
        ):
            self.console.print("📧 Checking for new email subscriptions...")
            self.email_manager.check_subscriptions(self.storage)

        try:
            # 1. Determine time window
            since = self._determine_time_window(force_hours)
            self.console.print(
                f"📅 Fetching content since: {since.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )

            # 2. Fetch content from all sources
            all_items = await self.fetch_all_sources(since)
            raw_items = [item.model_copy(deep=True) for item in all_items]
            if raw_items and hasattr(self.storage, "save_candidate_archive"):
                self.storage.save_candidate_archive(self._report_date(), raw_items)
            self.console.print(f"📥 Fetched {len(all_items)} items from all sources\n")

            tracked_x_items = [
                item
                for item in all_items
                if item.metadata.get("source_variant") == "twitter135_rapidapi"
            ]
            follow_builders_items = [
                item
                for item in all_items
                if item.source_type.value == "follow_builders"
            ]

            if not all_items:
                self._save_source_health("no_content")
                self.console.print("[yellow]No new content found. Exiting.[/yellow]")
                return

            # 3. Merge cross-source duplicates (same URL from different sources)
            merged_items = self.merge_cross_source_duplicates(all_items)
            self._save_source_health("deduplicated", merged=merged_items)
            if len(merged_items) < len(all_items):
                self.console.print(
                    f"🔗 Merged {len(all_items) - len(merged_items)} cross-source duplicates "
                    f"→ {len(merged_items)} unique items\n"
                )

            # 3.5 Condense long podcast transcripts across the whole document.
            with usage_stage("longform_preprocessing"):
                await self._prepare_longform_items(merged_items)

            # 4. Analyze with AI
            with usage_stage("mixed_screening" if self.config.ai.screening_excerpt_sources else "title_scoring" if self.config.ai.analysis_input == "title" else "excerpt_scoring"):
                analyzed_items = await self._analyze_content(merged_items)
            self._apply_source_scoring(analyzed_items)
            self._save_source_health("analyzed", prefiltered=[i for i in analyzed_items if i.metadata.get("prefilter_reason")])
            if hasattr(self.storage, "save_candidate_archive"):
                self.storage.save_candidate_archive(self._report_date(), self.build_candidate_archive(raw_items, analyzed_items))
            self.console.print(f"🤖 Analyzed {len(analyzed_items)} items with AI\n")

            # 5. Filter by score threshold
            threshold = self.config.filtering.ai_score_threshold
            important_items = self.select_important_items(analyzed_items)
            threshold_items = sum(
                1
                for item in important_items
                if item.ai_score is not None and item.ai_score >= threshold
            )
            mandatory_items = sum(bool(item.metadata.get("mandatory_inclusion")) for item in important_items)
            fallback_items = sum(
                not item.metadata.get("mandatory_inclusion")
                and (item.ai_score is None or item.ai_score < threshold)
                for item in important_items
            )

            self.console.print(f"⭐️ {threshold_items} items scored ≥ {threshold}\n")
            if mandatory_items:
                self.console.print(f"📌 {mandatory_items} items included by editorial rules (before deduplication)\n")
            if fallback_items:
                self.console.print(
                    f"🛟 Added {fallback_items} highest-scoring fallback items "
                    f"to reach the minimum digest size\n"
                )

            # 5.5 Semantic deduplication: drop items covering the same topic
            with usage_stage("topic_deduplication"):
                deduped_items = await self.merge_topic_duplicates(important_items)
            if len(deduped_items) < len(important_items):
                self.console.print(
                    f"🧹 Removed {len(important_items) - len(deduped_items)} topic duplicates "
                    f"→ {len(deduped_items)} unique items\n"
                )
            important_items = deduped_items

            # 5.6 Optional second-stage Twitter reply expansion + targeted re-analysis
            with usage_stage("twitter_reply_analysis"):
                await self._expand_twitter_discussion(important_items)

            # 5.7 Apply per-category and global digest limits before enrichment
            balanced_result = self.apply_balanced_digest(important_items)
            important_items = sorted(balanced_result.items, key=lambda item: item.ai_score if item.ai_score is not None else -1, reverse=True)

            # Show per-sub-source selection breakdown
            selected_counts: Dict[str, int] = defaultdict(int)
            for item in important_items:
                key = f"{item.source_type.value}/{self._sub_source_label(item)}"
                selected_counts[key] += 1
            for source_key, count in sorted(selected_counts.items()):
                self.console.print(f"      • {source_key}: {count}")
            self.console.print("")

            # 6. Verify original pages for top/high-risk items.
            await self._verify_important_items(important_items)

            # 7. Search related stories + enrich with background knowledge (2nd AI pass)
            with usage_stage("selected_summary"):
                await self._enrich_important_items(important_items)
            SourceVerifier.finalize_corroboration(important_items)
            self._save_source_health("selected", selected=important_items)

            archive_items = self.build_candidate_archive(raw_items, analyzed_items)
            if hasattr(self.storage, "save_candidate_archive"):
                self.storage.save_candidate_archive(self._report_date(), archive_items)

            # 8. Generate and save daily summaries for each configured language
            today = self._report_date()
            for lang in self.config.ai.languages:
                summarizer = DailySummarizer(editorial_mode=self.config.profile.editorial_mode)
                summary = await summarizer.generate_summary(
                    important_items, today, len(all_items), language=lang
                )
                pages_archive = summarizer.generate_pages_archive_tabs(
                    tracked_x_items,
                    follow_builders_items,
                    {item.id for item in important_items},
                    language=lang,
                    all_items=archive_items,
                )

                # Save to data/summaries/
                summary_path = self.storage.save_daily_summary(
                    today, summary, language=lang
                )
                self.console.print(
                    f"💾 Saved {lang.upper()} summary to: {summary_path}\n"
                )

                # Copy to docs/ for GitHub Pages
                try:
                    from pathlib import Path

                    post_filename = f"{today}-summary-{lang}.md"
                    posts_dir = Path("docs/_posts")
                    posts_dir.mkdir(parents=True, exist_ok=True)

                    dest_path = posts_dir / post_filename

                    # Add Jekyll front matter
                    front_matter = (
                        "---\n"
                        "layout: default\n"
                        f'title: "Horizon Summary: {today} ({lang.upper()})"\n'
                        f"date: {today}\n"
                        f"lang: {lang}\n"
                        "---\n\n"
                    )

                    # Strip leading H1 header to avoid duplication with Jekyll title
                    summary_content = summary
                    first_line = summary_content.strip().split("\n")[0]
                    if first_line.startswith("# "):
                        parts = summary_content.split("\n", 1)
                        if len(parts) > 1:
                            summary_content = parts[1].strip()

                    with open(dest_path, "w", encoding="utf-8") as f:
                        f.write(front_matter + summary_content + pages_archive)

                    self.console.print(
                        f"📄 Copied {lang.upper()} summary to GitHub Pages: {dest_path}\n"
                    )
                except Exception as e:
                    self.console.print(
                        f"[yellow]⚠️  Failed to copy {lang.upper()} summary to docs/: {e}[/yellow]\n"
                    )

                # Send email if configured
                if (
                    self.email_manager
                    and self.config.email
                    and self.config.email.enabled
                ):
                    self.console.print(f"📧 Sending {lang.upper()} email summary...")
                    subscribers = self.storage.load_subscribers()
                    subject = f"Horizon Summary ({lang.upper()}) - {today}"
                    self.email_manager.send_daily_summary(summary, subject, subscribers)

                # Send webhook notification if configured
                if self.webhook_notifier:
                    await self.webhook_notifier.send_daily_summary(
                        summary=summary,
                        important_items=important_items,
                        all_items_count=len(all_items),
                        date=today,
                        lang=lang,
                        summarizer=summarizer,
                    )

            self.console.print(
                "[bold green]✅ Horizon completed successfully![/bold green]"
            )
            self._save_source_health("success")
            usage = get_usage_snapshot()
            if hasattr(self.storage, "save_token_usage"):
                self.storage.save_token_usage(today, {
                    **usage.to_dict(),
                    "run_status": "success",
                    "model": self.config.ai.model,
                    "analysis_input": self.config.ai.analysis_input,
                    "fetched_items": len(all_items),
                    "analyzed_items": len(analyzed_items),
                    "selected_items": len(important_items),
                })
            if usage.total_tokens > 0:
                self.console.print(
                    f"\n🧮 Token usage this run: "
                    f"{usage.total_tokens} tokens "
                    f"(input: {usage.total_input_tokens}, output: {usage.total_output_tokens})"
                )
                for provider, u in sorted(usage.per_provider.items()):
                    if u.total <= 0:
                        continue
                    self.console.print(
                        f"   • {provider}: {u.total} tokens "
                        f"(in: {u.input_tokens}, out: {u.output_tokens})"
                    )
                for stage, u in sorted(usage.per_stage.items()):
                    self.console.print(
                        f"   • stage/{stage}: {u.total} tokens "
                        f"(in: {u.input_tokens}, out: {u.output_tokens}, "
                        f"reported calls: {u.reported_calls}, reported reasoning: {u.reasoning_tokens} "
                        f"in {u.reasoning_reported_calls} calls)"
                    )

        except Exception as e:
            self.console.print(f"[bold red]❌ Error: {e}[/bold red]")
            self._save_source_health("failed")
            if hasattr(self.storage, "save_token_usage"):
                try:
                    self.storage.save_token_usage(self._report_date(), {
                        **get_usage_snapshot().to_dict(), "run_status": "failed",
                        "model": self.config.ai.model,
                        "analysis_input": self.config.ai.analysis_input,
                    })
                except OSError:
                    self.console.print("[yellow]Could not persist partial token usage[/yellow]")

            # Send webhook failure notification if configured
            if self.webhook_notifier:
                await self.webhook_notifier.send_failure(
                    date=self._report_date(),
                    error_message=str(e),
                )

            raise

    def _report_date(self, moment: datetime | None = None) -> str:
        """Return the calendar date used for reports in the configured timezone."""
        current = moment or datetime.now(timezone.utc)
        if current.tzinfo is None:
            current = current.replace(tzinfo=timezone.utc)
        return current.astimezone(self.report_timezone).strftime("%Y-%m-%d")

    def _determine_time_window(self, force_hours: int = None) -> datetime:
        if force_hours:
            since = datetime.now(timezone.utc) - timedelta(hours=force_hours)
        else:
            hours = self.config.filtering.time_window_hours
            since = datetime.now(timezone.utc) - timedelta(hours=hours)
        return since

    async def fetch_all_sources(self, since: datetime) -> List[ContentItem]:
        """Fetch content from all configured sources.

        This is a stable stage entry point for integrations such as MCP.

        Args:
            since: Fetch items published after this time

        Returns:
            List[ContentItem]: All fetched items
        """
        self.source_health = {}
        self._source_health_path = None
        async with httpx.AsyncClient(timeout=30.0) as client:
            tasks = []

            # GitHub sources
            if self.config.sources.github:
                github_scraper = GitHubScraper(self.config.sources.github, client)
                tasks.append(self._fetch_with_progress("GitHub", github_scraper, since))

            # Hacker News
            if self.config.sources.hackernews.enabled:
                hn_scraper = HackerNewsScraper(self.config.sources.hackernews, client)
                tasks.append(
                    self._fetch_with_progress("Hacker News", hn_scraper, since)
                )

            # RSS feeds
            if self.config.sources.rss:
                rss_scraper = RSSScraper(self.config.sources.rss, client)
                tasks.append(self._fetch_with_progress("RSS Feeds", rss_scraper, since))

            # Reddit
            if self.config.sources.web:
                web_scraper = WebScraper(self.config.sources.web, client, self.storage.data_dir / "web-source-state.json")
                tasks.append(self._fetch_with_progress("Public Websites", web_scraper, since))

            # Reddit
            if self.config.sources.reddit.enabled:
                reddit_scraper = RedditScraper(self.config.sources.reddit, client)
                tasks.append(self._fetch_with_progress("Reddit", reddit_scraper, since))

            # Telegram
            if self.config.sources.telegram.enabled:
                telegram_scraper = TelegramScraper(self.config.sources.telegram, client)
                tasks.append(
                    self._fetch_with_progress("Telegram", telegram_scraper, since)
                )

            # Twitter (Apify, Playwright, or Twitter135/RapidAPI mode)
            if self.config.sources.twitter and self.config.sources.twitter.enabled:
                tw_cfg = self.config.sources.twitter
                if tw_cfg.mode == "playwright":
                    twitter_scraper = TwitterPlaywrightScraper(tw_cfg)
                elif tw_cfg.mode == "rapidapi":
                    twitter_scraper = TwitterRapidAPIScraper(tw_cfg, client)
                else:
                    twitter_scraper = TwitterScraper(tw_cfg, client)
                tasks.append(
                    self._fetch_with_progress("Twitter", twitter_scraper, since)
                )

            # OpenBB (financial news / filings via the OpenBB Platform SDK)
            if self.config.sources.openbb and self.config.sources.openbb.enabled:
                openbb_scraper = OpenBBScraper(self.config.sources.openbb, client)
                tasks.append(self._fetch_with_progress("OpenBB", openbb_scraper, since))

            # OSS Insight trending repos
            if (
                self.config.sources.ossinsight
                and self.config.sources.ossinsight.enabled
            ):
                oss_scraper = OSSInsightScraper(self.config.sources.ossinsight, client)
                tasks.append(
                    self._fetch_with_progress("OSS Insight", oss_scraper, since)
                )

            # GDELT 2.0 DOC API (key-less global news)
            if self.config.sources.gdelt and self.config.sources.gdelt.enabled:
                gdelt_scraper = GDELTScraper(self.config.sources.gdelt, client)
                tasks.append(self._fetch_with_progress("GDELT", gdelt_scraper, since))

            # Google News RSS (key-less news search)
            if (
                self.config.sources.google_news
                and self.config.sources.google_news.enabled
            ):
                gn_scraper = GoogleNewsScraper(self.config.sources.google_news, client)
                tasks.append(
                    self._fetch_with_progress("Google News", gn_scraper, since)
                )

            # AI HOT public curated feed
            if self.config.sources.aihot and self.config.sources.aihot.enabled:
                aihot_scraper = AIHotScraper(self.config.sources.aihot, client)
                tasks.append(self._fetch_with_progress("AI HOT", aihot_scraper, since))

            # Follow Builders public JSON feeds
            if (
                self.config.sources.follow_builders
                and self.config.sources.follow_builders.enabled
            ):
                builders_scraper = FollowBuildersScraper(
                    self.config.sources.follow_builders,
                    client,
                )
                tasks.append(
                    self._fetch_with_progress(
                        "Follow Builders", builders_scraper, since
                    )
                )

            # Fetch all concurrently
            results = await asyncio.gather(*tasks, return_exceptions=True)

            # Flatten results
            all_items = []
            for result in results:
                if isinstance(result, Exception):
                    self.console.print(f"[red]Error fetching source: {result}[/red]")
                elif isinstance(result, list):
                    all_items.extend(result)

            self._save_source_health("fetched", fetched=all_items)
            return all_items

    async def _fetch_with_progress(
        self, name: str, scraper, since: datetime
    ) -> List[ContentItem]:
        """Fetch from a scraper with progress indication.

        Args:
            name: Source name for display
            scraper: Scraper instance
            since: Fetch items after this time

        Returns:
            List[ContentItem]: Fetched items
        """
        self.console.print(f"🔍 Fetching from {name}...")
        started = time.monotonic()
        try:
            items = await scraper.fetch(since)
        except Exception as exc:
            self.source_health[name] = {"status": "unavailable", "error": type(exc).__name__, "items": 0, "seconds": round(time.monotonic() - started, 2)}
            raise
        diagnostics = getattr(scraper, "diagnostics", {})
        if not diagnostics:
            diagnostics = {name: {"status": "ok" if items else "no_recent_items", "items": len(items)}}
        for label, diagnostic in diagnostics.items():
            key = name if label == name else f"{name}/{label}"
            self.source_health[key] = {**diagnostic, "seconds": round(time.monotonic() - started, 2)}
            if diagnostic.get("status") in {"restricted", "unavailable", "data_unavailable", "stale_feed", "parse_failed", "no_matching_links", "partial", "invalid"}:
                self.console.print(f"   [yellow]{key}: {diagnostic['status']}[/yellow]")
        for item in items:
            label = item.metadata.get("source_variant") if name == "Follow Builders" else item.metadata.get("primary_language") if name == "OSS Insight" else self._sub_source_label(item)
            key = f"{name}/{label}" if label in diagnostics and label != name else name
            item.metadata["source_health_keys"] = [key]
        self.console.print(f"   Found {len(items)} items from {name}")

        # Show per-sub-source breakdown when there are multiple sub-sources
        sub_counts: Dict[str, int] = defaultdict(int)
        for item in items:
            sub_counts[self._sub_source_label(item)] += 1
        if len(sub_counts) > 1:
            for sub, count in sorted(sub_counts.items()):
                self.console.print(f"      • {sub}: {count}")

        return items

    def _save_source_health(self, status: str, **stages) -> None:
        if not hasattr(self.storage, "save_source_health"):
            return
        for stage, items in stages.items():
            counts = defaultdict(int)
            for item in items:
                for key in set(item.metadata.get("source_health_keys", [])):
                    counts[key] += 1
            for key, diagnostic in self.source_health.items():
                diagnostic[f"{stage}_items"] = counts[key]
        try:
            self._source_health_path = self.storage.save_source_health(
                self._report_date(), {"run_status": status, "sources": self.source_health}, self._source_health_path
            )
        except OSError as exc:
            self.console.print(f"[yellow]Could not persist source health: {type(exc).__name__}[/yellow]")

    @staticmethod
    def _sub_source_label(item: ContentItem) -> str:
        """Return a human-readable sub-source label for an item."""
        meta = item.metadata
        if meta.get("subreddit"):
            return f"r/{meta['subreddit']}"
        if meta.get("feed_name"):
            return meta["feed_name"]
        if meta.get("channel"):
            return f"@{meta['channel']}"
        if meta.get("period") and meta.get("repo"):
            return f"ossinsight:{meta.get('primary_language', 'all')}"
        if meta.get("repo"):
            return meta["repo"]
        if meta.get("watchlist"):
            return meta["watchlist"]
        if meta.get("source_name"):
            return meta["source_name"]
        if meta.get("gn_query"):
            return f"google_news:{meta['gn_query']}"
        if meta.get("domain"):
            return meta["domain"]
        if meta.get("source_variant"):
            return f"follow_builders:{meta['source_variant']}"
        if meta.get("upstream_source"):
            return str(meta["upstream_source"])
        return item.author or "unknown"

    def merge_cross_source_duplicates(
        self, items: List[ContentItem]
    ) -> List[ContentItem]:
        """Merge items that point to the same URL from different sources.

        This is a stable stage helper for integrations such as MCP.

        Keeps the item with the richest content and combines metadata.

        Args:
            items: Items to deduplicate

        Returns:
            List[ContentItem]: Deduplicated items
        """

        def normalize_url(url: str) -> str:
            parsed = urlparse(str(url))
            # Strip www prefix, fragments, and common tracking parameters while
            # preserving meaningful query parameters.
            host = parsed.hostname or ""
            if host.startswith("www."):
                host = host[4:]
            path = parsed.path.rstrip("/")
            tracking = {"ref", "source", "fbclid", "gclid"}
            query = urlencode(
                sorted(
                    (key, value)
                    for key, value in parse_qsl(parsed.query, keep_blank_values=True)
                    if not key.lower().startswith("utm_")
                    and key.lower() not in tracking
                )
            )
            return f"{host}{path}" + (f"?{query}" if query else "")

        # Group by normalized URL
        url_groups: Dict[str, List[ContentItem]] = {}
        for item in items:
            key = normalize_url(str(item.url))
            url_groups.setdefault(key, []).append(item)

        merged = []
        for key, group in url_groups.items():
            if len(group) == 1:
                merged.append(group[0])
                continue

            # Pick the item with the richest content as primary
            primary = max(group, key=lambda x: len(x.content or ""))
            health_keys = {key for item in group for key in item.metadata.get("source_health_keys", [])}

            # Merge metadata and source info from other items
            all_sources = set()
            for item in group:
                all_sources.add(item.source_type.value)
                # Merge metadata (engagement, discussion, etc.)
                for mk, mv in item.metadata.items():
                    if mk not in primary.metadata or not primary.metadata[mk]:
                        primary.metadata[mk] = mv

                # Append content (e.g., comments from another source)
                if item is not primary and item.content:
                    if primary.content and item.content not in primary.content:
                        primary.content = (
                            (primary.content or "")
                            + f"\n\n--- From {item.source_type.value} ---\n"
                            + item.content
                        )

            source_details = []
            original_urls = []
            for item in group:
                item_url = str(item.url)
                original_urls.append(item_url)
                source_details.append(
                    {
                        "title": item.title,
                        "url": item_url,
                        "source": item.source_type.value,
                    }
                )
            primary.metadata["merged_sources"] = sorted(all_sources)
            primary.metadata["source_count"] = len(source_details)
            primary.metadata["original_urls"] = list(dict.fromkeys(original_urls))
            primary.metadata["sources"] = source_details
            primary.metadata["source_health_keys"] = sorted(health_keys)
            merged.append(primary)

        return merged

    @staticmethod
    def build_candidate_archive(raw_items, analyzed_items):
        """Retain every fetched row and its original text, including merged rows."""
        by_id = {item.id: item for item in analyzed_items}
        by_url = {}
        for item in analyzed_items:
            for url in [str(item.url), *item.metadata.get("original_urls", [])]:
                by_url[str(url)] = item
        result = []
        for raw in raw_items:
            item = raw.model_copy(deep=True)
            analyzed = by_id.get(raw.id) or by_url.get(str(raw.url))
            if analyzed:
                item.ai_score = analyzed.ai_score
                item.ai_reason = analyzed.ai_reason
                item.ai_summary = analyzed.ai_summary
                item.ai_tags = list(analyzed.ai_tags)
                if analyzed.id == raw.id:
                    for key in ("title_zh", "summary_zh", "creator", "creator_eligible", "analysis_input", "is_model_release", "model_release_name", "mandatory_inclusion", "prefilter_reason", "verification_status", "coverage_status"):
                        if key in analyzed.metadata:
                            item.metadata[key] = analyzed.metadata[key]
                else:
                    item.metadata["archive_analysis_inherited"] = True
            result.append(item)
        return result

    def _apply_source_scoring(self, items: List[ContentItem]) -> None:
        """Blend personal, upstream, and corroboration signals into final scores."""
        filtering = self.config.filtering
        for item in items:
            personal = float(
                item.metadata.get("personal_ai_score") or item.ai_score or 0
            )
            score = personal
            if self.config.profile.editorial_mode == "creator":
                eligible = item.metadata.get("creator_eligible", False)
                item.ai_score = round(min(10 if eligible else 5.5, max(0, score)), 2)
                continue
            upstream = item.metadata.get("upstream_score")
            if item.source_type.value == "aihot" and isinstance(upstream, (int, float)):
                weight = filtering.aihot_score_weight
                score = personal * (1 - weight) + (float(upstream) / 10.0) * weight

            source_count = int(item.metadata.get("source_count") or 1)
            if source_count >= 4:
                score += filtering.multi_source_bonus_4_plus
            elif source_count >= 2:
                score += filtering.multi_source_bonus_2_3

            item.ai_score = round(min(max(score, 0.0), 10.0), 2)

    def select_important_items(self, items: List[ContentItem]) -> List[ContentItem]:
        """Select threshold-qualified items and backfill a useful minimum digest."""
        filtering = self.config.filtering
        mandatory = []
        for item in items:
            reason = self._mandatory_inclusion(item)
            if reason:
                item.metadata["mandatory_inclusion"] = reason
                mandatory.append(item)
        ranked = sorted(items, key=lambda item: item.ai_score or 0, reverse=True)
        if self.config.profile.editorial_mode == "creator":
            ranked = [item for item in ranked if item.metadata.get("creator_eligible")]
        selected = [
            item
            for item in ranked
            if item.ai_score is not None
            and item.ai_score >= filtering.ai_score_threshold
        ]

        missing = max(filtering.minimum_items - len(selected), 0)
        if missing:
            selected_ids = {item.id for item in selected}
            fallback = [
                item
                for item in ranked
                if item.id not in selected_ids
                and item.ai_score is not None
                and item.ai_score > 0
            ]
            selected.extend(fallback[:missing])

        return mandatory + [item for item in selected if item not in mandatory]

    def _mandatory_inclusion(self, item: ContentItem) -> Optional[str]:
        """Editorial overrides do not inflate or replace the model's score."""
        filtering = self.config.filtering
        host = (urlparse(str(item.url)).hostname or "").lower()
        if (
            filtering.always_include_aibase_daily
            and host in {"news.aibase.cn", "www.aibase.cn", "www.aibase.com", "news.aibase.com"}
            and re.match(r"^AI\s*日报\s*[:：]", item.title, re.I)
        ):
            return "AIbase AI 日报固定入选"
        if filtering.always_include_model_releases and item.metadata.get("is_model_release") is True:
            return "新模型发布固定入选（去重后）"
        return None

    async def merge_topic_duplicates(
        self, items: List[ContentItem]
    ) -> List[ContentItem]:
        """Merge items covering the same topic using AI semantic deduplication.

        This is a stable stage helper for integrations such as MCP.

        Sends all item titles, tags, and summaries to AI in a single call.
        Items must already be sorted by ai_score descending so that the first
        item in each duplicate group is always the highest-scored one.
        Content (comments) from duplicate items is merged into the primary.

        Falls back to returning items unchanged if the AI call fails.
        """
        if len(items) <= 1:
            return items

        # A roundup is a standalone reading resource, not a duplicate of any
        # individual headline it happens to mention.
        roundups = [item for item in items if self._mandatory_inclusion(item) == "AIbase AI 日报固定入选"]
        if roundups:
            others = [item for item in items if item not in roundups]
            return roundups + await self.merge_topic_duplicates(others)

        from .ai.prompts import TOPIC_DEDUP_SYSTEM, TOPIC_DEDUP_USER
        from .ai.utils import parse_json_response

        # Build the item list for the prompt
        lines = []
        for i, item in enumerate(items):
            tags = ", ".join(item.ai_tags) if item.ai_tags else "—"
            summary = item.ai_summary or "—"
            lines.append(
                f"[{i}] {item.title}\n    Tags: {tags}\n    Summary: {summary}"
            )
        items_text = "\n\n".join(lines)

        try:
            ai_client = create_ai_client(self.config.ai)
            response = await ai_client.complete(
                system=TOPIC_DEDUP_SYSTEM,
                user=TOPIC_DEDUP_USER.format(items=items_text),
            )
            result = parse_json_response(response)
            if result is None:
                self.console.print(
                    "[yellow]  dedup: could not parse AI response, skipping[/yellow]"
                )
                return items

            duplicate_groups = result.get("duplicates", [])
        except Exception as e:
            self.console.print(
                f"[yellow]  dedup: AI call failed ({e}), skipping[/yellow]"
            )
            return items

        if not duplicate_groups:
            return items

        # Build a set of indices to drop (all non-primary duplicates)
        drop_indices: set[int] = set()
        for group in duplicate_groups:
            if not isinstance(group, list) or len(group) < 2:
                continue
            primary_idx = group[0]
            if primary_idx < 0 or primary_idx >= len(items):
                continue
            primary = items[primary_idx]
            for dup_idx in group[1:]:
                if not isinstance(dup_idx, int) or dup_idx < 0 or dup_idx >= len(items):
                    continue
                if dup_idx == primary_idx:
                    continue
                dup = items[dup_idx]
                if dup.metadata.get("mandatory_inclusion"):
                    primary.metadata["mandatory_inclusion"] = dup.metadata["mandatory_inclusion"]
                if dup.metadata.get("is_model_release") is True:
                    primary.metadata["is_model_release"] = True
                    primary.metadata["model_release_name"] = dup.metadata.get("model_release_name", "")
                # Merge comments/content from the duplicate into the primary
                if dup.content:
                    if not primary.content or dup.content not in primary.content:
                        label = dup.source_type.value
                        primary.content = (
                            primary.content or ""
                        ) + f"\n\n--- From {label} ---\n{dup.content}"
                merged_sources = set(primary.metadata.get("merged_sources") or [])
                merged_sources.add(primary.source_type.value)
                merged_sources.add(dup.source_type.value)
                original_urls = list(
                    primary.metadata.get("original_urls") or [str(primary.url)]
                )
                if str(dup.url) not in original_urls:
                    original_urls.append(str(dup.url))
                source_details = list(primary.metadata.get("sources") or [])
                if not any(
                    source.get("url") == str(dup.url) for source in source_details
                ):
                    source_details.append(
                        {
                            "title": dup.title,
                            "url": str(dup.url),
                            "source": dup.source_type.value,
                        }
                    )
                primary.metadata["merged_sources"] = sorted(merged_sources)
                primary.metadata["source_health_keys"] = sorted(set(primary.metadata.get("source_health_keys", [])) | set(dup.metadata.get("source_health_keys", [])))
                primary.metadata["original_urls"] = original_urls
                primary.metadata["sources"] = source_details
                primary.metadata["source_count"] = max(
                    int(primary.metadata.get("source_count") or 1) + 1,
                    len(source_details),
                )
                self.console.print(
                    f"   [dim]dedup: keep [{primary_idx}] {primary.title}[/dim]\n"
                    f"   [dim]       drop [{dup_idx}] {dup.title}[/dim]"
                )
                drop_indices.add(dup_idx)

        result_items = [item for i, item in enumerate(items) if i not in drop_indices]
        self._apply_source_scoring(result_items)
        return result_items

    def apply_balanced_digest(
        self,
        items: List[ContentItem],
        *,
        log: bool = True,
    ) -> BalancedDigestResult:
        """Apply configured category quotas and the final item cap.

        Categories are read from ``item.metadata["category"]``. If a category
        appears in more than one configured group, the first group in config
        order wins.
        """
        filtering = self.config.filtering
        groups = filtering.category_groups
        max_items = filtering.max_items

        if not groups and max_items is None:
            return BalancedDigestResult(items=items)

        sorted_items = sorted(
            items,
            key=lambda item: item.ai_score or 0,
            reverse=True,
        )

        category_to_group: Dict[str, str] = {}
        duplicate_categories: List[str] = []
        for group_key, group in groups.items():
            for category in group.categories:
                if category in category_to_group:
                    if category_to_group[category] != group_key:
                        duplicate_categories.append(category)
                    continue
                category_to_group[category] = group_key

        if log:
            for category in sorted(set(duplicate_categories)):
                first_group = category_to_group[category]
                self.console.print(
                    f"[yellow]Warning: category '{category}' is configured in multiple "
                    f"groups; using '{first_group}'.[/yellow]"
                )

        selected: List[tuple[ContentItem, str]] = []
        group_counts: Dict[str, int] = defaultdict(int)
        default_group = filtering.default_group

        for item in sorted_items:
            if item.metadata.get("mandatory_inclusion") or self._mandatory_inclusion(item):
                selected.append((item, "mandatory"))
                continue
            category = item.metadata.get("category")
            group_key = (
                category_to_group.get(category, default_group)
                if isinstance(category, str)
                else default_group
            )

            if group_key in groups:
                limit = groups[group_key].limit
            else:
                limit = filtering.default_group_limit

            if limit is not None and group_counts[group_key] >= limit:
                continue

            selected.append((item, group_key))
            group_counts[group_key] += 1

        if max_items is not None:
            mandatory = [entry for entry in selected if entry[1] == "mandatory"]
            ordinary = [entry for entry in selected if entry[1] != "mandatory"]
            selected = mandatory + ordinary[:max(0, max_items - len(mandatory))]

        final_counts: Dict[str, int] = defaultdict(int)
        for _, group_key in selected:
            final_counts[group_key] += 1

        group_limits: Dict[str, Optional[int]] = {
            group_key: group.limit for group_key, group in groups.items()
        }
        group_limits.setdefault(default_group, filtering.default_group_limit)

        if log:
            self.console.print(
                f"⚖️ Balanced digest selected {len(selected)}/{len(items)} items"
            )
            for group_key, group in groups.items():
                label = group.name or group_key
                self.console.print(
                    f"      • {label}: {final_counts.get(group_key, 0)}/{group.limit}"
                )
            if (
                final_counts.get(default_group, 0)
                or filtering.default_group_limit is not None
            ):
                limit_label = (
                    str(filtering.default_group_limit)
                    if filtering.default_group_limit is not None
                    else "unlimited"
                )
                self.console.print(
                    f"      • {default_group}: "
                    f"{final_counts.get(default_group, 0)}/{limit_label}"
                )
            self.console.print("")

        return BalancedDigestResult(
            items=[item for item, _ in selected],
            enabled=True,
            group_counts=dict(final_counts),
            group_limits=group_limits,
            duplicate_categories=sorted(set(duplicate_categories)),
        )

    async def _expand_twitter_discussion(self, items: List[ContentItem]) -> None:
        """Second-stage: fetch reply text for important Twitter items and re-analyze.

        Only runs when sources.twitter.fetch_reply_text is True.
        Bounded by max_tweets_to_expand to control cost.
        """
        tw_cfg = self.config.sources.twitter
        if not tw_cfg or not tw_cfg.enabled or not tw_cfg.fetch_reply_text:
            return

        from .models import SourceType

        twitter_items = [
            item for item in items if item.source_type == SourceType.TWITTER
        ][: tw_cfg.max_tweets_to_expand]

        if not twitter_items:
            return

        self.console.print(
            f"💬 Fetching reply text for {len(twitter_items)} Twitter items..."
        )

        async with httpx.AsyncClient(timeout=30.0) as client:
            if tw_cfg.mode in {"playwright", "rapidapi"}:
                self.console.print(
                    f"   [yellow]Reply expansion not supported in {tw_cfg.mode} mode.[/yellow]"
                )
                return
            scraper = TwitterScraper(tw_cfg, client)
            expanded = []
            for item in twitter_items:
                try:
                    reply_lines = await scraper.fetch_replies_for_item(item)
                    if TwitterScraper.append_discussion_content(item, reply_lines):
                        expanded.append(item)
                        self.console.print(
                            f"   💬 {len(reply_lines)} replies added to: {item.title[:60]}"
                        )
                except Exception as exc:
                    self.console.print(
                        f"   [yellow]⚠️  Reply fetch failed for {item.id}: {exc}[/yellow]"
                    )

        if not expanded:
            return

        self.console.print(
            f"   Re-analyzing {len(expanded)} Twitter items with reply context...\n"
        )
        ai_client = create_ai_client(self.config.ai)
        analyzer = ContentAnalyzer(ai_client, self.config.profile)
        await analyzer.analyze_batch(expanded)

    async def _enrich_important_items(self, items: List[ContentItem]) -> None:
        """Enrich items with background knowledge (2nd AI pass).

        For each item that passed the score threshold, call AI to generate
        background knowledge based on the item's actual content.

        Args:
            items: Important items to enrich (modified in-place)
        """
        if not items:
            return

        self.console.print("📚 Enriching with background knowledge...")
        ai_client = create_ai_client(self.config.ai)
        enricher = ContentEnricher(ai_client, self.config.profile)
        await enricher.enrich_batch(items)
        self.console.print(f"   Enriched {len(items)} items\n")

    async def _verify_important_items(self, items: List[ContentItem]) -> None:
        """Verify original pages according to the configured tiered policy."""
        if not self.config.verification.enabled or not items:
            return
        self.console.print("🔎 Verifying original sources...")
        verifier = SourceVerifier(self.config.verification)
        await verifier.verify_batch(items)
        verified = sum(
            item.metadata.get("verification_status") in {"original_read", "original_reachable"} for item in items
        )
        self.console.print(
            f"   Verified or reached {verified}/{len(items)} shortlisted items\n"
        )

    async def _analyze_content(self, items: List[ContentItem]) -> List[ContentItem]:
        """Analyze content items with AI.

        Args:
            items: Items to analyze

        Returns:
            List[ContentItem]: Analyzed items
        """
        self.console.print("🤖 Analyzing content with AI...")

        candidates = []
        for item in items:
            reason = self._creator_prefilter_reason(item)
            if reason:
                item.ai_score = 0
                item.ai_reason = f"前置规则过滤：{reason}"
                item.ai_summary = item.title
                item.metadata.update({"prefilter_reason": reason, "creator_eligible": False})
            else:
                candidates.append(item)
        if not candidates:
            return items
        ai_client = create_ai_client(self.config.ai)
        analyzer = ContentAnalyzer(ai_client, self.config.profile)

        await analyzer.analyze_batch(candidates)
        return items

    def _creator_prefilter_reason(self, item: ContentItem) -> str | None:
        if not self.config.filtering.creator_prefilter or self.config.profile.editorial_mode != "creator":
            return None
        # A second collector's report may add relevant context; let AI assess it.
        if len(item.metadata.get("merged_sources", [])) > 1:
            return None
        from bs4 import BeautifulSoup
        text = BeautifulSoup(item.content or "", "html.parser").get_text(" ", strip=True)
        if item.source_type.value == "github" and item.metadata.get("tag"):
            if item.metadata.get("prerelease"):
                return "GitHub 预发布版本"
            feature = re.search(r"\b(new|add(?:ed|s)?|introduc\w*|support\w*|feature\w*|launch\w*|model)\b|新增|支持|新功能", text, re.I)
            if text and not feature and re.search(r"\b(fix(?:ed|es)?|bug|maintenance|chore)\b|修复|维护", text, re.I):
                return "GitHub 常规修复与维护"
        if item.source_type.value == "hackernews" and not re.search(
            r"\b(ai|llms?|gpt\w*|agents?|models?|neural|robot\w*|prompt\w*|diffusion|transformer\w*|intelligence|machine learning|deep learning|chatgpt|claude|gemini|openai|anthropic|deepseek|codex|copilot|sora|midjourney)\b|人工智能|大模型|生图|智能体", f"{item.title} {text}", re.I
        ):
            return "HN 标题及已抓取内容未命中 AI 主题"
        return None

    async def _prepare_longform_items(self, items: List[ContentItem]) -> None:
        """Summarize long podcast transcripts before relevance scoring."""
        if self.config.ai.analysis_input == "title":
            return
        if not any(
            item.metadata.get("source_variant") == "podcast"
            and len(item.content or "") > 6000
            for item in items
        ):
            return
        self.console.print("🎧 Condensing long podcast transcripts...")
        ai_client = create_ai_client(self.config.ai)
        processor = LongFormProcessor(ai_client)
        await processor.process_batch(items)

    async def _generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary.

        Args:
            items: Important items to include (already enriched with background/related)
            date: Date string
            total_fetched: Total items fetched
            language: Output language ("en" or "zh")

        Returns:
            str: Markdown summary
        """
        self.console.print("📝 Generating daily summary...")

        summarizer = DailySummarizer()

        return await summarizer.generate_summary(
            items, date, total_fetched, language=language
        )
