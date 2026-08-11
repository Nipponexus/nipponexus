#!/bin/bash
# Nipponexus nightly: 生成 -> ダンプ -> 差分があれば commit -> push
set -e
cd ~/nipponexus
LOG="$HOME/.openclaw/logs/nipponexus_nightly.log"
mkdir -p "$(dirname "$LOG")"
echo "===== $(date '+%F %T') nightly start =====" >> "$LOG"

/usr/bin/python3 steps/daily_cal.py >> "$LOG" 2>&1
/usr/bin/python3 steps/step92.py   >> "$LOG" 2>&1
/usr/bin/python3 scripts/dump_festivals.py >> "$LOG" 2>&1

T="data/festivals_dump.sql out/site_calendar.json out/site_corrections.json"
CH=0
git diff --quiet -- $T || CH=1
UP=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
if [ "$CH" = "0" ] && [ "$UP" = "0" ]; then
  echo "[INFO] no changes, skip push" >> "$LOG"; exit 0
fi
if [ "$CH" = "1" ]; then
  git add $T
  git commit -m "chore: nightly update ($(date '+%F'))" >> "$LOG" 2>&1
fi
source ~/.openclaw/.env
git push "https://${GITHUB_TOKEN_NIPPONEXUS}@github.com/Nipponexus/nipponexus.git" main >> "$LOG" 2>&1
echo "[OK] pushed" >> "$LOG"
