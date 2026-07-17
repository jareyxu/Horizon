import asyncio
from datetime import datetime, timezone

import httpx

from src.ai.analyzer import ContentAnalyzer
from src.ai.longform import LongFormProcessor
from src.ai.summarizer import DailySummarizer
from src.models import (
    Config,
    ContentItem,
    ProfileConfig,
    SourceType,
    VerificationConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.services.verification import SourceVerifier
from src.storage.manager import StorageManager


def _config() -> Config:
    return Config.model_validate(
        {
            "profile": {
                "interests": ["AI agents", "Codex"],
                "negative_topics": ["体育"],
                "preferred_content": ["技术实现"],
            },
            "ai": {
                "provider": "openai",
                "model": "deepseek-ai/DeepSeek-V4-Flash",
                "base_url": "https://api.siliconflow.cn/v1",
                "api_key_env": "SILICONFLOW_API_KEY",
                "languages": ["zh"],
            },
            "sources": {
                "hackernews": {"enabled": False},
                "reddit": {"enabled": False},
                "telegram": {"enabled": False},
            },
            "filtering": {"ai_score_threshold": 7.5},
        }
    )


def test_profile_is_injected_into_analysis_prompt():
    class FakeClient:
        config = type("Config", (), {"analysis_concurrency": 1, "throttle_sec": 0})()

        def __init__(self):
            self.user_prompt = ""

        async def complete(self, *, system, user):
            self.user_prompt = user
            return '{"score": 8, "reason": "relevant", "summary": "summary", "tags": ["agent"]}'

    client = FakeClient()
    analyzer = ContentAnalyzer(
        client,
        ProfileConfig(
            interests=["AI agents", "Codex"],
            negative_topics=["体育"],
            preferred_content=["技术实现"],
        ),
    )
    item = ContentItem(
        id="rss:test:1",
        source_type=SourceType.RSS,
        title="Agent release",
        url="https://example.com/release",
        published_at=datetime(2026, 7, 12, tzinfo=timezone.utc),
    )

    asyncio.run(analyzer.analyze_batch([item]))

    assert "AI agents" in client.user_prompt
    assert "体育" in client.user_prompt
    assert item.metadata["personal_ai_score"] == 8.0


def test_aihot_and_multi_source_score_are_combined(tmp_path):
    config = _config()
    orchestrator = HorizonOrchestrator(config, StorageManager(str(tmp_path)))
    item = ContentItem(
        id="aihot:item:1",
        source_type=SourceType.AIHOT,
        title="Agent release",
        url="https://example.com/release",
        published_at=datetime(2026, 7, 12, tzinfo=timezone.utc),
        ai_score=8.0,
        metadata={
            "personal_ai_score": 8.0,
            "upstream_score": 80,
            "source_count": 2,
        },
    )

    orchestrator._apply_source_scoring([item])

    assert item.ai_score == 8.3


def test_selection_backfills_minimum_digest_with_highest_scores(tmp_path):
    config = _config()
    config.filtering.minimum_items = 3
    orchestrator = HorizonOrchestrator(config, StorageManager(str(tmp_path)))
    items = [
        ContentItem(
            id=f"rss:item:{index}",
            source_type=SourceType.RSS,
            title=f"Item {index}",
            url=f"https://example.com/{index}",
            published_at=datetime(2026, 7, 12, tzinfo=timezone.utc),
            ai_score=score,
        )
        for index, score in enumerate([7.8, 6.9, 5.5, 0.0])
    ]

    selected = orchestrator.select_important_items(items)

    assert [item.ai_score for item in selected] == [7.8, 6.9, 5.5]


def test_verifier_extracts_original_and_renderer_shows_status():
    html = "<html><head><title>Original title</title></head><body><article>Verified facts here.</article></body></html>"

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, text=html, headers={"content-type": "text/html"})

    item = ContentItem(
        id="aihot:item:1",
        source_type=SourceType.AIHOT,
        title="News",
        url="https://example.com/news",
        published_at=datetime(2026, 7, 12, tzinfo=timezone.utc),
        ai_score=8.0,
        ai_summary="摘要",
        metadata={
            "reader_url": "https://aihot.virxact.com/items/1",
            "verification_status": "unverified",
        },
    )
    verifier = SourceVerifier(VerificationConfig(enabled=True))

    async def verify():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            await verifier._verify_item(item, client)

    asyncio.run(verify())

    rendered = asyncio.run(
        DailySummarizer().generate_summary([item], "2026-07-12", 1, language="zh")
    )

    assert item.metadata["verification_status"] == "original_checked"
    assert "Verified facts here" in item.metadata["verified_excerpt"]
    assert "已核对原文" in rendered
    assert "中文阅读" in rendered


def test_longform_processor_summarizes_all_chunks_in_order():
    class FakeClient:
        async def complete(self, *, system, user):
            marker = user.split("片段 ", 1)[1].split("：", 1)[0]
            return f"摘要 {marker}"

    item = ContentItem(
        id="follow_builders:podcast:1",
        source_type=SourceType.FOLLOW_BUILDERS,
        title="Long podcast",
        url="https://example.com/podcast",
        content=("第一段内容。" * 1000) + "\n\n" + ("第二段内容。" * 1000),
        published_at=datetime(2026, 7, 12, tzinfo=timezone.utc),
        metadata={"source_variant": "podcast"},
    )
    processor = LongFormProcessor(FakeClient(), chunk_chars=3000, max_chunks=6)

    asyncio.run(processor.process_batch([item]))

    assert item.metadata["longform_summarized"] is True
    assert item.metadata["longform_chunk_count"] == 4
    assert item.content.index("摘要 1/4") < item.content.index("摘要 4/4")
