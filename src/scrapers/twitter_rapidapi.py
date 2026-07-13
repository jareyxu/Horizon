"""Read-only X account tracking through Twitter135 on RapidAPI."""

from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
import logging
import os
from typing import Any, Iterator, List, Optional

import httpx

from .base import BaseScraper
from ..models import ContentItem, RapidAPIXUserConfig, SourceType, TwitterConfig

logger = logging.getLogger(__name__)


class TwitterRapidAPIScraper(BaseScraper):
    """Fetch one page of recent posts per configured account.

    Twitter135's BASIC plan counts every endpoint call as one request. This
    scraper therefore requires public X ``rest_id`` values in configuration,
    avoids the extra username lookup call, never paginates, and never retries.
    """

    def __init__(self, config: TwitterConfig, http_client: httpx.AsyncClient):
        super().__init__(config, http_client)
        self.config = config
        self.requests_used = 0

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.config.enabled:
            return []

        accounts = [
            account for account in self.config.rapidapi_users if account.enabled
        ]
        if not accounts:
            logger.debug("No RapidAPI X users configured, skipping.")
            return []

        api_key = os.environ.get(self.config.rapidapi_key_env)
        if not api_key:
            logger.warning(
                "RapidAPI key not found in env var '%s'. Skipping Twitter135.",
                self.config.rapidapi_key_env,
            )
            return []

        if since.tzinfo is None:
            since = since.replace(tzinfo=timezone.utc)

        request_budget = self.config.rapidapi_max_requests_per_run
        selected_accounts = accounts[:request_budget]
        if len(accounts) > request_budget:
            logger.warning(
                "Twitter135 request budget is %d; skipping %d configured accounts.",
                request_budget,
                len(accounts) - request_budget,
            )

        items: list[ContentItem] = []
        for account in selected_accounts:
            try:
                items.extend(await self._fetch_account(account, since, api_key))
            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                logger.warning(
                    "Twitter135 failed for @%s: HTTP %d", account.username, status
                )
                if status == 429:
                    break
            except (httpx.HTTPError, ValueError) as exc:
                logger.warning("Twitter135 failed for @%s: %s", account.username, exc)

        items.sort(key=lambda item: item.published_at, reverse=True)
        return items

    async def _fetch_account(
        self,
        account: RapidAPIXUserConfig,
        since: datetime,
        api_key: str,
    ) -> List[ContentItem]:
        url = f"https://{self.config.rapidapi_host}/v2/UserTweets/"
        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": self.config.rapidapi_host,
        }
        params = {
            "id": account.rest_id,
            "count": str(self.config.fetch_limit),
        }
        self.requests_used += 1
        response = await self.client.get(url, headers=headers, params=params)
        response.raise_for_status()
        payload = response.json()

        items: list[ContentItem] = []
        seen_ids: set[str] = set()
        for result in self._iter_tweet_results(payload):
            item = self._parse_tweet(result, account, since)
            if item is None or item.id in seen_ids:
                continue
            seen_ids.add(item.id)
            items.append(item)
            if len(items) >= self.config.fetch_limit:
                break
        return items

    def _parse_tweet(
        self,
        result: dict[str, Any],
        account: RapidAPIXUserConfig,
        since: datetime,
    ) -> Optional[ContentItem]:
        legacy = result.get("legacy")
        if not isinstance(legacy, dict):
            return None

        tweet_id = str(result.get("rest_id") or legacy.get("id_str") or "")
        text = self._tweet_text(result, legacy)
        created_at = self._parse_datetime(legacy.get("created_at"))
        if not tweet_id or not text or created_at is None or created_at < since:
            return None

        is_reply = bool(
            legacy.get("in_reply_to_status_id_str")
            or legacy.get("in_reply_to_user_id_str")
        )
        is_retweet = text.startswith("RT @") or bool(
            result.get("retweeted_status_result")
        )
        if is_reply and not self.config.rapidapi_include_replies:
            return None
        if is_retweet and not self.config.rapidapi_include_retweets:
            return None

        screen_name, display_name = self._author(result, account.username)
        clean_text = unescape(text).strip()
        title_text = " ".join(clean_text.split())
        if len(title_text) > 96:
            title_text = title_text[:93].rstrip() + "..."
        url = f"https://x.com/{screen_name}/status/{tweet_id}"

        views = result.get("views")
        view_count = views.get("count") if isinstance(views, dict) else None
        category = account.category or self.config.category

        return ContentItem(
            id=self._generate_id(SourceType.TWITTER.value, "tweet", tweet_id),
            source_type=SourceType.TWITTER,
            title=f"@{screen_name}: {title_text}",
            url=url,
            content=clean_text,
            author=display_name,
            published_at=created_at,
            metadata={
                "tweet_id": tweet_id,
                "conversation_id": str(legacy.get("conversation_id_str") or tweet_id),
                "favorite_count": legacy.get("favorite_count", 0),
                "retweet_count": legacy.get("retweet_count", 0),
                "reply_count": legacy.get("reply_count", 0),
                "quote_count": legacy.get("quote_count", 0),
                "view_count": view_count,
                "is_reply": is_reply,
                "is_retweet": is_retweet,
                "category": category,
                "source_variant": "twitter135_rapidapi",
                "rapidapi_account_rest_id": account.rest_id,
                "original_url": url,
                "verification_status": "unverified",
            },
        )

    @classmethod
    def _iter_tweet_results(cls, value: Any) -> Iterator[dict[str, Any]]:
        """Yield tweet result objects across Twitter135 response variants."""
        if isinstance(value, dict):
            legacy = value.get("legacy")
            if (
                isinstance(legacy, dict)
                and (legacy.get("full_text") or legacy.get("text"))
                and (value.get("rest_id") or legacy.get("id_str"))
            ):
                yield value
            for child in value.values():
                yield from cls._iter_tweet_results(child)
        elif isinstance(value, list):
            for child in value:
                yield from cls._iter_tweet_results(child)

    @classmethod
    def find_user_rest_id(cls, value: Any, username: str) -> Optional[str]:
        """Find one public numeric account ID in a UserByScreenName response."""
        expected = username.strip().lstrip("@").lower()
        if isinstance(value, dict):
            legacy = value.get("legacy")
            core = value.get("core")
            screen_name = ""
            if isinstance(legacy, dict):
                screen_name = str(legacy.get("screen_name") or "")
            if not screen_name and isinstance(core, dict):
                screen_name = str(core.get("screen_name") or "")
            rest_id = str(value.get("rest_id") or "")
            if screen_name.lower() == expected and rest_id.isdigit():
                return rest_id
            for child in value.values():
                result = cls.find_user_rest_id(child, expected)
                if result:
                    return result
        elif isinstance(value, list):
            for child in value:
                result = cls.find_user_rest_id(child, expected)
                if result:
                    return result
        return None

    @staticmethod
    def _tweet_text(result: dict[str, Any], legacy: dict[str, Any]) -> str:
        note = result.get("note_tweet")
        if isinstance(note, dict):
            note_result = note.get("note_tweet_results", {}).get("result", {})
            if isinstance(note_result, dict) and note_result.get("text"):
                return str(note_result["text"])
        return str(legacy.get("full_text") or legacy.get("text") or "")

    @staticmethod
    def _author(result: dict[str, Any], fallback: str) -> tuple[str, str]:
        core = result.get("core")
        if isinstance(core, dict):
            user_result = core.get("user_results", {}).get("result", {})
            if isinstance(user_result, dict):
                user_legacy = user_result.get("legacy", {})
                user_core = user_result.get("core", {})
                if isinstance(user_legacy, dict):
                    screen_name = str(
                        user_legacy.get("screen_name")
                        or (
                            user_core.get("screen_name")
                            if isinstance(user_core, dict)
                            else None
                        )
                        or fallback
                    )
                    display_name = str(
                        user_legacy.get("name")
                        or (
                            user_core.get("name")
                            if isinstance(user_core, dict)
                            else None
                        )
                        or screen_name
                    )
                    return screen_name, display_name
                if isinstance(user_core, dict):
                    screen_name = str(user_core.get("screen_name") or fallback)
                    display_name = str(user_core.get("name") or screen_name)
                    return screen_name, display_name
        return fallback, fallback

    @staticmethod
    def _parse_datetime(value: Any) -> Optional[datetime]:
        if not value:
            return None
        try:
            parsed = parsedate_to_datetime(str(value))
        except (TypeError, ValueError):
            try:
                parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
            except ValueError:
                return None
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
