import asyncio
from datetime import datetime, timedelta, timezone

import httpx

from src.models import FollowBuildersConfig
from src.scrapers.follow_builders import FollowBuildersScraper


def test_follow_builders_parses_three_feeds_and_compacts_transcript():
    now = datetime.now(timezone.utc)
    generated = now.isoformat()
    published = (now - timedelta(hours=1)).isoformat()
    transcript = "A" * 10000

    def handler(request: httpx.Request) -> httpx.Response:
        path = request.url.path
        if path.endswith("feed-x.json"):
            payload = {
                "generatedAt": generated,
                "x": [
                    {
                        "name": "Builder",
                        "handle": "builder",
                        "bio": "Builds things",
                        "tweets": [
                            {
                                "id": "123",
                                "text": "A useful AI engineering update",
                                "createdAt": published,
                                "url": "https://x.com/builder/status/123",
                                "likes": 10,
                                "retweets": 2,
                                "replies": 3,
                            }
                        ],
                    }
                ],
            }
        elif path.endswith("feed-podcasts.json"):
            payload = {
                "generatedAt": generated,
                "podcasts": [
                    {
                        "name": "Podcast",
                        "title": "Agent systems",
                        "guid": "episode-1",
                        "url": "https://example.com/podcast",
                        "publishedAt": published,
                        "transcript": transcript,
                    }
                ],
            }
        else:
            payload = {
                "generatedAt": generated,
                "blogs": [
                    {
                        "name": "Official Blog",
                        "title": "New release",
                        "url": "https://example.com/blog",
                        "publishedAt": published,
                        "author": "Team",
                        "content": "Release details",
                    }
                ],
            }
        return httpx.Response(200, json=payload)

    config = FollowBuildersConfig(enabled=True, transcript_max_chars=4000)

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = FollowBuildersScraper(config, client)
            return await scraper.fetch(now - timedelta(hours=24))

    items = asyncio.run(run())

    assert {item.metadata["source_variant"] for item in items} == {
        "x",
        "podcast",
        "blog",
    }
    podcast = next(
        item for item in items if item.metadata["source_variant"] == "podcast"
    )
    assert len(podcast.content or "") <= 4000
    assert podcast.metadata["transcript_compacted"] is True


def test_follow_builders_skips_stale_feeds():
    generated = (datetime.now(timezone.utc) - timedelta(days=3)).isoformat()

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, json={"generatedAt": generated, "x": [], "podcasts": [], "blogs": []}
        )

    config = FollowBuildersConfig(enabled=True, max_feed_age_hours=48)

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = FollowBuildersScraper(config, client)
            return await scraper.fetch(datetime.now(timezone.utc) - timedelta(days=7))

    items = asyncio.run(run())

    assert items == []
