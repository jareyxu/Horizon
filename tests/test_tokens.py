import asyncio

from src.ai.tokens import get_usage_snapshot, record_usage, reset_usage, usage_stage
from src.storage.manager import StorageManager


def test_stage_usage_is_async_isolated_and_reasoning_is_not_double_counted(tmp_path):
    reset_usage()
    async def record(stage, incoming, outgoing, reasoning=None):
        with usage_stage(stage):
            await asyncio.sleep(0)
            record_usage("openai", incoming, outgoing, reasoning)
    async def run():
        await asyncio.gather(record("scoring", 100, 40, 30), record("summary", 200, 60))
    asyncio.run(run())
    snapshot = get_usage_snapshot()
    assert snapshot.total_tokens == 400
    assert snapshot.per_stage["scoring"].reasoning_tokens == 30
    assert snapshot.per_stage["scoring"].reasoning_reported_calls == 1
    assert snapshot.per_stage["summary"].reasoning_reported_calls == 0
    assert snapshot.per_provider["openai"].reported_calls == 2
    record_usage("openai", 1, 1)
    assert snapshot.per_provider["openai"].reported_calls == 2
    storage = StorageManager(str(tmp_path))
    first = storage.save_token_usage("2026-10-20", snapshot.to_dict())
    second = storage.save_token_usage("2026-10-20", snapshot.to_dict())
    assert first != second
    assert '"per_stage"' in first.read_text()
    reset_usage()
    assert get_usage_snapshot().total_tokens == 0
    assert get_usage_snapshot().per_stage == {}
