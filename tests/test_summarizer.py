"""Unit tests for daily summary rendering."""

import asyncio
from datetime import datetime, timezone

from src.ai.summarizer import DailySummarizer
from src.models import ContentItem, SourceType


def _run_async(coro):
    return asyncio.run(coro)


def _make_item(idx: int) -> ContentItem:
    item = ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=f"Important Item {idx}",
        url=f"https://example.com/items/{idx}",
        content="content",
        author="tester",
        published_at=datetime(2026, 4, 25, 8, 0, tzinfo=timezone.utc),
    )
    item.ai_score = 8.0
    item.ai_summary = f"Summary for item {idx}."
    item.ai_tags = ["AI", "News"]
    return item


def test_generate_webhook_overview_lists_items_without_full_details():
    summarizer = DailySummarizer()
    items = [_make_item(1), _make_item(2)]

    result = summarizer.generate_webhook_overview(
        items,
        date="2026-04-25",
        total_fetched=10,
        language="en",
    )

    assert "Selected 2 important items from 10 fetched items" in result
    assert "1. [Important Item 1](https://example.com/items/1)" in result
    assert "2. [Important Item 2](https://example.com/items/2)" in result
    assert "Summary for item 1." not in result


def test_generate_webhook_item_renders_single_item_detail():
    summarizer = DailySummarizer()

    result = summarizer.generate_webhook_item(
        _make_item(1),
        language="en",
        index=1,
        total=2,
    )

    assert result.startswith("Item 1/2")
    assert "## [Important Item 1](https://example.com/items/1)" in result
    assert "Summary for item 1." in result
    assert "**Tags**: `#AI`, `#News`" in result


def test_generate_webhook_item_includes_discussion_link_when_distinct():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["discussion_url"] = "https://news.ycombinator.com/item?id=1"

    result = summarizer.generate_webhook_item(
        item,
        language="en",
        index=1,
        total=1,
    )

    assert (
        "tester · Apr 25, 08:00 · [Discussion](https://news.ycombinator.com/item?id=1)"
        in result
    )


def test_generate_webhook_item_omits_discussion_link_when_same_as_item_url():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["discussion_url"] = item.url

    result = summarizer.generate_webhook_item(
        item,
        language="en",
        index=1,
        total=1,
    )

    assert "[Discussion](https://example.com/items/1)" not in result


def test_generate_webhook_item_uses_localized_discussion_label():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["discussion_url"] = (
        "https://www.reddit.com/r/python/comments/abc123/test/"
    )

    result = summarizer.generate_webhook_item(
        item,
        language="zh",
        index=1,
        total=1,
    )

    assert "[社区讨论](https://www.reddit.com/r/python/comments/abc123/test/)" in result


def test_generate_summary_zh_uses_localized_selection_header_and_numeric_date():
    summarizer = DailySummarizer()
    item = _make_item(1)

    result = _run_async(
        summarizer.generate_summary(
            [item],
            date="2026-04-25",
            total_fetched=10,
            language="zh",
        )
    )

    assert "> 从 10 条内容中筛选出 1 条重要资讯。" in result
    assert "rss · tester · 4月25日 08:00" in result
    assert "From 10 items" not in result
    assert "Apr 25, 08:00" not in result


def test_generate_empty_summary_zh_uses_localized_analyzed_line():
    summarizer = DailySummarizer()

    result = _run_async(
        summarizer.generate_summary(
            [],
            date="2026-04-25",
            total_fetched=10,
            language="zh",
        )
    )

    assert "> 已分析 10 条内容，但没有达到重要性阈值的条目。" in result
    assert "Analyzed 10 items" not in result


def test_tracked_x_archive_renders_only_unselected_posts_with_full_content():
    summarizer = DailySummarizer()
    selected = _make_item(1)
    selected.source_type = SourceType.TWITTER
    selected.metadata.update(
        {
            "source_variant": "twitter135_rapidapi",
            "rapidapi_account_username": "dotey",
        }
    )
    archived = ContentItem(
        id="twitter:tweet:2",
        source_type=SourceType.TWITTER,
        title="@op7418: 一条没有进入主列表的推文",
        url="https://x.com/op7418/status/2",
        content="完整推文第一行\n\n完整推文第二行",
        author="op7418",
        published_at=datetime(2026, 7, 13, 2, 0, tzinfo=timezone.utc),
        metadata={
            "source_variant": "twitter135_rapidapi",
            "rapidapi_account_username": "op7418",
            "favorite_count": 5,
            "retweet_count": 2,
            "reply_count": 1,
            "view_count": "100",
        },
        ai_score=4.5,
    )

    result = summarizer.generate_tracked_x_archive(
        [selected, archived], {selected.id}, language="zh"
    )

    assert "## 其他追踪推文" in result
    assert "@op7418" in result
    assert "⭐️ 4.5/10" in result
    assert "> 完整推文第一行\n>\n> 完整推文第二行" in result
    assert "喜欢 5 · 转发 2 · 回复 1 · 浏览 100" in result
    assert "Important Item 1" not in result


def test_tracked_x_archive_is_empty_when_every_post_is_selected():
    item = _make_item(1)
    item.metadata["source_variant"] = "twitter135_rapidapi"

    result = DailySummarizer().generate_tracked_x_archive(
        [item], {item.id}, language="en"
    )

    assert result == ""
