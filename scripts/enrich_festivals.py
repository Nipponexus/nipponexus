#!/usr/bin/env python3
"""
Nipponexus: festivals テーブルの prefecture/region/season を事後補完
- 既存値がNULL/空の行のみ更新（idempotent）
- 3層検出: 直接マッチ → 辞書マッチ → 座標/キーワード推定
"""
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "sqlite" / "nipponexus.db"

# 47都道府県 → 8地方区分
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

# L2辞書: 市区町村・著名地名 → 都道府県
CITY_TO_PREF = {
    # 政令指定都市・県庁所在地
    "札幌": "北海道", "函館": "北海道", "旭川": "北海道", "釧路": "北海道", "小樽": "北海道", "帯広": "北海道",
    "青森市": "青森県", "弘前": "青森県", "八戸": "青森県", "五所川原": "青森県",
    "盛岡": "岩手県", "花巻": "岩手県", "一関": "岩手県", "釜石": "岩手県",
    "仙台": "宮城県", "石巻": "宮城県", "気仙沼": "宮城県",
    "秋田市": "秋田県", "大館": "秋田県", "横手": "秋田県", "大仙": "秋田県", "湯沢": "秋田県", "男鹿": "秋田県", "角館": "秋田県",
    "山形市": "山形県", "米沢": "山形県", "鶴岡": "山形県", "酒田": "山形県", "新庄": "山形県",
    "福島市": "福島県", "郡山": "福島県", "いわき": "福島県", "会津若松": "福島県", "白河": "福島県", "相馬": "福島県",
    "水戸": "茨城県", "つくば": "茨城県", "日立": "茨城県", "ひたちなか": "茨城県", "鹿嶋": "茨城県",
    "宇都宮": "栃木県", "日光": "栃木県", "鹿沼": "栃木県", "足利": "栃木県",
    "前橋": "群馬県", "高崎": "群馬県", "桐生": "群馬県", "伊勢崎": "群馬県", "太田": "群馬県",
    "さいたま": "埼玉県", "川越": "埼玉県", "川口": "埼玉県", "所沢": "埼玉県", "秩父": "埼玉県", "熊谷": "埼玉県",
    "千葉市": "千葉県", "船橋": "千葉県", "成田": "千葉県", "館山": "千葉県", "佐倉": "千葉県", "勝浦": "千葉県",
    "横浜": "神奈川県", "川崎": "神奈川県", "鎌倉": "神奈川県", "藤沢": "神奈川県", "小田原": "神奈川県", "箱根": "神奈川県",
    "新潟市": "新潟県", "長岡": "新潟県", "上越": "新潟県", "佐渡": "新潟県", "苗場": "新潟県",
    "富山市": "富山県", "高岡": "富山県", "魚津": "富山県", "南砺": "富山県", "氷見": "富山県",
    "金沢": "石川県", "輪島": "石川県", "七尾": "石川県", "白山": "石川県", "加賀": "石川県",
    "福井市": "福井県", "敦賀": "福井県", "鯖江": "福井県", "越前": "福井県",
    "甲府": "山梨県", "富士吉田": "山梨県", "山中湖": "山梨県", "河口湖": "山梨県",
    "長野市": "長野県", "松本": "長野県", "上田": "長野県", "諏訪": "長野県", "軽井沢": "長野県", "飯田": "長野県",
    "岐阜市": "岐阜県", "高山": "岐阜県", "大垣": "岐阜県", "下呂": "岐阜県", "郡上": "岐阜県", "多治見": "岐阜県",
    "静岡市": "静岡県", "浜松": "静岡県", "沼津": "静岡県", "熱海": "静岡県", "伊豆": "静岡県", "富士宮": "静岡県",
    "名古屋": "愛知県", "豊田": "愛知県", "岡崎": "愛知県", "豊橋": "愛知県", "一宮": "愛知県", "犬山": "愛知県",
    "津市": "三重県", "四日市": "三重県", "伊勢": "三重県", "鈴鹿": "三重県", "松阪": "三重県", "鳥羽": "三重県",
    "大津": "滋賀県", "彦根": "滋賀県", "長浜": "滋賀県", "近江": "滋賀県",
    "京都市": "京都府", "宇治": "京都府", "舞鶴": "京都府", "亀岡": "京都府", "天橋立": "京都府",
    "大阪市": "大阪府", "堺": "大阪府", "東大阪": "大阪府", "枚方": "大阪府", "岸和田": "大阪府", "豊中": "大阪府",
    "神戸": "兵庫県", "姫路": "兵庫県", "西宮": "兵庫県", "尼崎": "兵庫県", "明石": "兵庫県", "宝塚": "兵庫県", "淡路": "兵庫県",
    "奈良市": "奈良県", "橿原": "奈良県", "生駒": "奈良県", "桜井": "奈良県", "吉野": "奈良県",
    "和歌山市": "和歌山県", "田辺": "和歌山県", "新宮": "和歌山県", "高野": "和歌山県", "白浜": "和歌山県",
    "鳥取市": "鳥取県", "米子": "鳥取県", "倉吉": "鳥取県", "境港": "鳥取県",
    "松江": "島根県", "出雲": "島根県", "浜田": "島根県", "益田": "島根県",
    "岡山市": "岡山県", "倉敷": "岡山県", "津山": "岡山県",
    "広島市": "広島県", "福山": "広島県", "尾道": "広島県", "呉": "広島県", "宮島": "広島県",
    "山口市": "山口県", "下関": "山口県", "宇部": "山口県", "萩": "山口県", "岩国": "山口県",
    "徳島市": "徳島県", "鳴門": "徳島県", "阿波": "徳島県",
    "高松": "香川県", "丸亀": "香川県", "坂出": "香川県",
    "松山": "愛媛県", "今治": "愛媛県", "新居浜": "愛媛県", "宇和島": "愛媛県",
    "高知市": "高知県", "南国": "高知県", "四万十": "高知県",
    "福岡市": "福岡県", "北九州": "福岡県", "博多": "福岡県", "久留米": "福岡県", "太宰府": "福岡県", "筑後": "福岡県",
    "佐賀市": "佐賀県", "唐津": "佐賀県", "鳥栖": "佐賀県", "伊万里": "佐賀県", "有田": "佐賀県",
    "長崎市": "長崎県", "佐世保": "長崎県", "島原": "長崎県", "雲仙": "長崎県", "平戸": "長崎県",
    "熊本市": "熊本県", "天草": "熊本県", "阿蘇": "熊本県", "人吉": "熊本県", "山鹿": "熊本県",
    "大分市": "大分県", "別府": "大分県", "由布": "大分県", "中津": "大分県", "日田": "大分県",
    "宮崎市": "宮崎県", "都城": "宮崎県", "日南": "宮崎県", "高千穂": "宮崎県",
    "鹿児島市": "鹿児島県", "霧島": "鹿児島県", "指宿": "鹿児島県", "薩摩": "鹿児島県", "奄美": "鹿児島県",
    "那覇": "沖縄県", "石垣": "沖縄県", "宮古島": "沖縄県", "沖縄市": "沖縄県", "うるま": "沖縄県",
    # 東京区
    "新宿": "東京都", "渋谷": "東京都", "浅草": "東京都", "上野": "東京都", "銀座": "東京都",
    "秋葉原": "東京都", "六本木": "東京都", "池袋": "東京都", "東京": "東京都", "墨田": "東京都",
    "足立": "東京都", "葛飾": "東京都", "江戸川": "東京都", "品川": "東京都", "目黒": "東京都",
    "国際展示場": "東京都", "東京ビッグサイト": "東京都",
}

# 著名祭り名から都道府県（label_ja マッチ用）
FESTIVAL_TO_PREF = {
    "青森ねぶた": "青森県", "弘前ねぷた": "青森県", "五所川原立佞武多": "青森県",
    "盛岡さんさ": "岩手県", "チャグチャグ馬コ": "岩手県",
    "仙台七夕": "宮城県", "塩竈みなと": "宮城県",
    "竿燈": "秋田県", "かまくら": "秋田県", "なまはげ": "秋田県",
    "山形花笠": "山形県", "新庄まつり": "山形県",
    "相馬野馬追": "福島県", "わらじまつり": "福島県",
    "祇園祭": "京都府", "葵祭": "京都府", "時代祭": "京都府", "鞍馬の火祭": "京都府",
    "天神祭": "大阪府", "岸和田だんじり": "大阪府", "住吉": "大阪府",
    "灘のけんか": "兵庫県", "ルミナリエ": "兵庫県",
    "博多祇園山笠": "福岡県", "博多どんたく": "福岡県", "おくんち": "長崎県",
    "唐津くんち": "佐賀県", "佐賀インターナショナルバルーン": "佐賀県",
    "阿波おどり": "徳島県", "よさこい": "高知県",
    "ねぶた": "青森県", "ねぷた": "青森県",
    "高山祭": "岐阜県", "古川祭": "岐阜県", "郡上おどり": "岐阜県",
    "おわら風の盆": "富山県", "高岡御車山": "富山県",
    "金沢百万石": "石川県", "輪島大祭": "石川県",
    "ござれ": "高知県", "土佐の": "高知県",
    "秩父夜祭": "埼玉県", "川越まつり": "埼玉県",
    "成田祇園": "千葉県",
    "三社祭": "東京都", "神田祭": "東京都", "山王祭": "東京都", "深川八幡": "東京都",
    "葉山": "神奈川県", "湘南": "神奈川県",
    "長岡まつり": "新潟県", "新潟まつり": "新潟県",
    "御柱祭": "長野県", "諏訪大社": "長野県", "善光寺": "長野県",
    "甲府": "山梨県", "信玄公": "山梨県", "吉田の火祭": "山梨県",
    "おやま夏まつり": "栃木県", "東照宮": "栃木県",
    "やぶさめ": "神奈川県",
    "西大寺はだか": "岡山県",
    "厳島": "広島県", "とうかさん": "広島県",
    "おわら": "富山県",
    "下呂": "岐阜県",
    "送り盆": "秋田県", "湯沢": "秋田県",
}

# season L2: label_ja キーワード → 季節
SEASON_KEYWORDS = {
    # winter
    "雪まつり": "winter", "雪祭り": "winter", "かまくら": "winter", "氷祭": "winter",
    "裸祭": "winter", "はだか祭": "winter", "節分": "winter", "初詣": "winter",
    "どんど焼き": "winter", "正月": "winter",
    # spring
    "桜まつり": "spring", "花見": "spring", "春祭": "spring", "雛祭": "spring",
    "ひな祭": "spring", "葵祭": "spring", "曳山": "spring",
    # summer
    "ねぶた": "summer", "ねぷた": "summer", "七夕": "summer", "花火": "summer",
    "夏祭": "summer", "祇園祭": "summer", "天神祭": "summer", "山笠": "summer",
    "灯籠": "summer", "盆踊": "summer", "送り盆": "summer", "竿燈": "summer",
    "風鈴": "summer", "海": "summer",
    # autumn
    "紅葉": "autumn", "もみじ": "autumn", "月見": "autumn", "秋祭": "autumn",
    "くんち": "autumn", "時代祭": "autumn", "だんじり": "autumn", "おくんち": "autumn",
    "新嘗祭": "autumn",
}

# 確実な祭り→季節ハードコード（L3）
FESTIVAL_TO_SEASON = {
    "佐賀インターナショナルバルーンフェスタ": "autumn",
    "東京国際映画祭": "autumn",
    "コミックマーケット": "summer",  # 夏コミ主体
    "ぐず焼き祭り": "summer",
    "大館アメッコ市": "winter",
    "ゲームマーケット": "autumn",
    "下呂の田の神祭": "winter",
    "住吉の御田植": "summer",
    "送り盆まつり": "summer",
    "吉田の火祭": "summer",
    "さっぽろ雪まつり": "winter",
    "青森ねぶた": "summer",
    "仙台七夕": "summer",
    "祇園祭": "summer",
    "葵祭": "spring",
    "時代祭": "autumn",
    "博多祇園山笠": "summer",
    "長崎くんち": "autumn",
    "唐津くんち": "autumn",
    "阿波おどり": "summer",
    "よさこい祭り": "summer",
    "竿燈": "summer",
    "神戸ルミナリエ": "winter",
    "フジロックフェスティバル": "summer",
    "天神祭": "summer",
}


def month_to_season(month):
    if month is None:
        return None
    m = int(month)
    if m in (3, 4, 5): return "spring"
    if m in (6, 7, 8): return "summer"
    if m in (9, 10, 11): return "autumn"
    if m in (12, 1, 2): return "winter"
    return None


def detect_prefecture_l1(text):
    """L1: 都道府県名フル直接マッチ"""
    if not text:
        return None
    for pref in PREFECTURES:
        if pref in text:
            return pref
    # 略称（県/府/都を外した形）も後方一致で確認
    short_map = {
        "東京": "東京都", "京都": "京都府", "大阪": "大阪府", "北海道": "北海道",
    }
    for short, full in short_map.items():
        if short in text:
            return full
    return None


def detect_prefecture_l2(text):
    """L2: 市区町村・地名辞書マッチ"""
    if not text:
        return None
    # 長い地名から優先マッチ（札幌市 > 札幌）
    for city in sorted(CITY_TO_PREF.keys(), key=len, reverse=True):
        if city in text:
            return CITY_TO_PREF[city]
    return None


def detect_prefecture_from_festival(label_ja):
    """祭り名から推定（label_ja用）"""
    if not label_ja:
        return None
    for fest_key, pref in FESTIVAL_TO_PREF.items():
        if fest_key in label_ja:
            return pref
    return None


# 47都道府県の簡易バウンディングボックス (min_lat, max_lat, min_lon, max_lon)
# 重複領域では優先度順に判定
PREF_BBOX = [
    ("沖縄県", 24.0, 27.9, 122.9, 131.4),
    ("北海道", 41.3, 45.6, 139.3, 148.9),
    ("青森県", 40.2, 41.6, 139.5, 141.7),
    ("秋田県", 38.8, 40.5, 139.7, 141.0),
    ("岩手県", 38.8, 40.5, 140.6, 142.1),
    ("山形県", 37.7, 39.2, 139.5, 140.7),
    ("宮城県", 37.7, 39.0, 140.3, 141.7),
    ("福島県", 36.8, 38.0, 139.2, 141.1),
    ("新潟県", 36.7, 38.6, 137.6, 139.9),
    ("栃木県", 36.2, 37.2, 139.3, 140.3),
    ("茨城県", 35.7, 36.9, 139.7, 140.9),
    ("群馬県", 35.9, 37.1, 138.4, 139.7),
    ("千葉県", 34.9, 36.1, 139.7, 140.9),
    ("埼玉県", 35.7, 36.3, 138.7, 139.9),
    ("東京都", 24.2, 35.9, 136.0, 142.3),  # 小笠原含む広域
    ("神奈川県", 35.1, 35.7, 138.9, 139.8),
    ("山梨県", 35.1, 35.9, 138.2, 139.2),
    ("長野県", 35.2, 37.0, 137.3, 138.8),
    ("静岡県", 34.6, 35.7, 137.4, 139.2),
    ("愛知県", 34.5, 35.5, 136.6, 137.8),
    ("岐阜県", 35.1, 36.5, 136.3, 137.7),
    ("富山県", 36.3, 36.9, 136.7, 137.8),
    ("石川県", 36.0, 37.6, 136.2, 137.4),
    ("福井県", 35.3, 36.3, 135.4, 136.8),
    ("三重県", 33.7, 35.3, 135.8, 136.9),
    ("滋賀県", 34.8, 35.7, 135.8, 136.5),
    ("京都府", 34.7, 35.8, 134.8, 136.0),
    ("大阪府", 34.2, 35.0, 135.1, 135.8),
    ("奈良県", 33.8, 34.8, 135.6, 136.2),
    ("和歌山県", 33.4, 34.4, 135.0, 136.0),
    ("兵庫県", 34.1, 35.7, 134.2, 135.5),
    ("鳥取県", 35.1, 35.6, 133.1, 134.5),
    ("岡山県", 34.4, 35.4, 133.3, 134.4),
    ("島根県", 34.3, 35.6, 131.6, 133.4),
    ("広島県", 34.0, 35.1, 132.0, 133.5),
    ("山口県", 33.7, 34.8, 130.7, 132.4),
    ("香川県", 34.1, 34.6, 133.4, 134.5),
    ("徳島県", 33.5, 34.3, 133.6, 134.8),
    ("愛媛県", 32.9, 34.3, 132.0, 133.7),
    ("高知県", 32.7, 33.9, 132.4, 134.3),
    ("福岡県", 33.0, 34.0, 130.0, 131.2),
    ("佐賀県", 33.0, 33.6, 129.7, 130.5),
    ("長崎県", 32.5, 34.7, 128.6, 130.4),
    ("熊本県", 32.1, 33.3, 129.9, 131.2),
    ("大分県", 32.7, 33.7, 130.7, 132.1),
    ("宮崎県", 31.3, 32.8, 130.7, 131.9),
    ("鹿児島県", 27.0, 32.2, 128.4, 131.2),
]


def detect_prefecture_l3_coord(lat, lon):
    """L3: 座標→都道府県逆引き"""
    if lat is None or lon is None:
        return None
    candidates = []
    for pref, min_lat, max_lat, min_lon, max_lon in PREF_BBOX:
        if min_lat <= lat <= max_lat and min_lon <= lon <= max_lon:
            candidates.append(pref)
    if not candidates:
        return None
    # 複数候補の場合：東京都は広域なので優先度を下げる
    if len(candidates) == 1:
        return candidates[0]
    non_tokyo = [c for c in candidates if c != "東京都"]
    return non_tokyo[0] if non_tokyo else candidates[0]


def detect_season(label_ja, start_month, qid=None):
    """3層 season 検出"""
    # L1: start_month
    s = month_to_season(start_month)
    if s:
        return s, "L1_month"
    if not label_ja:
        return None, None
    # L3: ハードコード辞書（優先度高・確実）
    for fest, season in FESTIVAL_TO_SEASON.items():
        if fest in label_ja:
            return season, "L3_hardcoded"
    # L2: キーワード
    # 長いキーワードから優先マッチ
    for keyword in sorted(SEASON_KEYWORDS.keys(), key=len, reverse=True):
        if keyword in label_ja:
            return SEASON_KEYWORDS[keyword], "L2_keyword"
    return None, None


def detect_prefecture(label_ja, location_label_ja, lat, lon):
    """3層 prefecture 検出"""
    # L1: 都道府県名フルマッチ（location 優先 → label）
    for text in (location_label_ja, label_ja):
        pref = detect_prefecture_l1(text)
        if pref:
            return pref, "L1_full"
    # L2a: 祭り名辞書（label_ja のみ）
    pref = detect_prefecture_from_festival(label_ja)
    if pref:
        return pref, "L2_festival"
    # L2b: 市区町村辞書
    for text in (location_label_ja, label_ja):
        pref = detect_prefecture_l2(text)
        if pref:
            return pref, "L2_city"
    # L3: 座標逆引き
    pref = detect_prefecture_l3_coord(lat, lon)
    if pref:
        return pref, "L3_coord"
    return None, None


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 補完対象を取得
    cur.execute("""
        SELECT qid, label_ja, location_label_ja, latitude, longitude,
               start_month, prefecture, region, season
        FROM festivals
    """)
    rows = cur.fetchall()

    stats = {
        "total": len(rows),
        "pref_already": 0, "pref_filled": 0, "pref_still_null": 0,
        "season_already": 0, "season_filled": 0, "season_still_null": 0,
        "pref_l1": 0, "pref_l2_fest": 0, "pref_l2_city": 0, "pref_l3_coord": 0,
        "season_l1": 0, "season_l2": 0, "season_l3": 0,
    }

    updates = []
    for row in rows:
        qid, label_ja, loc_ja, lat, lon, start_month, cur_pref, cur_region, cur_season = row

        new_pref = cur_pref
        new_region = cur_region
        new_season = cur_season

        # prefecture 補完
        if cur_pref and cur_pref.strip():
            stats["pref_already"] += 1
        else:
            pref, method = detect_prefecture(label_ja, loc_ja, lat, lon)
            if pref:
                new_pref = pref
                new_region = REGION_MAP.get(pref)
                stats["pref_filled"] += 1
                if method == "L1_full": stats["pref_l1"] += 1
                elif method == "L2_festival": stats["pref_l2_fest"] += 1
                elif method == "L2_city": stats["pref_l2_city"] += 1
                elif method == "L3_coord": stats["pref_l3_coord"] += 1
            else:
                stats["pref_still_null"] += 1

        # season 補完
        if cur_season and cur_season.strip():
            stats["season_already"] += 1
        else:
            season, method = detect_season(label_ja, start_month, qid)
            if season:
                new_season = season
                stats["season_filled"] += 1
                if method == "L1_month": stats["season_l1"] += 1
                elif method == "L2_keyword": stats["season_l2"] += 1
                elif method == "L3_hardcoded": stats["season_l3"] += 1
            else:
                stats["season_still_null"] += 1

        # 変更があれば更新リストへ
        if (new_pref, new_region, new_season) != (cur_pref, cur_region, cur_season):
            updates.append((new_pref, new_region, new_season, qid))

    # 一括更新
    cur.executemany("""
        UPDATE festivals SET prefecture=?, region=?, season=? WHERE qid=?
    """, updates)
    conn.commit()

    # 結果出力
    print(f"=== enrich_festivals.py 実行結果 ===")
    print(f"総件数: {stats['total']:,}")
    print(f"")
    print(f"[prefecture]")
    print(f"  既存: {stats['pref_already']:,}")
    print(f"  新規補完: {stats['pref_filled']:,}")
    print(f"    L1 (都道府県フル): {stats['pref_l1']:,}")
    print(f"    L2 (祭り名辞書):   {stats['pref_l2_fest']:,}")
    print(f"    L2 (市区町村辞書): {stats['pref_l2_city']:,}")
    print(f"    L3 (座標逆引き):   {stats['pref_l3_coord']:,}")
    print(f"  残NULL: {stats['pref_still_null']:,}")
    print(f"")
    print(f"[season]")
    print(f"  既存: {stats['season_already']:,}")
    print(f"  新規補完: {stats['season_filled']:,}")
    print(f"    L1 (start_month):  {stats['season_l1']:,}")
    print(f"    L2 (キーワード):   {stats['season_l2']:,}")
    print(f"    L3 (ハードコード): {stats['season_l3']:,}")
    print(f"  残NULL: {stats['season_still_null']:,}")
    print(f"")
    print(f"UPDATE実行: {len(updates):,}件")

    # 補完後の都道府県別カバレッジ
    print(f"\n=== 都道府県別件数（上位15） ===")
    cur.execute("""
        SELECT prefecture, COUNT(*) FROM festivals
        WHERE prefecture IS NOT NULL AND prefecture != ''
        GROUP BY prefecture ORDER BY COUNT(*) DESC LIMIT 15
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

    print(f"\n=== 地域別件数 ===")
    cur.execute("""
        SELECT region, COUNT(*) FROM festivals
        WHERE region IS NOT NULL AND region != ''
        GROUP BY region ORDER BY COUNT(*) DESC
    """)
    for region, cnt in cur.fetchall():
        print(f"  {region:10s}: {cnt:,}")

    conn.close()


if __name__ == "__main__":
    main()
