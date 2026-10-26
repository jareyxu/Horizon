"""Read-only public-source smoke check; no AI, paid X, delivery or live baseline changes."""

import argparse
import asyncio
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from src.models import Config
from src.orchestrator import HorizonOrchestrator
from src.storage.manager import StorageManager


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', default='data/config.github.json')
    parser.add_argument('--hours', type=int, default=24)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    config = Config.model_validate_json(Path(args.config).read_text())
    # All X backends can incur paid usage or use account sessions.
    if config.sources.twitter:
        config.sources.twitter.enabled = False
    if config.sources.openbb:
        config.sources.openbb.enabled = False
    since = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    with TemporaryDirectory(prefix='horizon-health-') as temporary:
        orchestrator = HorizonOrchestrator(config, StorageManager(temporary), delivery_enabled=False)
        items = await orchestrator.fetch_all_sources(since)
        merged = orchestrator.merge_cross_source_duplicates(items)
        skipped = [i for i in merged if orchestrator._creator_prefilter_reason(i)]
        orchestrator._save_source_health('smoke_checked', merged=merged, prefiltered=skipped)
        result = {'checked_at': datetime.now(timezone.utc).isoformat(), 'window_hours': args.hours, 'fetched_items': len(items), 'merged_items': len(merged), 'prefiltered_items': len(skipped), 'ai_calls': 0, 'sources': orchestrator.source_health}
        if args.output:
            args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    asyncio.run(main())
