#!/usr/bin/env python3
"""Dump festivals table to SQL for version control (replaces binary DB commits)."""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "nipponexus/data/sqlite/nipponexus.db"
DUMP_PATH = Path.home() / "nipponexus/data/festivals_dump.sql"

conn = sqlite3.connect(DB_PATH)
with open(DUMP_PATH, "w", encoding="utf-8") as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")
conn.close()
print(f"[OK] Dumped to {DUMP_PATH}")
print(f"     size: {DUMP_PATH.stat().st_size:,} bytes")
