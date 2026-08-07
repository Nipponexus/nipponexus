#!/usr/bin/env python3
"""
日次10件本文貼付スクリプト雛形
使い方: 私(AIコンサル)が ITEMS辞書を10件分埋めた完成版を提示する。
ユーザーは bash上で 'python3 -' に貼付するだけ。
"""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path("/Users/openclaw_ks/nipponexus/data/sqlite/nipponexus.db")

# === ここから AIコンサルが毎日10件分埋める ===
ITEMS = {
    # "Q1234567": {
    #     "slug_ja": "saga-international-balloon-fiesta",
    #     "slug_en": "saga-international-balloon-fiesta",
    #     "content_ja": """## 概要
    # ...日本語本文(マークダウン or HTML断片)...
    # """,
    #     "content_en": """## Overview
    # ...English content...
    # """,
    # },
}
# === ここまで ===

if not ITEMS:
    print("[ERROR] ITEMS が空です。AIコンサル提示版を貼り直してください。")
    raise SystemExit(1)

conn = sqlite3.connect(DB)
now = datetime.now(timezone.utc).isoformat()
updated = 0
missing = []
for qid, data in ITEMS.items():
    cur = conn.execute("SELECT qid, status FROM festivals WHERE qid=?", (qid,))
    row = cur.fetchone()
    if not row:
        missing.append(qid)
        continue
    # NXPREF_v1 (2026-08-07): 県名整合ガード
    import nxpref as _nxp
    _nxp.assert_ok(conn, qid)
    conn.execute("""
        UPDATE festivals
        SET manual_content_ja=?, manual_content_en=?,
            slug_ja=?, slug_en=?,
            status='drafted', published_at=NULL
        WHERE qid=?
    """, (data["content_ja"], data["content_en"],
          data["slug_ja"], data["slug_en"], qid))
    updated += 1

conn.commit()

# 検証
print(f"[OK] {updated}件 を status='drafted' に更新")
if missing:
    print(f"[WARN] DBに存在しないQID: {missing}")

cur = conn.execute("SELECT COUNT(*) FROM festivals WHERE status='drafted'")
print(f"[INFO] drafted合計: {cur.fetchone()[0]:,}件")
cur = conn.execute("SELECT COUNT(*) FROM festivals WHERE status='pending' AND label_ja IS NOT NULL AND label_en IS NOT NULL")
print(f"[INFO] pending残: {cur.fetchone()[0]:,}件")
conn.close()
