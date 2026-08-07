#!/bin/bash
# Nipponexus nightly build: SQLite に変更があれば dump→commit→push で Cloudflare Pages を再ビルド
set -e

cd ~/nipponexus
LOG_FILE="$HOME/.openclaw/logs/nipponexus_nightly.log"
mkdir -p "$(dirname "$LOG_FILE")"

echo "===== $(date '+%Y-%m-%d %H:%M:%S') nightly_rebuild start =====" >> "$LOG_FILE"

# SQLダンプを再生成
python3 scripts/dump_festivals.py >> "$LOG_FILE" 2>&1

# git に変更があるか確認
if git diff --quiet data/festivals_dump.sql; then
  echo "[INFO] No DB changes, skip push" >> "$LOG_FILE"
  exit 0
fi

# 変更がある場合のみコミット&push
git add data/festivals_dump.sql
git commit -m "chore: nightly DB dump update ($(date '+%Y-%m-%d'))" >> "$LOG_FILE" 2>&1

source ~/.openclaw/.env
git push "https://${GITHUB_TOKEN_NIPPONEXUS}@github.com/Nipponexus/nipponexus.git" main >> "$LOG_FILE" 2>&1

echo "[OK] Pushed nightly DB update" >> "$LOG_FILE"
