#!/usr/bin/env python3
"""次の生成対象10件をAIコンサル提示用に整形出力"""
import sqlite3
import sys
from pathlib import Path

DB = Path("/Users/openclaw_ks/nipponexus/data/sqlite/nipponexus.db")
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 10

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.execute("""
    SELECT qid, label_ja, label_en, description_ja, description_en,
           location_label_ja, location_label_en, prefecture, region,
           latitude, longitude, inception_year, start_month, season,
           image_url, wikipedia_ja, wikipedia_en, priority_score
    FROM festivals
    WHERE status='pending' AND label_ja IS NOT NULL AND label_en IS NOT NULL
    ORDER BY priority_score DESC, qid
    LIMIT ?
""", (LIMIT,))

rows = cur.fetchall()
print(f"=== 生成対象 {len(rows)}件（priority_score降順） ===\n")
for i, r in enumerate(rows, 1):
    print(f"【{i}】 [{r['priority_score']}] {r['qid']}")
    print(f"  日本語名: {r['label_ja']}")
    print(f"  英語名:   {r['label_en']}")
    if r['description_ja']: print(f"  説明(ja): {r['description_ja']}")
    if r['description_en']: print(f"  説明(en): {r['description_en']}")
    if r['location_label_ja']: print(f"  場所: {r['location_label_ja']} / {r['location_label_en'] or ''}")
    if r['prefecture']: print(f"  都道府県: {r['prefecture']} ({r['region']})")
    if r['latitude']: print(f"  座標: {r['latitude']:.4f}, {r['longitude']:.4f}")
    if r['inception_year']: print(f"  起源年: {r['inception_year']}")
    if r['start_month']: print(f"  開催月: {r['start_month']}月 ({r['season']})")
    if r['image_url']: print(f"  画像: {r['image_url']}")
    if r['wikipedia_ja']: print(f"  wiki_ja: {r['wikipedia_ja']}")
    if r['wikipedia_en']: print(f"  wiki_en: {r['wikipedia_en']}")
    print()

# pendingの残数
cur = conn.execute("SELECT COUNT(*) FROM festivals WHERE status='pending' AND label_ja IS NOT NULL AND label_en IS NOT NULL")
print(f"=== pending残: {cur.fetchone()[0]:,}件 ===")
conn.close()
