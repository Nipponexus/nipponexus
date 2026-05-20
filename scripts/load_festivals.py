#!/usr/bin/env python3
"""
Nipponexus: Wikidata raw JSON → SQLite festivals テーブル投入
v1: 日次10件運用対応・優先度スコアリング付き
"""
import json
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
DB_PATH = ROOT / "data" / "sqlite" / "nipponexus.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# 8地方区分マッピング（都道府県名 → 地域）
REGION_MAP = {
    "北海道": "hokkaido",
    "青森県": "tohoku", "岩手県": "tohoku", "宮城県": "tohoku",
    "秋田県": "tohoku", "山形県": "tohoku", "福島県": "tohoku",
    "茨城県": "kanto", "栃木県": "kanto", "群馬県": "kanto",
    "埼玉県": "kanto", "千葉県": "kanto", "東京都": "kanto", "神奈川県": "kanto",
    "新潟県": "chubu", "富山県": "chubu", "石川県": "chubu", "福井県": "chubu",
    "山梨県": "chubu", "長野県": "chubu", "岐阜県": "chubu",
    "静岡県": "chubu", "愛知県": "chubu",
    "三重県": "kinki", "滋賀県": "kinki", "京都府": "kinki",
    "大阪府": "kinki", "兵庫県": "kinki", "奈良県": "kinki", "和歌山県": "kinki",
    "鳥取県": "chugoku", "島根県": "chugoku", "岡山県": "chugoku",
    "広島県": "chugoku", "山口県": "chugoku",
    "徳島県": "shikoku", "香川県": "shikoku", "愛媛県": "shikoku", "高知県": "shikoku",
    "福岡県": "kyushu", "佐賀県": "kyushu", "長崎県": "kyushu", "熊本県": "kyushu",
    "大分県": "kyushu", "宮崎県": "kyushu", "鹿児島県": "kyushu", "沖縄県": "okinawa",
}

PREFECTURES = list(REGION_MAP.keys())

# 月→季節
def month_to_season(month):
    if month is None:
        return None
    try:
        m = int(month)
    except (ValueError, TypeError):
        return None
    if m in (3, 4, 5):
        return "spring"
    if m in (6, 7, 8):
        return "summer"
    if m in (9, 10, 11):
        return "autumn"
    if m in (12, 1, 2):
        return "winter"
    return None


def parse_year(date_str):
    """+1869-01-01T00:00:00Z → 1869"""
    if not date_str:
        return None
    m = re.match(r"^[+-]?(\d{1,4})", date_str)
    return int(m.group(1)) if m else None


def parse_coord(coord_str):
    """Point(135.7681 35.0116) → (lat, lon)"""
    if not coord_str:
        return None, None
    m = re.match(r"Point\(([-\d.]+)\s+([-\d.]+)\)", coord_str)
    if not m:
        return None, None
    lon, lat = float(m.group(1)), float(m.group(2))
    return lat, lon


def detect_prefecture(location_ja):
    """地名文字列から都道府県を推測"""
    if not location_ja:
        return None
    for pref in PREFECTURES:
        if pref in location_ja:
            return pref
    # 「東京都」「大阪府」等の語尾なしマッチ（市名のみ等は除外）
    return None


def calc_priority_score(item):
    """生成キュー優先度: 0〜100"""
    score = 0
    if item.get("label_ja"):    score += 20
    if item.get("label_en"):    score += 25
    if item.get("image"):       score += 20
    if item.get("wikipedia_ja"):score += 15
    if item.get("coord"):       score += 10
    if item.get("desc_ja"):     score += 5
    if item.get("month"):       score += 5
    return score


def init_db(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS festivals (
            qid TEXT PRIMARY KEY,
            label_ja TEXT,
            label_en TEXT,
            description_ja TEXT,
            description_en TEXT,
            location_qid TEXT,
            location_label_ja TEXT,
            location_label_en TEXT,
            prefecture TEXT,
            region TEXT,
            latitude REAL,
            longitude REAL,
            inception_year INTEGER,
            start_month INTEGER,
            season TEXT,
            image_url TEXT,
            wikipedia_ja TEXT,
            wikipedia_en TEXT,
            priority_score INTEGER DEFAULT 0,
            status TEXT DEFAULT 'pending',
            manual_content_ja TEXT,
            manual_content_en TEXT,
            slug_ja TEXT,
            slug_en TEXT,
            published_at TEXT,
            fetched_at TEXT NOT NULL,
            source TEXT NOT NULL DEFAULT 'wikidata'
        );

        CREATE INDEX IF NOT EXISTS idx_prefecture ON festivals(prefecture);
        CREATE INDEX IF NOT EXISTS idx_region ON festivals(region);
        CREATE INDEX IF NOT EXISTS idx_season ON festivals(season);
        CREATE INDEX IF NOT EXISTS idx_status ON festivals(status);
        CREATE INDEX IF NOT EXISTS idx_priority ON festivals(priority_score DESC);

        CREATE TABLE IF NOT EXISTS fetch_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fetched_at TEXT NOT NULL,
            raw_file TEXT NOT NULL,
            unique_qids INTEGER NOT NULL,
            inserted INTEGER NOT NULL,
            updated INTEGER NOT NULL
        );
    """)
    conn.commit()


def aggregate_bindings(bindings):
    """SPARQLの行展開を QIDごとに統合"""
    items = defaultdict(lambda: defaultdict(lambda: None))
    for b in bindings:
        qid = b.get("item", {}).get("value", "").rsplit("/", 1)[-1]
        if not qid:
            continue
        mapping = {
            "itemLabel": "label_ja", "itemLabelEn": "label_en",
            "descJa": "desc_ja", "descEn": "desc_en",
            "location": "location_qid",
            "locationLabel": "location_label_ja",
            "locationLabelEn": "location_label_en",
            "coord": "coord", "inception": "inception",
            "month": "month", "image": "image",
            "wikipediaJa": "wikipedia_ja", "wikipediaEn": "wikipedia_en",
        }
        for src, dst in mapping.items():
            if src in b and not items[qid][dst]:
                items[qid][dst] = b[src]["value"]
    return items


def upsert_item(conn, qid, item, fetched_at):
    label_ja = item.get("label_ja")
    label_en = item.get("label_en")
    desc_ja = item.get("desc_ja")
    desc_en = item.get("desc_en")
    loc_qid_url = item.get("location_qid")
    location_qid = loc_qid_url.rsplit("/", 1)[-1] if loc_qid_url else None
    location_label_ja = item.get("location_label_ja")
    location_label_en = item.get("location_label_en")
    lat, lon = parse_coord(item.get("coord"))
    inception_year = parse_year(item.get("inception"))
    month_str = item.get("month")
    start_month = None
    if month_str:
        m = re.search(r"Q(\d+)$", month_str)
        # Wikidataの月QIDマッピング (Q108=Jan ... 簡易版・正確な対応は別途)
        month_qid_map = {
            "Q108": 1, "Q109": 2, "Q110": 3, "Q118": 4, "Q119": 5, "Q120": 6,
            "Q121": 7, "Q122": 8, "Q123": 9, "Q124": 10, "Q125": 11, "Q126": 12,
        }
        if m and f"Q{m.group(1)}" in month_qid_map:
            start_month = month_qid_map[f"Q{m.group(1)}"]
    season = month_to_season(start_month)
    prefecture = detect_prefecture(location_label_ja) or detect_prefecture(label_ja)
    region = REGION_MAP.get(prefecture) if prefecture else None
    image_url = item.get("image")
    wikipedia_ja = item.get("wikipedia_ja")
    wikipedia_en = item.get("wikipedia_en")
    priority_score = calc_priority_score({
        "label_ja": label_ja, "label_en": label_en, "image": image_url,
        "wikipedia_ja": wikipedia_ja, "coord": item.get("coord"),
        "desc_ja": desc_ja, "month": start_month,
    })

    cur = conn.execute("SELECT qid FROM festivals WHERE qid = ?", (qid,))
    exists = cur.fetchone() is not None

    if exists:
        conn.execute("""
            UPDATE festivals SET
                label_ja=?, label_en=?, description_ja=?, description_en=?,
                location_qid=?, location_label_ja=?, location_label_en=?,
                prefecture=?, region=?, latitude=?, longitude=?,
                inception_year=?, start_month=?, season=?,
                image_url=?, wikipedia_ja=?, wikipedia_en=?,
                priority_score=?, fetched_at=?
            WHERE qid = ?
        """, (label_ja, label_en, desc_ja, desc_en,
              location_qid, location_label_ja, location_label_en,
              prefecture, region, lat, lon,
              inception_year, start_month, season,
              image_url, wikipedia_ja, wikipedia_en,
              priority_score, fetched_at, qid))
        return "updated"
    else:
        conn.execute("""
            INSERT INTO festivals (
                qid, label_ja, label_en, description_ja, description_en,
                location_qid, location_label_ja, location_label_en,
                prefecture, region, latitude, longitude,
                inception_year, start_month, season,
                image_url, wikipedia_ja, wikipedia_en,
                priority_score, status, fetched_at, source
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (qid, label_ja, label_en, desc_ja, desc_en,
              location_qid, location_label_ja, location_label_en,
              prefecture, region, lat, lon,
              inception_year, start_month, season,
              image_url, wikipedia_ja, wikipedia_en,
              priority_score, "pending", fetched_at, "wikidata"))
        return "inserted"


def main():
    raw_files = sorted(RAW_DIR.glob("festivals_wikidata_*.json"))
    if not raw_files:
        print("[ERROR] raw JSON が見つかりません", file=sys.stderr)
        sys.exit(1)
    latest = raw_files[-1]
    print(f"[INFO] 投入対象: {latest.name}")

    data = json.loads(latest.read_text(encoding="utf-8"))
    bindings = data["results"]["bindings"]
    items = aggregate_bindings(bindings)
    print(f"[INFO] ユニーク QID: {len(items)}")

    conn = sqlite3.connect(DB_PATH)
    init_db(conn)

    fetched_at = datetime.now(timezone.utc).isoformat()
    inserted = updated = 0
    for qid, item in items.items():
        result = upsert_item(conn, qid, item, fetched_at)
        if result == "inserted":
            inserted += 1
        else:
            updated += 1

    conn.execute("""
        INSERT INTO fetch_history (fetched_at, raw_file, unique_qids, inserted, updated)
        VALUES (?, ?, ?, ?, ?)
    """, (fetched_at, latest.name, len(items), inserted, updated))
    conn.commit()

    print(f"[INFO] INSERT: {inserted}件 / UPDATE: {updated}件")

    # 検証クエリ
    print("\n=== 投入後の集計 ===")
    cur = conn.execute("SELECT COUNT(*) FROM festivals")
    print(f"  総件数: {cur.fetchone()[0]:,}")

    cur = conn.execute("SELECT COUNT(*) FROM festivals WHERE label_ja IS NOT NULL AND label_en IS NOT NULL")
    print(f"  日英ラベル両方: {cur.fetchone()[0]:,}")

    cur = conn.execute("SELECT COUNT(*) FROM festivals WHERE image_url IS NOT NULL")
    print(f"  画像あり: {cur.fetchone()[0]:,}")

    cur = conn.execute("SELECT COUNT(*) FROM festivals WHERE prefecture IS NOT NULL")
    print(f"  都道府県解決済み: {cur.fetchone()[0]:,}")

    print("\n=== 地域別件数 ===")
    cur = conn.execute("""
        SELECT region, COUNT(*) FROM festivals
        WHERE region IS NOT NULL GROUP BY region ORDER BY COUNT(*) DESC
    """)
    for region, cnt in cur.fetchall():
        print(f"  {region:10s}: {cnt:,}")

    print("\n=== 季節別件数 ===")
    cur = conn.execute("""
        SELECT season, COUNT(*) FROM festivals
        WHERE season IS NOT NULL GROUP BY season ORDER BY COUNT(*) DESC
    """)
    for season, cnt in cur.fetchall():
        print(f"  {season:10s}: {cnt:,}")

    print("\n=== 優先度上位10件（生成キュー先頭） ===")
    cur = conn.execute("""
        SELECT qid, label_ja, label_en, prefecture, priority_score
        FROM festivals ORDER BY priority_score DESC, qid LIMIT 10
    """)
    for row in cur.fetchall():
        qid, ja, en, pref, score = row
        print(f"  [{score}] {qid}: {ja} / {en} ({pref or '?'})")

    conn.close()
    print(f"\n[INFO] SQLite: {DB_PATH}")


if __name__ == "__main__":
    main()
