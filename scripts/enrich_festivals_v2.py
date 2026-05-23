#!/usr/bin/env python3
"""
Nipponexus: enrich v2 - description_ja 解析 + 神社/寺辞書追加
v1で残ったNULL分を狙い撃ち補完
"""
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "sqlite" / "nipponexus.db"

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

# 神社/寺/施設名辞書（location_label_ja の典型パターン）
SHRINE_TEMPLE_TO_PREF = {
    # 三重
    "伊勢神宮": "三重県", "多度大社": "三重県", "津島神社": "三重県",
    "斎宮跡": "三重県", "椿大神社": "三重県",
    # 大阪
    "住吉大社": "大阪府", "天王寺": "大阪府", "四天王寺": "大阪府",
    "大阪城": "大阪府", "通天閣": "大阪府",
    # 奈良
    "東大寺": "奈良県", "春日大社": "奈良県", "興福寺": "奈良県",
    "薬師寺": "奈良県", "唐招提寺": "奈良県", "奈良公園": "奈良県",
    "大神神社": "奈良県", "石上神宮": "奈良県",
    # 京都
    "伏見稲荷": "京都府", "清水寺": "京都府", "金閣寺": "京都府",
    "銀閣寺": "京都府", "平安神宮": "京都府", "下鴨神社": "京都府",
    "上賀茂神社": "京都府", "八坂神社": "京都府", "北野天満宮": "京都府",
    "東寺": "京都府", "嵐山": "京都府",
    # 東京
    "明治神宮": "東京都", "靖国神社": "東京都", "浅草寺": "東京都",
    "増上寺": "東京都", "築地": "東京都", "両国": "東京都",
    "富岡八幡宮": "東京都", "大國魂神社": "東京都", "神田明神": "東京都",
    "湯島天神": "東京都", "日枝神社": "東京都", "亀戸天神": "東京都",
    "隅田川": "東京都", "お台場": "東京都", "八王子": "東京都",
    "板橋区": "東京都", "練馬区": "東京都", "杉並区": "東京都",
    "世田谷": "東京都", "中野区": "東京都", "豊島区": "東京都",
    "文京区": "東京都", "千代田": "東京都", "中央区": "東京都",
    "港区": "東京都", "台東": "東京都", "荒川区": "東京都",
    "北区": "東京都", "板橋": "東京都", "練馬": "東京都",
    # 神奈川
    "鶴岡八幡宮": "神奈川県", "江ノ島": "神奈川県", "横浜中華街": "神奈川県",
    # 千葉
    "成田山": "千葉県", "成田": "千葉県", "香取神宮": "千葉県",
    # 長野
    "諏訪大社": "長野県", "善光寺": "長野県", "戸隠神社": "長野県",
    # 山梨
    "富士山": "山梨県",  # 山梨/静岡境界だが優先
    "富士急": "山梨県", "山中湖": "山梨県", "河口湖": "山梨県",
    # 静岡
    "三嶋大社": "静岡県", "熱海": "静岡県", "伊豆": "静岡県",
    # 愛知
    "熱田神宮": "愛知県", "豊川稲荷": "愛知県", "犬山城": "愛知県",
    "田縣神社": "愛知県", "大縣神社": "愛知県",
    # 岐阜
    "白川郷": "岐阜県", "下呂温泉": "岐阜県",
    # 石川
    "金剱宮": "石川県", "兼六園": "石川県", "千里浜": "石川県",
    # 富山
    "雄山神社": "富山県", "立山": "富山県",
    # 福井
    "永平寺": "福井県", "気比神宮": "福井県", "東尋坊": "福井県",
    "武生中央公園": "福井県",
    # 兵庫
    "湊川神社": "兵庫県", "西宮神社": "兵庫県", "生田神社": "兵庫県",
    "姫路城": "兵庫県", "甲子園": "兵庫県", "六甲": "兵庫県",
    "有馬温泉": "兵庫県",
    # 和歌山
    "熊野那智大社": "和歌山県", "熊野本宮大社": "和歌山県",
    "熊野速玉大社": "和歌山県", "高野山": "和歌山県",
    # 広島
    "厳島神社": "広島県", "原爆ドーム": "広島県", "宮島": "広島県",
    # 島根
    "出雲大社": "島根県", "松江城": "島根県",
    # 山口
    "防府天満宮": "山口県", "錦帯橋": "山口県", "秋吉台": "山口県",
    # 福岡
    "太宰府天満宮": "福岡県", "宗像大社": "福岡県", "筥崎宮": "福岡県",
    "玄界灘": "福岡県",  # 福岡/長崎境界・福岡優先
    "中洲": "福岡県", "天神": "福岡県",
    # 佐賀
    "祐徳稲荷神社": "佐賀県", "唐津神社": "佐賀県",
    # 長崎
    "諏訪神社": "長崎県",  # 長崎の有名な諏訪神社・要注意
    "出島": "長崎県", "ハウステンボス": "長崎県", "グラバー園": "長崎県",
    # 熊本
    "阿蘇神社": "熊本県", "熊本城": "熊本県",
    # 大分
    "宇佐神宮": "大分県", "湯布院": "大分県",
    # 宮崎
    "高千穂神社": "宮崎県", "鵜戸神宮": "宮崎県",
    # 鹿児島
    "霧島神宮": "鹿児島県", "桜島": "鹿児島県", "天文館": "鹿児島県",
    "屋久島": "鹿児島県",
    # 沖縄
    "首里城": "沖縄県", "沖縄本島": "沖縄県", "美ら海": "沖縄県",
    # 秋田
    "土崎神明社": "秋田県", "千秋公園": "秋田県", "なまはげ館": "秋田県",
    # 青森
    "三内丸山": "青森県", "十和田": "青森県", "奥入瀬": "青森県",
    # 岩手
    "中尊寺": "岩手県", "毛越寺": "岩手県", "平泉": "岩手県",
    # 宮城
    "塩竈神社": "宮城県", "瑞鳳殿": "宮城県", "松島": "宮城県",
    # 山形
    "山寺": "山形県", "立石寺": "山形県", "蔵王": "山形県",
    "出羽三山": "山形県", "羽黒山": "山形県",
    # 福島
    "鶴ヶ城": "福島県", "磐梯山": "福島県",
    # 北海道
    "札幌大通": "北海道", "大通公園": "北海道", "すすきの": "北海道",
    "ニセコ": "北海道", "知床": "北海道",
    # 茨城
    "鹿島神宮": "茨城県", "筑波山": "茨城県", "偕楽園": "茨城県",
    # 栃木
    "日光東照宮": "栃木県", "華厳の滝": "栃木県", "中禅寺湖": "栃木県",
    # 群馬
    "草津温泉": "群馬県", "伊香保": "群馬県", "榛名": "群馬県",
    # 埼玉
    "氷川神社": "埼玉県",  # さいたまの氷川神社（東京の氷川と区別注意）
    # 高知
    "桂浜": "高知県", "はりまや橋": "高知県",
    # 愛媛
    "道後温泉": "愛媛県", "松山城": "愛媛県", "石鎚山": "愛媛県",
    # 香川
    "金刀比羅宮": "香川県", "栗林公園": "香川県",
    # 徳島
    "大塚国際美術館": "徳島県",
    # 岡山
    "後楽園": "岡山県", "倉敷美観": "岡山県",
    # 鳥取
    "鳥取砂丘": "鳥取県", "大山": "鳥取県",
    # 新潟
    "弥彦神社": "新潟県", "佐渡": "新潟県", "苗場": "新潟県",
}

# 漢数字→数字
KANSUJI = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6,
           "七": 7, "八": 8, "九": 9, "十": 10, "十一": 11, "十二": 12}


def month_to_season(month):
    if month is None:
        return None
    try:
        m = int(month)
    except (ValueError, TypeError):
        return None
    if m in (3, 4, 5): return "spring"
    if m in (6, 7, 8): return "summer"
    if m in (9, 10, 11): return "autumn"
    if m in (12, 1, 2): return "winter"
    return None


def extract_prefecture_from_desc(desc):
    """description_ja から都道府県名を抽出"""
    if not desc:
        return None
    for pref in PREFECTURES:
        if pref in desc:
            return pref
    return None


def extract_prefecture_from_shrine(text):
    """神社/寺/施設辞書マッチ"""
    if not text:
        return None
    for key in sorted(SHRINE_TEMPLE_TO_PREF.keys(), key=len, reverse=True):
        if key in text:
            return SHRINE_TEMPLE_TO_PREF[key]
    return None


def extract_month_from_desc(desc):
    """description_ja から月（1-12）を抽出"""
    if not desc:
        return None
    # 歴史事象除外：年号がある場合はスキップ
    if re.search(r"(慶応|明治|大正|昭和)\s*\d+年", desc):
        # ただし「毎年○月」のようなパターンがあれば月だけ採用
        m = re.search(r"毎年\s*(\d{1,2})月", desc)
        if m:
            return int(m.group(1))
        return None

    # パターン1: 「毎年○月」「○月○日」
    m = re.search(r"(\d{1,2})月", desc)
    if m:
        month = int(m.group(1))
        if 1 <= month <= 12:
            return month

    # パターン2: 漢数字「二月」「十二月」等
    m = re.search(r"([一二三四五六七八九十]{1,3})月", desc)
    if m:
        kan = m.group(1)
        if kan in KANSUJI:
            month = KANSUJI[kan]
            if 1 <= month <= 12:
                return month

    return None


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT qid, label_ja, location_label_ja, description_ja,
               start_month, prefecture, region, season
        FROM festivals
    """)
    rows = cur.fetchall()

    stats = {
        "total": len(rows),
        "pref_already": 0, "pref_filled_v2": 0, "pref_still_null": 0,
        "season_already": 0, "season_filled_v2": 0, "season_still_null": 0,
        "pref_from_desc": 0, "pref_from_shrine": 0,
        "season_from_desc_month": 0,
    }

    updates = []
    for row in rows:
        qid, label_ja, loc_ja, desc_ja, start_month, cur_pref, cur_region, cur_season = row

        new_pref = cur_pref
        new_region = cur_region
        new_season = cur_season

        # prefecture v2 補完
        if cur_pref and cur_pref.strip():
            stats["pref_already"] += 1
        else:
            # L4: description_ja から都道府県抽出
            pref = extract_prefecture_from_desc(desc_ja)
            method = "desc" if pref else None
            # L5: 神社/寺/施設辞書（location → label の順）
            if not pref:
                for text in (loc_ja, label_ja):
                    pref = extract_prefecture_from_shrine(text)
                    if pref:
                        method = "shrine"
                        break
            if pref:
                new_pref = pref
                new_region = REGION_MAP.get(pref)
                stats["pref_filled_v2"] += 1
                if method == "desc": stats["pref_from_desc"] += 1
                elif method == "shrine": stats["pref_from_shrine"] += 1
            else:
                stats["pref_still_null"] += 1

        # season v2 補完
        if cur_season and cur_season.strip():
            stats["season_already"] += 1
        else:
            # L4: description_ja から月抽出
            month = extract_month_from_desc(desc_ja)
            season = month_to_season(month)
            if season:
                new_season = season
                stats["season_filled_v2"] += 1
                stats["season_from_desc_month"] += 1
            else:
                stats["season_still_null"] += 1

        if (new_pref, new_region, new_season) != (cur_pref, cur_region, cur_season):
            updates.append((new_pref, new_region, new_season, qid))

    cur.executemany("""
        UPDATE festivals SET prefecture=?, region=?, season=? WHERE qid=?
    """, updates)
    conn.commit()

    print(f"=== enrich_festivals_v2.py 実行結果 ===")
    print(f"総件数: {stats['total']:,}")
    print(f"")
    print(f"[prefecture v2]")
    print(f"  既存（v1+生）: {stats['pref_already']:,}")
    print(f"  新規補完(v2): {stats['pref_filled_v2']:,}")
    print(f"    description_ja:    {stats['pref_from_desc']:,}")
    print(f"    神社/寺/施設辞書:  {stats['pref_from_shrine']:,}")
    print(f"  残NULL: {stats['pref_still_null']:,}")
    print(f"")
    print(f"[season v2]")
    print(f"  既存（v1+生）: {stats['season_already']:,}")
    print(f"  新規補完(v2): {stats['season_filled_v2']:,}")
    print(f"    desc から月抽出: {stats['season_from_desc_month']:,}")
    print(f"  残NULL: {stats['season_still_null']:,}")
    print(f"")
    print(f"UPDATE実行: {len(updates):,}件")

    # 補完後の最終カバレッジ
    print(f"\n=== 最終カバレッジ ===")
    cur.execute("SELECT COUNT(*) FROM festivals")
    total = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM festivals WHERE prefecture IS NOT NULL AND prefecture != ''")
    p = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM festivals WHERE season IS NOT NULL AND season != ''")
    s = cur.fetchone()[0]
    print(f"  prefecture: {p:,} / {total:,} ({p*100/total:.1f}%)")
    print(f"  season:     {s:,} / {total:,} ({s*100/total:.1f}%)")

    print(f"\n=== 都道府県別件数（全表示） ===")
    cur.execute("""
        SELECT prefecture, COUNT(*) FROM festivals
        WHERE prefecture IS NOT NULL AND prefecture != ''
        GROUP BY prefecture ORDER BY COUNT(*) DESC
    """)
    for pref, cnt in cur.fetchall():
        print(f"  {pref:8s}: {cnt:,}")

    print(f"\n=== 季節別件数 ===")
    cur.execute("""
        SELECT season, COUNT(*) FROM festivals
        WHERE season IS NOT NULL AND season != ''
        GROUP BY season ORDER BY COUNT(*) DESC
    """)
    for season, cnt in cur.fetchall():
        print(f"  {season:8s}: {cnt:,}")

    conn.close()


if __name__ == "__main__":
    main()
