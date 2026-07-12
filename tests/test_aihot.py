import asyncio
from datetime import datetime, timezone

import httpx

from src.models import AIHotConfig
from src.scrapers.aihot import AIHotScraper


def test_aihot_fetches_pages_filters_score_and_preserves_links():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        cursor = request.url.params.get("cursor")
        if not cursor:
            return httpx.Response(
                200,
                json={
                    "hasNext": True,
                    "nextCursor": "page-2",
                    "items": [
                        {
                            "id": "one",
                            "title": "Important model update",
                            "title_en": "Important model update",
                            "url": "https://example.com/original?utm_source=test",
                            "permalink": "https://aihot.virxact.com/items/one",
                            "source": "Example",
                            "publishedAt": "2026-07-12T01:00:00Z",
                            "summary": "中文摘要",
                            "category": "ai-models",
                            "score": 88,
                            "selected": True,
                        },
                        {
                            "id": "low",
                            "title": "Low score",
                            "url": "https://example.com/low",
                            "publishedAt": "2026-07-12T01:00:00Z",
                            "category": "tip",
                            "score": 20,
                        },
                    ],
                },
            )
        return httpx.Response(
            200,
            json={
                "hasNext": False,
                "nextCursor": None,
                "items": [
                    {
                        "id": "two",
                        "title": "Useful product launch",
                        "url": "https://example.com/two",
                        "publishedAt": "2026-07-12T02:00:00Z",
                        "summary": "第二条摘要",
                        "category": "ai-products",
                        "score": 75,
                        "selected": True,
                    }
                ],
            },
        )

    config = AIHotConfig(enabled=True, min_score=55, take=2, max_pages=2)

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = AIHotScraper(config, client)
            return await scraper.fetch(datetime(2026, 7, 11, tzinfo=timezone.utc))

    items = asyncio.run(run())

    assert [item.id for item in items] == ["aihot:item:one", "aihot:item:two"]
    assert items[0].metadata["category"] == "models"
    assert items[0].metadata["upstream_score"] == 88
    assert items[0].metadata["reader_url"] == "https://aihot.virxact.com/items/one"
    assert len(calls) == 2
    assert calls[0].headers["user-agent"].startswith("jareyxu-horizon/")
    assert calls[1].url.params["cursor"] == "page-2"
