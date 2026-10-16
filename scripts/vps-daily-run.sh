#!/usr/bin/env bash
set -euo pipefail
export TZ=Asia/Shanghai
export PATH="/opt/horizon/.local/bin:/usr/local/bin:/usr/bin:/bin"
cd /opt/horizon/app
exec 9>/opt/horizon/state/run.lock
flock -n 9 || exit 0
report_date=$(date +%F)
if [[ ${HORIZON_FORCE:-0} != 1 && -f /opt/horizon/state/success-$report_date ]]; then
  echo "Already published $report_date"
  exit 0
fi
git pull --ff-only origin main
uv sync --frozen --no-dev
cp data/config.github.json data/config.json
uv run --no-sync horizon --hours "${HORIZON_HOURS:-24}"
test -s "docs/_posts/$report_date-summary-zh.md"
cd /opt/horizon/pages
git pull --ff-only origin gh-pages
cp -a /opt/horizon/app/docs/. ./
git add -A
if ! git diff --cached --quiet; then
  git commit -m "Daily Summary: $report_date (VPS)"
fi
for attempt in 1 2 3; do
  if git push origin HEAD:gh-pages; then
    touch "/opt/horizon/state/success-$report_date"
    exit 0
  fi
  git pull --rebase origin gh-pages
  sleep 10
done
exit 1
