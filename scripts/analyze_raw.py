#!/usr/bin/env python3
"""raw JSONの品質分析"""
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"

# 最新のraw JSONを読み込む
raw_files = sorted(RAW_DIR.glob("festivals_wikidata_*.json"))
if not raw_files:
    print("[ERROR] raw JSON が見つかりません", file=sys.stderr)
    sys.exit(1)
latest = raw_files[-1]
print(f"[INFO] 分析対象: {latest.name}")

data = json.loads(latest.read_text(encoding="utf-8"))
bindings = data.get("results", {}).get("bindings", [])
print(f"[INFO] 取得行数: {len(bindings):,}")

# QIDごとに統合
items = defaultdict(lambda: {
    "label_ja": None, "label_en": None,
    "desc_ja": None, "desc_en": None,
    "location_ja": None, "location_en": None,
    "coord": None, "inception": None,
    "start_time": None, "end_time": None,
    "point_in_time": None, "month": None,
    "image": None, "wikipedia_ja": None, "wikipedia_en": None,
})

for b in bindings:
    qid = b.get("item", {}).get("value", "").rsplit("/", 1)[-1]
    if not qid:
        continue
    it = items[qid]
    for src, dst in [
        ("itemLabel", "label_ja"), ("itemLabelEn", "label_en"),
        ("descJa", "desc_ja"), ("descEn", "desc_en"),
        ("locationLabel", "location_ja"), ("locationLabelEn", "location_en"),
        ("coord", "coord"), ("inception", "inception"),
        ("startTime", "start_time"), ("endTime", "end_time"),
        ("pointInTime", "point_in_time"), ("month", "month"),
        ("image", "image"), ("wikipediaJa", "wikipedia_ja"),
        ("wikipediaEn", "wikipedia_en"),
    ]:
        if src in b and not it[dst]:
            it[dst] = b[src]["value"]

total = len(items)
print(f"[INFO] ユニーク QID: {total:,}")
print()
print("=== フィールド網羅率 ===")
for field in ["label_ja", "label_en", "desc_ja", "desc_en",
              "location_ja", "location_en", "coord",
              "inception", "start_time", "end_time", "point_in_time", "month",
              "image", "wikipedia_ja", "wikipedia_en"]:
    count = sum(1 for v in items.values() if v[field])
    pct = (count / total * 100) if total else 0
    bar = "█" * int(pct / 5)
    print(f"  {field:20s} {count:5d} / {total} ({pct:5.1f}%) {bar}")

print()
print("=== 日英両方のラベルあり (公開可能件数の上限) ===")
both = sum(1 for v in items.values() if v["label_ja"] and v["label_en"])
print(f"  両方あり: {both:,} / {total:,} ({both/total*100:.1f}%)")

print()
print("=== サンプル: 日英両方のラベル + 画像あり (公開時の優良候補) ===")
candidates = [(qid, v) for qid, v in items.items() 
              if v["label_ja"] and v["label_en"] and v["image"]]
print(f"  該当: {len(candidates):,} 件")
for qid, v in candidates[:10]:
    loc = v["location_ja"] or "場所不明"
    print(f"    {qid}: {v['label_ja']} / {v['label_en']} ({loc})")

print()
print("=== ラベル欠落の例 (Q番号ラベルのみ) ===")
broken = [(qid, v) for qid, v in items.items() 
          if v["label_ja"] and v["label_ja"].startswith("Q") and v["label_ja"][1:].isdigit()]
print(f"  ラベルがQID自身になっている件数（日本語ラベル未設定）: {len(broken):,}")
