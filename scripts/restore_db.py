#!/usr/bin/env python3
"""Cloudflare Pages 用: festivals_dump.sql から SQLite DB を復元（Python標準ライブラリのみ）"""
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_DIR = ROOT / "data" / "sqlite"
DB_FILE = DB_DIR / "nipponexus.db"
DUMP_FILE = ROOT / "data" / "festivals_dump.sql"

DB_DIR.mkdir(parents=True, exist_ok=True)

if not DUMP_FILE.exists():
    print(f"[ERROR] {DUMP_FILE} not found", file=sys.stderr)
    sys.exit(1)

import os
if DB_FILE.exists() and DUMP_FILE.exists() and not os.environ.get("NX_FORCE_RESTORE"):
    if DB_FILE.stat().st_mtime > DUMP_FILE.stat().st_mtime:
        print("[ABORT] DB is newer than dump. Set NX_FORCE_RESTORE=1 to override.", file=sys.stderr)
        sys.exit(1)

if DB_FILE.exists():
    DB_FILE.unlink()

sql = DUMP_FILE.read_text(encoding="utf-8")
conn = sqlite3.connect(DB_FILE)
conn.executescript(sql)
conn.commit()

cur = conn.execute("SELECT COUNT(*) FROM festivals")
count = cur.fetchone()[0]
conn.close()

print(f"[OK] DB restored from {DUMP_FILE.name}")
print(f"[OK] festivals count: {count}")
