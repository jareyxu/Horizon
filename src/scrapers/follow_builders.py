"""Follow Builders public JSON feed scraper."""

from __future__ import annotations

import asyncio
from datetime import datetime, timedelta, timezone
import hashlib
from typing import Any, List

from dateutil.parser import isoparse
import httpx

from .base import BaseScraper
from ..models import ContentItem, FollowBuildersConfig, SourceType


class FollowBuildersScraper(BaseScraper):
    """Consume the public X, podcast, and blog feeds maintained upstream."""

    def __init__(self, config: FollowBuildersConfig, http_client: httpx.AsyncClient):
        super().__init__(config, http_client)
        self.config = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if since.tzinfo is None:
            since = since.replace(tzinfo=timezone.utc)

        requests = [
            ("x", str(self.config.x_feed)),
            ("podcast", str(self.config.podcast_feed)),
            ("blog", str(self.config.blog_feed)),
        ]
        results = await asyncio.gather(
            *(self._fetch_feed(kind, url, since) for kind, url in requests),
            return_exceptions=True,
        )

        items: list[ContentItem] = []
        for result in results:
            if isinstance(result, list):
                items.extend(result)
        return items

    async def _fetch_feed(
        self,
        kind: str,
        url: str,
        since: datetime,
    ) -> List[ContentItem]:
        response = await self.client.get(
            url,
            headers={"User-Agent": "jareyxu-horizon/0.1 (follow-builders-reader)"},
        )
        response.raise_for_status()
        payload = response.json()
        generated_at = self._parse_datetime(payload.get("generatedAt"))
        if generated_at is None:
            raise ValueError(f"Follow Builders {kind} feed has no valid generatedAt")
        oldest_allowed = datetime.now(timezone.utc) - timedelta(
            hours=self.config.max_feed_age_hours
        )
        if generated_at < oldest_allowed:
            return []

        if kind == "x":
            return self._parse_x(payload, since, generated_at)
        if kind == "podcast":
            return self._parse_podcasts(payload, since, generated_at)
        return self._parse_blogs(payload, since, generated_at)

    def _parse_x(
        self,
        payload: dict[str, Any],
        since: datetime,
        generated_at: datetime,
    ) -> List[ContentItem]:
        items: list[ContentItem] = []
        builders = payload.get("x", [])
        if not isinstance(builders, list):
            raise ValueError("Follow Builders X field must be a list")

        for builder in builders:
            name = str(builder.get("name") or builder.get("handle") or "Unknown")
            handle = str(builder.get("handle") or "")
            tweets = builder.get("tweets", [])
            if not isinstance(tweets, list):
                continue
            for tweet in tweets:
                native_id = str(tweet.get("id") or "").strip()
                text = str(tweet.get("text") or "").strip()
                url = str(tweet.get("url") or "").strip()
                published_at = self._parse_datetime(tweet.get("createdAt"))
                if (
                    not native_id
                    or not text
                    or not url
                    or not published_at
                    or published_at < since
                ):
                    continue
                title_text = " ".join(text.split())
                if len(title_text) > 96:
                    title_text = title_text[:93].rstrip() + "..."
                items.append(
                    ContentItem(
                        id=self._generate_id("follow_builders", "x", native_id),
                        source_type=SourceType.FOLLOW_BUILDERS,
                        title=f"{name}: {title_text}",
                        url=url,
                        content=text,
                        author=name,
                        published_at=published_at,
                        metadata={
                            "category": self.config.category_mapping.get(
                                "x", "builders"
                            ),
                            "source_variant": "x",
                            "handle": handle,
                            "bio": builder.get("bio"),
                            "favorite_count": tweet.get("likes", 0),
                            "retweet_count": tweet.get("retweets", 0),
                            "reply_count": tweet.get("replies", 0),
                            "is_quote": bool(tweet.get("isQuote", False)),
                            "quoted_tweet_id": tweet.get("quotedTweetId"),
                            "feed_generated_at": generated_at.isoformat(),
                            "original_url": url,
                            "verification_status": "original_checked",
                        },
                    )
                )
        return items

    def _parse_podcasts(
        self,
        payload: dict[str, Any],
        since: datetime,
        generated_at: datetime,
    ) -> List[ContentItem]:
        items: list[ContentItem] = []
        episodes = payload.get("podcasts", [])
        if not isinstance(episodes, list):
            raise ValueError("Follow Builders podcasts field must be a list")

        for episode in episodes:
            guid = str(episode.get("guid") or "").strip()
            title = str(episode.get("title") or "").strip()
            url = str(episode.get("url") or "").strip()
            transcript = str(episode.get("transcript") or "").strip()
            published_at = self._parse_datetime(episode.get("publishedAt"))
            if (
                not guid
                or not title
                or not url
                or not published_at
                or published_at < since
            ):
                continue
            compact = self._compact_transcript(
                transcript, self.config.transcript_max_chars
            )
            items.append(
                ContentItem(
                    id=self._generate_id("follow_builders", "podcast", guid),
                    source_type=SourceType.FOLLOW_BUILDERS,
                    title=title,
                    url=url,
                    content=compact,
                    author=str(episode.get("name") or "Follow Builders Podcast"),
                    published_at=published_at,
                    metadata={
                        "category": self.config.category_mapping.get(
                            "podcast", "podcasts"
                        ),
                        "source_variant": "podcast",
                        "guid": guid,
                        "feed_generated_at": generated_at.isoformat(),
                        "transcript_chars": len(transcript),
                        "transcript_compacted": len(compact) < len(transcript),
                        "original_url": url,
                        "verification_status": "original_checked",
                    },
                )
            )
        return items

    def _parse_blogs(
        self,
        payload: dict[str, Any],
        since: datetime,
        generated_at: datetime,
    ) -> List[ContentItem]:
        items: list[ContentItem] = []
        posts = payload.get("blogs", [])
        if not isinstance(posts, list):
            raise ValueError("Follow Builders blogs field must be a list")

        for post in posts:
            title = str(post.get("title") or "").strip()
            url = str(post.get("url") or "").strip()
            published_at = self._parse_datetime(post.get("publishedAt"))
            if not title or not url or not published_at or published_at < since:
                continue
            native_id = hashlib.sha256(url.encode("utf-8")).hexdigest()[:20]
            content = str(post.get("content") or post.get("description") or "").strip()
            items.append(
                ContentItem(
                    id=self._generate_id("follow_builders", "blog", native_id),
                    source_type=SourceType.FOLLOW_BUILDERS,
                    title=title,
                    url=url,
                    content=content,
                    author=str(
                        post.get("author") or post.get("name") or "Follow Builders Blog"
                    ),
                    published_at=published_at,
                    metadata={
                        "category": self.config.category_mapping.get(
                            "blog", "official-blogs"
                        ),
                        "source_variant": "blog",
                        "feed_name": post.get("name"),
                        "feed_generated_at": generated_at.isoformat(),
                        "original_url": url,
                        "verification_status": "original_checked",
                    },
                )
            )
        return items

    @staticmethod
    def _compact_transcript(transcript: str, limit: int) -> str:
        """Keep representative beginning/middle/end excerpts within a hard limit."""
        if len(transcript) <= limit:
            return transcript
        marker = "\n\n[... transcript excerpt omitted ...]\n\n"
        available = max(limit - len(marker) * 2, 3)
        first = available // 3
        middle = available // 3
        last = available - first - middle
        center = len(transcript) // 2
        return (
            transcript[:first]
            + marker
            + transcript[center - middle // 2 : center + (middle - middle // 2)]
            + marker
            + transcript[-last:]
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
