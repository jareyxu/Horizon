"""AI HOT public REST API scraper."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, List

from dateutil.parser import isoparse
import httpx

from .base import BaseScraper
from ..models import AIHotConfig, ContentItem, SourceType


class AIHotScraper(BaseScraper):
    """Fetch curated AI news from AI HOT's key-less public API."""

    def __init__(self, config: AIHotConfig, http_client: httpx.AsyncClient):
        super().__init__(config, http_client)
        self.config = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if since.tzinfo is None:
            since = since.replace(tzinfo=timezone.utc)

        endpoint = f"{self.config.base_url.rstrip('/')}/api/public/items"
        cursor: str | None = None
        items: list[ContentItem] = []
        seen_ids: set[str] = set()

        for _ in range(self.config.max_pages):
            params: dict[str, Any] = {
                "mode": self.config.mode,
                "since": since.astimezone(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "take": self.config.take,
            }
            if cursor:
                params["cursor"] = cursor

            response = await self.client.get(
                endpoint,
                params=params,
                headers={"User-Agent": self.config.user_agent},
            )
            response.raise_for_status()
            payload = response.json()
            raw_items = payload.get("items", [])
            if not isinstance(raw_items, list):
                raise ValueError("AI HOT response field 'items' must be a list")

            for raw in raw_items:
                item = self._to_content_item(raw, since)
                if item and item.id not in seen_ids:
                    seen_ids.add(item.id)
                    items.append(item)

            cursor = payload.get("nextCursor")
            if not payload.get("hasNext") or not cursor:
                break

        return items

    def _to_content_item(
        self,
        raw: dict[str, Any],
        since: datetime,
    ) -> ContentItem | None:
        native_id = str(raw.get("id") or "").strip()
        title = str(raw.get("title") or "").strip()
        original_url = str(raw.get("url") or "").strip()
        if not native_id or not title or not original_url:
            return None

        upstream_score = raw.get("score")
        if (
            isinstance(upstream_score, (int, float))
            and upstream_score < self.config.min_score
        ):
            return None

        upstream_category = str(raw.get("category") or "").strip()
        if self.config.categories and upstream_category not in self.config.categories:
            return None

        published_at = self._parse_datetime(raw.get("publishedAt"))
        if published_at is None or published_at < since:
            return None

        permalink = str(raw.get("permalink") or "").strip() or None
        mapped_category = self.config.category_mapping.get(
            upstream_category,
            upstream_category or "aihot",
        )

        return ContentItem(
            id=self._generate_id("aihot", "item", native_id),
            source_type=SourceType.AIHOT,
            title=title,
            url=original_url,
            content=str(raw.get("summary") or "")
            if self.config.use_remote_summary
            else None,
            author=str(raw.get("source") or "AI HOT"),
            published_at=published_at,
            metadata={
                "category": mapped_category,
                "upstream_category": upstream_category,
                "upstream_source": "AI HOT",
                "upstream_id": native_id,
                "upstream_score": upstream_score,
                "upstream_selected": bool(raw.get("selected", False)),
                "original_url": original_url,
                "reader_url": permalink if self.config.prefer_permalink else None,
                "title_en": raw.get("title_en"),
                "verification_status": "unverified",
            },
        )

    @staticmethod
    def _parse_datetime(value: Any) -> datetime | None:
        if not value:
            return None
        try:
            parsed = isoparse(str(value))
        except (TypeError, ValueError):
            return None
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
