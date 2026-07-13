"""Tests for the Twitter135 RapidAPI X scraper."""

import asyncio
from datetime import datetime, timedelta, timezone

import httpx

from src.models import RapidAPIXUserConfig, TwitterConfig
from src.scrapers.twitter_rapidapi import TwitterRapidAPIScraper


def _config(**overrides) -> TwitterConfig:
    values = {
        "enabled": True,
        "mode": "rapidapi",
        "fetch_limit": 10,
        "category": "builders",
        "rapidapi_key_env": "RAPIDAPI_KEY",
        "rapidapi_users": [
            {"username": "karpathy", "rest_id": "33836629"},
        ],
        "rapidapi_max_requests_per_run": 3,
    }
    values.update(overrides)
    return TwitterConfig.model_validate(values)


def _tweet_result(
    tweet_id: str,
    *,
    text: str = "A useful post about agents",
    username: str = "karpathy",
    created_at: datetime | None = None,
    reply_to: str | None = None,
) -> dict:
    published = created_at or datetime.now(timezone.utc)
    return {
        "rest_id": tweet_id,
        "core": {
            "user_results": {
                "result": {
                    "legacy": {
                        "screen_name": username,
                        "name": username.capitalize(),
                    }
                }
            }
        },
        "legacy": {
            "full_text": text,
            "created_at": published.strftime("%a %b %d %H:%M:%S +0000 %Y"),
            "conversation_id_str": tweet_id,
            "favorite_count": 12,
            "retweet_count": 3,
            "reply_count": 2,
            "quote_count": 1,
            "in_reply_to_status_id_str": reply_to,
        },
        "views": {"count": "321"},
    }


def _payload(*results: dict) -> dict:
    return {
        "data": {
            "user": {
                "result": {
                    "timeline_v2": {
                        "timeline": {
                            "instructions": [
                                {
                                    "entries": [
                                        {
                                            "content": {
                                                "itemContent": {
                                                    "tweet_results": {"result": result}
                                                }
                                            }
                                        }
                                        for result in results
                                    ]
                                }
                            ]
                        }
                    }
                }
            }
        }
    }


def test_missing_key_skips_without_request(monkeypatch):
    monkeypatch.delenv("RAPIDAPI_KEY", raising=False)

    def handler(request: httpx.Request) -> httpx.Response:
        raise AssertionError(f"Unexpected request: {request.url}")

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = TwitterRapidAPIScraper(_config(), client)
            return await scraper.fetch(datetime.now(timezone.utc) - timedelta(hours=24))

    assert asyncio.run(run()) == []


def test_fetches_v2_timeline_and_filters_replies_and_old_posts(monkeypatch):
    monkeypatch.setenv("RAPIDAPI_KEY", "test-key")
    now = datetime.now(timezone.utc)
    response_payload = _payload(
        _tweet_result("101", created_at=now),
        _tweet_result("102", created_at=now, reply_to="99"),
        _tweet_result("103", created_at=now - timedelta(days=2)),
    )

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/v2/UserTweets/"
        assert request.url.params["id"] == "33836629"
        assert request.url.params["count"] == "10"
        assert request.headers["X-RapidAPI-Key"] == "test-key"
        assert request.headers["X-RapidAPI-Host"] == "twitter135.p.rapidapi.com"
        return httpx.Response(200, json=response_payload)

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = TwitterRapidAPIScraper(_config(), client)
            items = await scraper.fetch(now - timedelta(hours=24))
            return scraper, items

    scraper, items = asyncio.run(run())

    assert scraper.requests_used == 1
    assert len(items) == 1
    assert items[0].id == "twitter:tweet:101"
    assert str(items[0].url) == "https://x.com/karpathy/status/101"
    assert items[0].metadata["source_variant"] == "twitter135_rapidapi"
    assert items[0].metadata["view_count"] == "321"


def test_long_note_text_overrides_truncated_legacy_text(monkeypatch):
    monkeypatch.setenv("RAPIDAPI_KEY", "test-key")
    result = _tweet_result("201", text="Truncated...")
    result["note_tweet"] = {
        "note_tweet_results": {"result": {"text": "Complete long-form post"}}
    }

    async def run():
        transport = httpx.MockTransport(
            lambda request: httpx.Response(200, json=_payload(result))
        )
        async with httpx.AsyncClient(transport=transport) as client:
            scraper = TwitterRapidAPIScraper(_config(), client)
            return await scraper.fetch(datetime.now(timezone.utc) - timedelta(hours=24))

    items = asyncio.run(run())

    assert items[0].content == "Complete long-form post"


def test_request_budget_caps_number_of_accounts(monkeypatch):
    monkeypatch.setenv("RAPIDAPI_KEY", "test-key")
    config = _config(
        rapidapi_users=[
            {"username": "one", "rest_id": "1"},
            {"username": "two", "rest_id": "2"},
            {"username": "three", "rest_id": "3"},
        ],
        rapidapi_max_requests_per_run=2,
    )
    requested_ids: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requested_ids.append(request.url.params["id"])
        return httpx.Response(200, json={})

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = TwitterRapidAPIScraper(config, client)
            await scraper.fetch(datetime.now(timezone.utc) - timedelta(hours=24))
            return scraper.requests_used

    assert asyncio.run(run()) == 2
    assert requested_ids == ["1", "2"]


def test_one_account_failure_does_not_block_the_next(monkeypatch):
    monkeypatch.setenv("RAPIDAPI_KEY", "test-key")
    config = _config(
        rapidapi_users=[
            {"username": "broken", "rest_id": "1"},
            {"username": "working", "rest_id": "2"},
        ]
    )

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.params["id"] == "1":
            return httpx.Response(503, json={"error": "temporary"})
        return httpx.Response(
            200,
            json=_payload(_tweet_result("301", username="working")),
        )

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = TwitterRapidAPIScraper(config, client)
            return await scraper.fetch(datetime.now(timezone.utc) - timedelta(hours=24))

    items = asyncio.run(run())

    assert [item.id for item in items] == ["twitter:tweet:301"]


def test_account_config_normalizes_username():
    account = RapidAPIXUserConfig(username=" @karpathy ", rest_id="33836629")
    assert account.username == "karpathy"


def test_account_schedule_supports_daily_and_deterministic_intervals():
    daily = RapidAPIXUserConfig(username="daily", rest_id="1", fetch_every_days=1)
    alternating = RapidAPIXUserConfig(
        username="alternating",
        rest_id="2",
        fetch_every_days=2,
        schedule_offset=1,
    )

    assert TwitterRapidAPIScraper._account_is_due(daily, 100) is True
    assert TwitterRapidAPIScraper._account_is_due(daily, 101) is True
    assert TwitterRapidAPIScraper._account_is_due(alternating, 100) is False
    assert TwitterRapidAPIScraper._account_is_due(alternating, 101) is True


def test_fetch_skips_accounts_not_due_without_spending_request(monkeypatch):
    monkeypatch.setenv("RAPIDAPI_KEY", "test-key")
    run_day = datetime.now(timezone.utc).date().toordinal()
    config = _config(
        rapidapi_users=[
            {
                "username": "deferred",
                "rest_id": "1",
                "fetch_every_days": 2,
                "schedule_offset": (run_day + 1) % 2,
            },
            {"username": "daily", "rest_id": "2", "fetch_every_days": 1},
        ]
    )
    requested_ids: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requested_ids.append(request.url.params["id"])
        return httpx.Response(200, json={})

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = TwitterRapidAPIScraper(config, client)
            await scraper.fetch(datetime.now(timezone.utc) - timedelta(hours=24))
            return scraper.requests_used

    assert asyncio.run(run()) == 1
    assert requested_ids == ["2"]


def test_finds_rest_id_in_user_lookup_response():
    payload = {
        "data": {
            "user": {
                "result": {
                    "rest_id": "33836629",
                    "legacy": {"screen_name": "karpathy", "name": "Andrej"},
                }
            }
        }
    }

    assert TwitterRapidAPIScraper.find_user_rest_id(payload, "@Karpathy") == "33836629"
