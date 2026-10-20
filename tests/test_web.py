import asyncio
from datetime import datetime, timezone

import httpx
from bs4 import BeautifulSoup

from src.models import WebSourceConfig
from src.scrapers.web import WebScraper


def test_public_articles_skip_undated_and_isolate_http_failure(tmp_path):
    pages = {
        "/": '<a href="/old">old</a><a href="/broken">bad</a><a href="/new">new</a>',
        "/old": '<main><h1>Old without date</h1>body</main>',
        "/new": '<meta property="article:published_time" content="2026-10-19T03:00:00Z"><main><h1>New</h1>Useful text</main>',
    }
    def handler(request):
        return httpx.Response(403 if request.url.path == "/broken" else 200, text=pages.get(request.url.path, ""))
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = WebScraper([WebSourceConfig(name="Test", url="https://example.com/", link_selector="a")], client, tmp_path / "state.json")
            return await scraper.fetch(datetime(2026, 10, 18, tzinfo=timezone.utc))
    items = asyncio.run(run())
    assert [i.title for i in items] == ["New"]
    assert items[0].published_at == datetime(2026, 10, 19, 3, tzinfo=timezone.utc)


def test_snapshot_baselines_then_only_reports_actual_change(tmp_path):
    source = WebSourceConfig(name="Product", url="https://example.com/", mode="snapshot")
    scraper = WebScraper([], None, tmp_path / "state.json")
    first = BeautifulSoup('<main>' + 'Product capability. ' * 12 + '</main>', "html.parser")
    second = BeautifulSoup('<main>' + 'New capability. ' * 12 + '</main>', "html.parser")
    assert scraper._snapshot(source, first) == []
    assert scraper._snapshot(source, first) == []
    changed = scraper._snapshot(source, second)
    assert changed[0].metadata["requires_verification"] is True
    assert changed[0].metadata["observed_change"] is True
    assert scraper._snapshot(source, second) == []


def test_changelog_keeps_sections_separate():
    source = WebSourceConfig(name="Updates", url="https://example.com/log", mode="changelog")
    soup = BeautifulSoup('<article><h1>Release notes</h1><h2>October 19, 2026</h2><h3>Feature A</h3><p>Alpha</p><h2>October 18, 2026</h2><p>Beta</p></article>', "html.parser")
    items = WebScraper([], None)._changelog(source, soup)
    assert len(items) == 2
    assert "Alpha" in items[0].content and "Beta" not in items[0].content
    assert items[0].id != items[1].id


def test_chinese_publication_date_uses_beijing_timezone():
    soup = BeautifulSoup('<main>发布时间 : 2026年10月20号 17:55</main>', "html.parser")
    assert WebScraper._published(soup) == datetime(2026, 10, 20, 9, 55, tzinfo=timezone.utc)


def test_modified_date_does_not_create_news():
    soup = BeautifulSoup('<meta property="article:modified_time" content="2026-10-20T12:00:00Z">', "html.parser")
    assert WebScraper._published(soup) is None
