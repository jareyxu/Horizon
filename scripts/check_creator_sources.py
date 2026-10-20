"""Read-only source checks: no AI calls, no paid X calls, no publishing."""

import argparse
import asyncio
from datetime import datetime, timedelta, timezone
import json
import logging
from pathlib import Path
from tempfile import TemporaryDirectory

import httpx

from src.models import Config
from src.scrapers.rss import RSSScraper
from src.scrapers.web import WebScraper


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="data/config.github.json")
    parser.add_argument("--days", type=int, default=7)
    args = parser.parse_args()
    config = Config.model_validate_json(Path(args.config).read_text())
    since = datetime.now(timezone.utc) - timedelta(days=args.days)
    async with httpx.AsyncClient(timeout=25, follow_redirects=True) as client:
        with TemporaryDirectory(prefix="horizon-source-check-") as temporary:
            for kind, sources in [("rss", config.sources.rss), ("web", config.sources.web)]:
                for source in sources:
                    if not source.enabled:
                        continue
                    scraper = RSSScraper([source], client) if kind == "rss" else WebScraper([source], client, Path(temporary) / "state.json")
                    items = await scraper.fetch(since)
                    print(json.dumps({"name": source.name, "type": kind, "window_days": args.days,
                        "health": scraper.diagnostics.get(source.name, {}),
                        "items": len(items), "sample": [{"title": i.title, "date": i.published_at.isoformat(), "url": str(i.url)} for i in items[:1]]}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
