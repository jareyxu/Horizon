import asyncio
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

import httpx

from src.ai.analyzer import ContentAnalyzer
from src.models import Config, ContentItem, FollowBuildersConfig, OSSInsightConfig, ProfileConfig, SourceType, VerificationConfig, WebSourceConfig
from src.orchestrator import HorizonOrchestrator
from src.scrapers.follow_builders import FollowBuildersScraper
from src.scrapers.ossinsight import OSSInsightScraper
from src.scrapers.web import WebScraper
from src.services.verification import SourceVerifier
from src.storage.manager import StorageManager


def news(source=SourceType.RSS, **kwargs):
    return ContentItem(id='test:1', source_type=source, title='AI news', url='https://example.com/story', published_at=datetime.now(timezone.utc), **kwargs)


def config(**overrides):
    data = {'ai': {'provider': 'openai', 'model': 'test', 'api_key_env': 'TEST_KEY'}, 'sources': {'hackernews': {'enabled': False}, 'reddit': {'enabled': False}, 'telegram': {'enabled': False}}, 'filtering': {}}
    data.update(overrides)
    return Config.model_validate(data)


def test_relative_days_and_weeks_are_collected_and_unknown_dates_reported(tmp_path):
    source = WebSourceConfig(name='Cards', url='https://example.com/', mode='cards', link_selector='a')
    html = '<a href="/one"><h3>One</h3><time>2d ago</time></a><a href="/two"><h3>Two</h3><time>1 week ago</time></a><a href="/three"><time>yesterday-ish</time></a>'
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(200, text=html))) as client:
            scraper = WebScraper([source], client, tmp_path/'state.json')
            items = await scraper.fetch(datetime.now(timezone.utc)-timedelta(days=8))
            return items, scraper.diagnostics['Cards']
    items, health = asyncio.run(run())
    assert [i.title for i in items] == ['One', 'Two']
    assert abs((datetime.now(timezone.utc)-items[0].published_at).total_seconds()-2*86400) < 5
    assert items[0].metadata['date_precision'] == 'relative'
    assert health['status'] == 'partial'
    assert health['date_parse_failures'] == 1


def test_anthropic_selector_accepts_titles_without_inline_time(tmp_path):
    source = next(s for s in Config.model_validate_json(Path('data/config.github.json').read_text()).sources.web if s.name == 'Anthropic News')
    html = '<a href="/news/announcements">Category</a><a class="TableView-module__title-link" href="/news/new-product">Product</a>'
    article = '<meta property="article:published_time" content="'+datetime.now(timezone.utc).isoformat()+'"><main><h1>New product</h1>Original article.</main>'
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(200,text=html if r.url.path == '/news' else article))) as client:
            return await WebScraper([source],client,tmp_path/'state.json').fetch(datetime.now(timezone.utc)-timedelta(days=1))
    assert [i.title for i in asyncio.run(run())] == ['New product']


def test_empty_selector_and_403_have_distinct_health(tmp_path):
    sources = [WebSourceConfig(name='Empty',url='https://example.com/empty'),WebSourceConfig(name='Restricted',url='https://example.com/restricted',fallback_sources=['Official RSS'])]
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(403 if r.url.path == '/restricted' else 200,text='<main>No links</main>'))) as client:
            scraper=WebScraper(sources,client,tmp_path/'state.json');await scraper.fetch(datetime.now(timezone.utc)-timedelta(days=1));return scraper.diagnostics
    health=asyncio.run(run())
    assert health['Empty']['status']=='no_matching_links'
    assert health['Restricted']['status']=='restricted'
    assert health['Restricted']['fallback_sources']==['Official RSS']


def test_oss_unavailable_quality_discards_even_nonempty_rows():
    payload={'data':{'rows':[{'repo_id':1,'repo_name':'owner/ai','stars':100}]},'data_quality':{'status':'unavailable','reason':'Insufficient coverage'}}
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r:httpx.Response(200,json=payload))) as client:
            scraper=OSSInsightScraper(OSSInsightConfig(enabled=True,languages=['Python']),client)
            items=await scraper.fetch(datetime.now(timezone.utc));return items,scraper.diagnostics
    items,health=asyncio.run(run())
    assert items==[]
    assert health['Python']['status']=='data_unavailable'


def test_follow_builder_failures_empty_and_old_content_are_separate():
    now=datetime.now(timezone.utc)
    def handler(r):
        if r.url.path.endswith('feed-x.json'):return httpx.Response(503)
        if r.url.path.endswith('feed-blogs.json'):return httpx.Response(200,json={'generatedAt':now.isoformat(),'blogs':[]})
        return httpx.Response(200,json={'generatedAt':now.isoformat(),'podcasts':[{'guid':'old','title':'Old episode','url':'https://example.com/old','publishedAt':(now-timedelta(days=10)).isoformat()}]})
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper=FollowBuildersScraper(FollowBuildersConfig(enabled=True),client)
            assert await scraper.fetch(now-timedelta(days=7))==[]
            return scraper.diagnostics
    health=asyncio.run(run())
    assert {key:value['status'] for key,value in health.items()}=={'x':'unavailable','blog':'empty_feed','podcast':'no_recent_items'}
    assert health['podcast']['latest_published_at']


def test_feed_entries_are_not_marked_original_verified():
    now=datetime.now(timezone.utc)
    items=FollowBuildersScraper(FollowBuildersConfig(),None)._parse_blogs({'blogs':[{'title':'Title','url':'https://example.com/article','publishedAt':now.isoformat()}]},now-timedelta(days=1),now)
    assert items[0].metadata['verification_status']=='feed_provided'


def test_different_domains_do_not_upgrade_verification():
    item=news(metadata={'verification_status':'unverified','sources':[{'url':'https://other.example/story'}]})
    SourceVerifier.finalize_corroboration([item])
    assert item.metadata['verification_status']=='unverified'
    assert item.metadata['coverage_status']=='multiple_domains'


def test_challenge_page_is_not_original_text():
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r:httpx.Response(200,text='<div id="challenge-form">Wait</div>',headers={'content-type':'text/html'}))) as client:
            item=news();await SourceVerifier(VerificationConfig(enabled=True))._verify_item(item,client);return item
    assert asyncio.run(run()).metadata['verification_status']=='unverified'


def test_source_health_run_files_do_not_overwrite_and_latest_updates(tmp_path):
    storage=StorageManager(str(tmp_path))
    first=storage.save_source_health('2026-10-26',{'run_status':'fetched'})
    second=storage.save_source_health('2026-10-26',{'run_status':'failed'})
    assert first!=second
    storage.save_source_health('2026-10-26',{'run_status':'success'},first)
    assert json.loads(first.read_text())['run_status']=='success'
    assert json.loads(second.read_text())['run_status']=='failed'
    assert json.loads((tmp_path/'source-health/latest.json').read_text())['run_status']=='success'


def test_failed_fetch_is_persisted_without_hiding_other_source(tmp_path):
    orchestrator=HorizonOrchestrator(config(),StorageManager(str(tmp_path)))
    class Broken:
        async def fetch(self,since):raise httpx.ConnectError('Offline')
    class Good:
        diagnostics={'Feed':{'status':'ok','items':1}}
        async def fetch(self,since):return [news(metadata={'feed_name':'Feed'})]
    async def run():
        results=await asyncio.gather(orchestrator._fetch_with_progress('Broken',Broken(),datetime.now(timezone.utc)),orchestrator._fetch_with_progress('RSS Feeds',Good(),datetime.now(timezone.utc)),return_exceptions=True)
        items=results[1];orchestrator._save_source_health('fetched',fetched=items)
    asyncio.run(run())
    health=json.loads((tmp_path/'source-health/latest.json').read_text())['sources']
    assert health['Broken']['status']=='unavailable'
    assert health['RSS Feeds/Feed']['fetched_items']==1


def test_creator_prefilter_keeps_feature_releases_and_ai_in_body(tmp_path):
    orchestrator=HorizonOrchestrator(config(profile={'editorial_mode':'creator'},filtering={'creator_prefilter':True}),StorageManager(str(tmp_path)))
    routine=news(SourceType.GITHUB,content='Fix crash on exit',metadata={'tag':'v1.0.1'})
    feature=news(SourceType.GITHUB,content='Added voice conversations',metadata={'tag':'v1.1'})
    hn=news(SourceType.HACKERNEWS,content='A new language model for audio')
    other=news(SourceType.HACKERNEWS,content='A recipe collection');other.title='Cooking today'
    assert orchestrator._creator_prefilter_reason(routine)
    assert orchestrator._creator_prefilter_reason(other)
    assert orchestrator._creator_prefilter_reason(feature) is None
    assert orchestrator._creator_prefilter_reason(hn) is None


def test_selective_short_excerpt_does_not_send_full_body_or_comments():
    class Client:
        config=SimpleNamespace(analysis_input='title',screening_excerpt_sources=[SourceType.WEB],screening_excerpt_chars=100)
        async def complete(self,**kwargs):
            assert 'Useful excerpt' in kwargs['user']
            assert 'TRAILING_BODY' not in kwargs['user']
            assert 'PRIVATE_COMMENT' not in kwargs['user']
            return json.dumps({'score':6})
    item=news(SourceType.WEB,content='Useful excerpt '+('x'*150)+'TRAILING_BODY\n--- Top Comments ---\nPRIVATE_COMMENT')
    asyncio.run(ContentAnalyzer(Client())._analyze_item(item))
    assert item.metadata['analysis_input']=='excerpt'


def test_github_drafts_and_prereleases_do_not_become_regular_releases():
    from src.models import GitHubSourceConfig
    from src.scrapers.github import GitHubScraper
    now=datetime.now(timezone.utc)
    releases=[{'id':index,'tag_name':f'v{index}','html_url':f'https://github.com/owner/repo/releases/tag/v{index}','published_at':None if index==3 else now.isoformat(),'author':{'login':'owner'},'prerelease':index==2,'draft':index==3} for index in range(1,4)]
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r:httpx.Response(200,json=releases))) as client:
            scraper=GitHubScraper([GitHubSourceConfig(type='repo_releases',owner='owner',repo='repo',include_prereleases=False)],client)
            return await scraper.fetch(now-timedelta(days=1))
    assert [i.metadata['tag'] for i in asyncio.run(run())]==['v1']


def test_fetch_stage_persists_source_health_before_any_ai(tmp_path,monkeypatch):
    cfg=config(sources={'rss':[{'name':'Offline RSS','url':'https://example.com/feed'}],'hackernews':{'enabled':False},'reddit':{'enabled':False},'telegram':{'enabled':False}})
    real_client=httpx.AsyncClient
    monkeypatch.setattr('src.orchestrator.httpx.AsyncClient',lambda **kw:real_client(transport=httpx.MockTransport(lambda r:httpx.Response(403)),**kw))
    orchestrator=HorizonOrchestrator(cfg,StorageManager(str(tmp_path)))
    assert asyncio.run(orchestrator.fetch_all_sources(datetime.now(timezone.utc)-timedelta(days=1)))==[]
    health=json.loads((tmp_path/'source-health/latest.json').read_text())
    assert health['run_status']=='fetched'
    assert health['sources']['RSS Feeds/Offline RSS']['status']=='restricted'
    assert health['sources']['RSS Feeds/Offline RSS']['fetched_items']==0


def test_single_collector_name_is_not_duplicated_in_stage_counts(tmp_path):
    orchestrator=HorizonOrchestrator(config(),StorageManager(str(tmp_path)))
    class Collector:
        diagnostics={'AI HOT':{'status':'ok','items':1}}
        async def fetch(self,since):return [news(SourceType.AIHOT,metadata={'upstream_source':'AI HOT'})]
    async def run():
        items=await orchestrator._fetch_with_progress('AI HOT',Collector(),datetime.now(timezone.utc))
        orchestrator._save_source_health('fetched',fetched=items)
        return items
    items=asyncio.run(run())
    assert items[0].metadata['source_health_keys']==['AI HOT']
    assert orchestrator.source_health['AI HOT']['fetched_items']==1
