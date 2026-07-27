# -*- coding: utf-8 -*-
"""接ぎ木・現況断定・DBメタ矛盾の決定論検出器 (111深大寺の実データを基準に設計)"""
import re, sqlite3

import os
DB = os.path.expanduser("~/nipponexus/data/sqlite/nipponexus.db")

ORIGIN_ANCHOR = re.compile(r"起源|由来|ルーツ|さかのぼる|にちなみ|始まり")
ORIGIN_SUBJ = [
    re.compile(r"[「『]([^」』]{2,14})[」』]の縁日"),
    re.compile(r"([一-龥ァ-ヶー]{2,14})の縁日"),
    re.compile(r"([一-龥ァ-ヶー]{2,14})の功徳日"),
    re.compile(r"[「『]?([^」』\s、。]{2,14})[」』]?をルーツ"),
]
DROP_SUBJ = {"この", "その", "同じ", "毎年", "現在", "同様"}
def _clean_subj(s):
    s = s.strip()
    if s.startswith(("の","を","は","が","と")): return None
    if s.endswith(("縁日","功徳日","行事","祭り")): return None
    if len(s) < 3 or s in DROP_SUBJ: return None
    return s

START_CTX = re.compile(r"開始|始まっ|第1回|第一回|創始|発足|立ち上げ|ようになった")
YEAR = re.compile(r"(1[5-9]\d{2}|20[0-4]\d)年")
ANNIV = re.compile(r"(20[0-4]\d)年.{0,20}?(\d{1,3})周年")

STATUS_ASSERT = re.compile(r"再開され|再開した|現在も(?:毎年)?(?:開催|続)|毎年開催されて|継続して開催|復活を遂げ")
STATUS_ASSERT_EN = re.compile(r"has (?:since )?resumed|resumed (?:since|after)|has (?:since )?been held again|continues to be held annually", re.I)
OFFICIAL_NOTE = re.compile(r"公式(?:サイト|ホームページ)?で(?:最新|開催|実施)?.{0,8}確認|最新の.{0,12}公式")
OFFICIAL_NOTE_EN = re.compile(r"check the official (?:web)?site|refer to the official", re.I)

READING_TABLE = {
    "四万六千日": {"expected": ["shimanrokusennichi", "46,000 days"],
                   "forbidden": ["man'nichi", "mannichi", "shimanroku-sen'nichi-shi"]},
    "深沙大王": {"expected": ["jinja daio", "jinjadaio", "jinsha daio"], "forbidden": []},
}

def _norm_en(s):
    return s.replace("\u2019", "'").replace("\u2018", "'").lower()

def detect_origin_conflict(ja):
    subj, ev = [], []
    for i, line in enumerate(ja.split("\n"), 1):
        if not ORIGIN_ANCHOR.search(line):
            continue
        for rx in ORIGIN_SUBJ:
            for m in rx.finditer(line):
                s = _clean_subj(m.group(1))
                if not s:
                    continue
                if s not in subj:
                    subj.append(s); ev.append((i, s))
    subj = [a for a in subj if not any(a != b and a in b for b in subj)]
    ev = [(i, s) for i, s in ev if s in subj]
    return (len(subj) >= 2), subj, ev

def detect_meta_year_conflict(ja, inception, start_month):
    ng = []
    for i, line in enumerate(ja.split("\n"), 1):
        if START_CTX.search(line):
            for y in YEAR.findall(line):
                if inception and abs(int(y) - int(inception)) >= 1:
                    ng.append((i, "開始年", "本文%s / DB inception_year %s" % (y, inception)))
    for m in ANNIV.finditer(ja):
        y, n = int(m.group(1)), int(m.group(2))
        implied = y - n + 1
        if inception and implied != int(inception):
            ng.append((0, "周年逆算", "%s年%s周年→初回%s / DB %s" % (y, n, implied, inception)))
    if start_month:
        months = set(int(x) for x in re.findall(r"例年(\d{1,2})月", ja))
        if months and int(start_month) not in months:
            ng.append((0, "開催月", "本文%s / DB start_month %s" % (sorted(months), start_month)))
    return (len(ng) > 0), ng

def detect_status_assertion(ja, en):
    ng = []
    for tag, text, rx, note in (("JA", ja, STATUS_ASSERT, OFFICIAL_NOTE),
                                ("EN", en, STATUS_ASSERT_EN, OFFICIAL_NOTE_EN)):
        for i, line in enumerate(text.split("\n"), 1):
            if rx.search(line) and not note.search(line):
                ng.append((tag, i, line.strip()[:60]))
    return (len(ng) > 0), ng

def detect_reading_mismatch(ja, en):
    ng, warn = [], []
    enn = _norm_en(en)
    for term, d in READING_TABLE.items():
        if term not in ja:
            continue
        for f in d["forbidden"]:
            if f in enn:
                ng.append((term, "禁止読み", f))
        if d["expected"] and not any(e in enn for e in d["expected"]):
            warn.append((term, "期待読み不在", "/".join(d["expected"])))
    return (len(ng) > 0), ng, warn

def load_meta(qid):
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("SELECT inception_year, start_month, label_ja FROM festivals WHERE qid=?", (qid,))
    r = cur.fetchone(); con.close()
    return r if r else (None, None, None)

def run(qid, ja, en):
    inc, sm, label = load_meta(qid)
    print("== %s %s (inception=%s start_month=%s) ==" % (qid, label, inc, sm))
    hit, subj, ev = detect_origin_conflict(ja)
    print("1 起源主体の自己矛盾 : %s  %s" % ("NG" if hit else "OK", subj))
    for i, s in ev: print("     L%-4s %s" % (i, s))
    hit, ng = detect_meta_year_conflict(ja, inc, sm)
    print("2 DBメタ突合         : %s%s" % ("NG" if hit else "OK",
          "  [WARN] start_month=None (投入時に必須セット)" if not sm else ""))
    for i, k, v in ng: print("     L%-4s [%s] %s" % (i, k, v))
    hit, ng = detect_status_assertion(ja, en)
    print("3 現況断定ガード     : %s" % ("NG" if hit else "OK"))
    for t, i, v in ng: print("     %s L%-4s %s" % (t, i, v))
    hit, ng, warn = detect_reading_mismatch(ja, en)
    print("4 訳語の読み照合     : %s" % ("NG" if hit else "OK"))
    for a, b, c in ng: print("     NG   %s %s: %s" % (a, b, c))
    for a, b, c in warn: print("     WARN %s %s: %s" % (a, b, c))
