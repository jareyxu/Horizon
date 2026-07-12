#!/usr/bin/env python3
"""Read-only smoke check for the public AI HOT and Follow Builders sources."""

from __future__ import annotations

import asyncio
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path

import httpx

from src.models import Config
from src.scrapers.aihot import AIHotScraper
from src.scrapers.follow_builders import FollowBuildersScraper


async def main() -> None:
    config = Config.model_validate(
        json.loads(Path("data/config.github.json").read_text(encoding="utf-8"))
    )
    since = datetime.now(timezone.utc) - timedelta(hours=24)
    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        results = await asyncio.gather(
            AIHotScraper(config.sources.aihot, client).fetch(since),
            FollowBuildersScraper(config.sources.follow_builders, client).fetch(since),
        )

    aihot_items, builder_items = results
    variants: dict[str, int] = {}
    for item in builder_items:
        variant = str(item.metadata.get("source_variant") or "unknown")
        variants[variant] = variants.get(variant, 0) + 1
    print(
        json.dumps(
            {
                "aihot": len(aihot_items),
                "follow_builders": len(builder_items),
                "follow_builders_variants": variants,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
