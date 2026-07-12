"""Lightweight original-source verification for shortlisted items."""

from __future__ import annotations

import asyncio
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import httpx

from ..models import ContentItem, SourceType, VerificationConfig


class SourceVerifier:
    """Check original pages and preserve a grounded excerpt for enrichment."""

    def __init__(self, config: VerificationConfig):
        self.config = config

    async def verify_batch(self, items: list[ContentItem]) -> None:
        if not self.config.enabled or not items:
            return

        targets: list[ContentItem] = []
        for index, item in enumerate(items):
            upstream_score = item.metadata.get("upstream_score")
            is_high_aihot = (
                item.source_type == SourceType.AIHOT
                and isinstance(upstream_score, (int, float))
                and upstream_score >= self.config.aihot_min_score
            )
            if index < self.config.top_n or is_high_aihot:
                targets.append(item)

        semaphore = asyncio.Semaphore(self.config.concurrency)
        async with httpx.AsyncClient(
            timeout=20.0,
            follow_redirects=True,
            headers={"User-Agent": self.config.user_agent},
        ) as client:

            async def _verify(item: ContentItem) -> None:
                async with semaphore:
                    await self._verify_item(item, client)

            await asyncio.gather(*(_verify(item) for item in targets))

    async def _verify_item(
        self,
        item: ContentItem,
        client: httpx.AsyncClient,
    ) -> None:
        try:
            response = await client.get(str(item.url))
            response.raise_for_status()
            content_type = response.headers.get("content-type", "")
            if "html" not in content_type and "text" not in content_type:
                item.metadata["verification_status"] = "original_reachable"
                return

            soup = BeautifulSoup(response.text, "html.parser")
            for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
                tag.decompose()
            title = soup.title.get_text(" ", strip=True) if soup.title else ""
            text = " ".join(soup.get_text(" ", strip=True).split())
            excerpt = text[: self.config.max_excerpt_chars]
            if excerpt:
                item.metadata["verified_excerpt"] = excerpt
                item.content = (
                    (item.content or "")
                    + "\n\n--- Original Source Excerpt ---\n"
                    + excerpt
                )
            if title:
                item.metadata["original_title"] = title
            item.metadata["verification_status"] = "original_checked"
        except Exception as exc:
            item.metadata["verification_status"] = "unverified"
            item.metadata["verification_error"] = type(exc).__name__

    @staticmethod
    def finalize_corroboration(items: list[ContentItem]) -> None:
        """Upgrade verification when enrichment found another independent domain."""
        for item in items:
            primary_domain = urlparse(str(item.url)).hostname or ""
            source_domains = {
                urlparse(str(source.get("url", ""))).hostname or ""
                for source in item.metadata.get("sources", [])
                if isinstance(source, dict)
            }
            source_domains.discard("")
            if any(domain != primary_domain for domain in source_domains):
                item.metadata["verification_status"] = "corroborated"
