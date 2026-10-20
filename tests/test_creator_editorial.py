import asyncio
import json
from datetime import datetime, timezone

from bs4 import BeautifulSoup

from src.ai.analyzer import ContentAnalyzer
from src.ai.summarizer import DailySummarizer
from src.models import ContentItem, Config, ProfileConfig, SourceType
from src.orchestrator import HorizonOrchestrator
from src.storage.manager import StorageManager


def item(id, **overrides):
    return ContentItem(id=id, source_type=SourceType.RSS, title=id, url=f"https://example.com/{id}", content="Original fetched text", published_at=datetime(2026, 10, 20, tzinfo=timezone.utc), **overrides)


def test_creator_rubric_caps_technical_and_translates_every_source():
    class Client:
        async def complete(self, *, system, user):
            assert "ordinary adults" in system
            assert "title_zh" in user
            return json.dumps({"score": 10, "summary": "摘要", "title_zh": "中文标题", "summary_zh": "中文摘要", "creator": {"kind": "technical", "dimensions": {k: 10 for k in ["audience", "utility", "novelty", "visual", "viewpoint", "timeliness"]}}})
    news = item("engineering")
    asyncio.run(ContentAnalyzer(Client(), ProfileConfig(editorial_mode="creator"))._analyze_item(news))
    assert news.ai_score == 5.5
    assert news.metadata["creator_eligible"] is False
    assert news.metadata["title_zh"] == "中文标题"


def test_creator_score_is_weighted_not_arbitrary_model_score():
    class Client:
        async def complete(self, **kwargs):
            return json.dumps({"score": 1, "creator": {"kind": "practical", "dimensions": {"audience": 10, "utility": 10, "novelty": 8, "visual": 8, "viewpoint": 6, "timeliness": 8}}})
    news = item("tutorial")
    asyncio.run(ContentAnalyzer(Client(), ProfileConfig(editorial_mode="creator"))._analyze_item(news))
    assert news.ai_score == 8.7
    assert news.metadata["category"] == "creator-practical"


def test_popularity_and_minimum_do_not_promote_developer_only_news(tmp_path):
    config = Config.model_validate({"ai": {"provider": "openai", "model": "test", "api_key_env": "TEST_KEY"}, "sources": {}, "profile": {"editorial_mode": "creator"}, "filtering": {"minimum_items": 5}})
    news = item("technical", ai_score=10, metadata={"personal_ai_score": 10, "source_count": 8, "upstream_score": 100, "creator_eligible": False})
    orchestrator = HorizonOrchestrator(config, StorageManager(str(tmp_path)))
    orchestrator._apply_source_scoring([news])
    assert news.ai_score == 5.5
    assert orchestrator.select_important_items([news]) == []


def test_archive_retains_raw_merged_rows_and_every_source(tmp_path):
    selected = item("selected")
    duplicate = item("duplicate")
    new_source = item("web-story")
    new_source.source_type = SourceType.WEB
    raw = [n.model_copy(deep=True) for n in [selected, duplicate, new_source]]
    selected.metadata["original_urls"] = [str(selected.url), str(duplicate.url)]
    selected.content = "Merged content, not the original"
    selected.ai_score = 9
    new_source.ai_score = 2
    pool = HorizonOrchestrator.build_candidate_archive(raw, [selected, new_source])
    assert len(pool) == 3
    assert pool[0].content == "Original fetched text"
    assert pool[1].metadata["archive_analysis_inherited"] is True
    storage = StorageManager(str(tmp_path))
    assert len(json.loads(storage.save_candidate_archive("2026-10-20", pool).read_text())) == 3
    html = DailySummarizer().generate_pages_archive_tabs([], [], {selected.id}, language="zh", all_items=pool)
    soup = BeautifulSoup(html, "html.parser")
    assert soup.select_one('[data-archive-tab="all"]')["data-count"] == "2"
    assert len(soup.select('#archive-panel-all article')) == 2
    assert "web-story" in soup.select_one('#archive-panel-all').get_text()
    assert soup.select_one('[data-archive-tab="all"]')["aria-selected"] == "true"


def test_creator_cards_and_empty_summary_have_usable_counts():
    summarizer = DailySummarizer(editorial_mode="creator")
    empty = asyncio.run(summarizer.generate_summary([], "2026-10-20", 84, "zh"))
    assert "从 84 条内容中筛选出 0 条" in empty
    news = item("story", metadata={"editorial_mode": "creator", "audience_zh": "上班族", "content_angle_zh": "一个观点", "visual_plan_zh": "实测对比", "availability_zh": "价格待核实", "verification_needed_zh": "核实地区"})
    rendered = asyncio.run(summarizer.generate_summary([news], "2026-10-20", 84, "zh"))
    assert "适合谁" in rendered and "可以怎么拍" in rendered
    assert "发布前核实" in rendered
