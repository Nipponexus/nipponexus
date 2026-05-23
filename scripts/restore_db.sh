#!/bin/bash
# Cloudflare Pages 用: ビルド前に festivals_dump.sql から SQLite DB を復元
set -e
DB_DIR="data/sqlite"
DB_FILE="$DB_DIR/nipponexus.db"
DUMP_FILE="data/festivals_dump.sql"

mkdir -p "$DB_DIR"

if [ ! -f "$DUMP_FILE" ]; then
  echo "[ERROR] $DUMP_FILE not found"
  exit 1
fi

# 既存DBを削除して再構築
rm -f "$DB_FILE"
sqlite3 "$DB_FILE" < "$DUMP_FILE"
echo "[OK] DB restored from $DUMP_FILE"
sqlite3 "$DB_FILE" "SELECT COUNT(*) FROM festivals;" | xargs -I {} echo "[OK] festivals count: {}"
