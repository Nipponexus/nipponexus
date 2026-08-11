# -*- coding: utf-8 -*-
# step74 : 開催日のルール化。規則型を抽出し毎年計算可能にする。二軸検証つき。
import os, sys, re, json, time, sqlite3, datetime, calendar, collections, subprocess, urllib.parse
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); SNAP = os.path.join(ROOT, "snapshots")
DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
UA = os.environ.get("NX_UA", "nipponexus/1.0 (contact: yuki.shiori@nexus-ds.jp)")
APPLY = os.environ.get("NX_APPLY") == "1"
sys.path.insert(0, SCR)
import nxwiki, nxledger
R = {}
def sec(n, f):
    try: R[n] = f(); print("[OK] " + n)
    except Exception as e: R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))

def s0():
    b = os.path.join(SNAP, "db_" + TS + ".db")
    a = sqlite3.connect(DB); c = sqlite3.connect(b); a.backup(c); c.close(); a.close()
    print("  " + b); return {"db_snapshot": b}

DATE = r'''# -*- coding: utf-8 -*-
# DATE_v1 : 日本語の開催日表現 -> 機械可読ルール -> 任意年の実日付。
# 設計方針: 毎年変わる情報は照合相手がいない。だが「規則」は不変なので、
# 規則を保存して毎年計算すれば、外部照会なしに永久に更新できる。
# 規則化できないもの(旬・月のみ・不定)は rule=None とし、自動更新の対象外にする。
import re, calendar, datetime

DOW = {"月": 0, "火": 1, "水": 2, "木": 3, "金": 4, "土": 5, "日": 6}
NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
# 特定年の記述を除外する。「2023年（令和5年）10月29日」は毎年の開催日ではない。
YEARISH = re.compile(r"(\d{4}年|令和\d+年|平成\d+年|昭和\d+年|第\d+回)")
RECUR = re.compile(r"(毎年|例年|恒例)")

PATS = [
 ("nth_dow",   re.compile(r"(\d{1,2})月(?:の)?第([一二三四五1-5])[週]?(?:の)?([日月火水木金土])曜日")),
 ("last_dow",  re.compile(r"(\d{1,2})月(?:の)?最終(?:の)?([日月火水木金土])曜日")),
 ("range_fix", re.compile(r"(\d{1,2})月(\d{1,2})日\s*(?:から|〜|～|-|‐|・)\s*(?:(\d{1,2})月)?(\d{1,2})日")),
 ("fixed",     re.compile(r"(\d{1,2})月(\d{1,2})日")),
]

def _tainted(text, pos, back=16):
    """直前に特定年・回数の記述があれば、それは毎年の開催日ではない。"""
    pre = text[max(0, pos - back):pos]
    if RECUR.search(pre):
        return False
    return bool(YEARISH.search(pre))

def parse(text):
    """最初に見つかった規則を返す。見つからなければ None。"""
    if not text:
        return None
    for kind, rx in PATS:
        for m in rx.finditer(text):
            if _tainted(text, m.start()):
                continue
            g = m.groups()
            if kind == "nth_dow":
                r = {"type": "nth_dow", "month": int(g[0]), "nth": NUM.get(g[1], 0), "dow": DOW[g[2]]}
                if not r["nth"]:
                    continue
            elif kind == "last_dow":
                r = {"type": "last_dow", "month": int(g[0]), "dow": DOW[g[1]]}
            elif kind == "range_fix":
                r = {"type": "range_fixed", "month": int(g[0]), "day": int(g[1]),
                     "end_month": int(g[2]) if g[2] else int(g[0]), "end_day": int(g[3])}
            else:
                r = {"type": "fixed", "month": int(g[0]), "day": int(g[1])}
            r["raw"] = m.group(0)
            r["ctx"] = text[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
            r["pos"] = m.start()
            return r
    return None

def evaluate(rule, year):
    """規則 + 年 -> (開始日, 終了日)。計算不能なら None。"""
    if not rule:
        return None
    t = rule["type"]
    try:
        if t == "fixed":
            d = datetime.date(year, rule["month"], rule["day"]); return (d, d)
        if t == "range_fixed":
            a = datetime.date(year, rule["month"], rule["day"])
            b = datetime.date(year, rule["end_month"], rule["end_day"])
            return (a, b)
        if t == "nth_dow":
            first = datetime.date(year, rule["month"], 1)
            off = (rule["dow"] - first.weekday()) % 7
            day = 1 + off + (rule["nth"] - 1) * 7
            last = calendar.monthrange(year, rule["month"])[1]
            if day > last:
                return None
            d = datetime.date(year, rule["month"], day); return (d, d)
        if t == "last_dow":
            last = calendar.monthrange(year, rule["month"])[1]
            d = datetime.date(year, rule["month"], last)
            d -= datetime.timedelta(days=(d.weekday() - rule["dow"]) % 7)
            return (d, d)
    except ValueError:
        return None
    return None

def describe(rule):
    if not rule: return ""
    t = rule["type"]
    if t == "fixed": return "毎年%d月%d日" % (rule["month"], rule["day"])
    if t == "range_fixed": return "毎年%d月%d日〜%d月%d日" % (rule["month"], rule["day"], rule["end_month"], rule["end_day"])
    if t == "nth_dow": return "毎年%d月第%d%s曜日" % (rule["month"], rule["nth"], "月火水木金土日"[rule["dow"]])
    if t == "last_dow": return "毎年%d月最終%s曜日" % (rule["month"], "月火水木金土日"[rule["dow"]])
    return ""

CALC = ("nth_dow", "last_dow")

def verify_against_text(rule, fulltext):
    """独立検証: 規則から過去年の日付を計算し、本文中の『YYYY年…M月D日』と突き合わせる。
    導入部の規則文とは別の箇所(沿革・日程表)に一致があれば、二つ目の根拠になる。"""
    if not rule or rule["type"] not in CALC or not fulltext:
        return None
    hits, miss = [], []
    for m in re.finditer(r"(\d{4})年[^。]{0,24}?(\d{1,2})月(\d{1,2})日", fulltext):
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if not (1990 <= y <= 2030) or mo != rule["month"]:
            continue
        got = evaluate(rule, y)
        if not got:
            continue
        (hits if got[0].day == d else miss).append("%d年%d月%d日(計算=%d日)" % (y, mo, d, got[0].day))
    if not hits and not miss:
        return None
    return {"match": hits[:4], "mismatch": miss[:4], "ok": len(hits) > 0 and len(hits) >= len(miss)}
'''

def s1():
    p = os.path.join(SCR, "nxdate.py")
    open(p, "w", encoding="utf-8").write(DATE)
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    subprocess.run([sys.executable, os.path.join(SCR, "nxname.py"), p], check=True)
    import nxdate
    cases = [
      ("静岡県下田市で5月第3金曜日から日曜日にかけて", "nth_dow", (2026, 5, 15)),
      ("石川県鳳珠郡能登町宇出津で毎年7月第1金曜日および土曜日に行われる", "nth_dow", (2026, 7, 3)),
      ("毎年7月の最終土曜日に開催される", "last_dow", (2026, 7, 25)),
      ("千葉県いすみ市で、毎年9月23日、24日に行われる祭礼", "fixed", (2026, 9, 23)),
      ("毎年6月30日から7月2日に催される祭り", "range_fixed", (2026, 6, 30)),
      ("最新開催は2020年予定だったが延期され、2023年（令和5年）10月29日開催となった。", None, None),
    ]
    for txt, exp, want in cases:
        r = nxdate.parse(txt)
        got = r["type"] if r else None
        ev = nxdate.evaluate(r, 2026) if r else None
        ok = (got == exp) and (want is None or (ev and (ev[0].year, ev[0].month, ev[0].day) == want))
        print("    %-6s %-11s %-12s %s" % ("OK" if ok else "NG", str(got), str(ev[0]) if ev else "-", txt[:34]))
        assert ok, (txt, exp, got, ev)
    print("  自己検証 OK (特定年の記述『2023年…10月29日』は正しく除外)")
    return {"cases": len(cases)}

def s2():
    con = sqlite3.connect(DB)
    have = [r[1] for r in con.execute("pragma table_info('festivals')")]
    added = []
    for c in ("date_rule", "date_rule_json", "date_rule_src", "date_verified"):
        if c not in have:
            con.execute("alter table festivals add column %s TEXT" % c); added.append(c)
    con.commit(); con.close()
    print("  列追加 = %s (追加のみ・非破壊)" % added); return added

def s3():
    import nxdate
    con = sqlite3.connect(DB)
    rows = con.execute(
        "select qid,label_ja,wikipedia_ja,prefecture,"
        "case when manual_content_ja is null or manual_content_ja='' then 0 else 1 end "
        "from festivals where wikipedia_ja is not null and wikipedia_ja<>'' "
        "and status in ('pending','drafted') order by (manual_content_ja is null), priority_score desc").fetchall()
    n = int(os.environ.get("NX_N", "150"))
    rows = rows[:n]
    tmap = collections.OrderedDict()
    for r in rows: tmap.setdefault(nxwiki.title_of(r[2], r[1]), []).append(r)
    print("  対象 %d 件 / %d タイトル (導入部)" % (len(rows), len(tmap)))
    ext = nxwiki.extracts(list(tmap), intro=True, ua=UA)
    res, cnt = [], collections.Counter()
    for t, lst in tmap.items():
        rule = nxdate.parse(ext.get(t, ""))
        for qid, lab, wj, pf, pub in lst:
            k = rule["type"] if rule else "none"
            cnt[k] += 1
            if rule and rule["type"] in nxdate.CALC: cnt["calculable"] += 1
            res.append({"qid": qid, "label": lab, "title": t, "pub": pub, "rule": rule,
                        "desc": nxdate.describe(rule)})
    print("  種別内訳 = %s" % dict(cnt))
    print("  毎年計算できる規則型 = %d 件 (%.0f%%)" % (cnt["calculable"], 100.0*cnt["calculable"]/max(1,len(res))))
    return res

def s4():
    import nxdate
    cand = [x for x in R["parse"] if x["rule"] and x["rule"]["type"] in nxdate.CALC]
    n = int(os.environ.get("NX_V", "25"))
    cand = cand[:n]
    print("  規則型 %d 件を全文で独立検証 (1件ずつ取得のため時間がかかる)" % len(cand))
    ok = ng = na = 0
    for i, x in enumerate(cand):
        full = nxwiki.extracts([x["title"]], intro=False, ua=UA, verbose=False).get(x["title"], "")
        v = nxdate.verify_against_text(x["rule"], full)
        x["verify"] = v
        if v is None:
            na += 1; mark = "照合材料なし"
        elif v["ok"]:
            ok += 1; mark = "一致 " + ",".join(v["match"][:2])
        else:
            ng += 1; mark = "不一致 " + ",".join(v["mismatch"][:2])
        print("    %-11s %-18s %-16s %s" % (x["qid"], (x["label"] or "")[:18], x["desc"], mark))
        sys.stdout.flush()
    print("  検証: 一致 %d / 不一致 %d / 材料なし %d" % (ok, ng, na))
    print("  ※ 一致=導入部の規則と本文中の実績日が独立に符合。不一致は規則の誤読か例外年。")
    return {"ok": ok, "ng": ng, "na": na}

def s5():
    import nxdate
    con = sqlite3.connect(DB); n = 0
    y = datetime.date.today().year
    for x in R["parse"]:
        r = x["rule"]
        if not r: continue
        v = x.get("verify")
        conf = "verified" if (v and v.get("ok")) else ("計算型/未検証" if r["type"] in nxdate.CALC else "固定日/規則のみ")
        if APPLY:
            con.execute("update festivals set date_rule=?, date_rule_json=?, date_rule_src=?, "
                        "date_verified=?, updated_at=? where qid=?",
                        (x["desc"], json.dumps(r, ensure_ascii=False), "jawiki導入部: " + r["ctx"][:200],
                         conf, TS, x["qid"]))
            n += 1
    if APPLY: con.commit()
    print("  規則を保存 %d 件 (APPLY=%s)" % (n, APPLY))
    print("  今年(%d)の日付が出せる例:" % y)
    for x in [z for z in R["parse"] if z["rule"] and z["rule"]["type"] in nxdate.CALC][:8]:
        d = nxdate.evaluate(x["rule"], y)
        print("    %-11s %-18s %-16s -> %s" % (x["qid"], (x["label"] or "")[:18], x["desc"],
                                               d[0].strftime("%Y-%m-%d(%a)") if d else "-"))
    con.close(); return n

KEY = "## [DATE_RULE_V1_20260811]"
BLOCK = KEY + """
不労所得ロードマップ第一段。毎年変わる開催日は照合相手がおらず自動検証できないが、
「規則」は不変なので規則を保存すれば外部照会なしに毎年計算で更新できる。
これが唯一、放置しても中身が新しくなる部分であり、更新性の土台になる。
DATE_v1(scripts/nxdate.py): 第N曜日型・最終曜日型・固定日型・期間型を抽出し JSON 規則化。
evaluate(rule, year) で任意年の実日付を返す。旬・月のみ・不定は規則化せず自動更新の対象外。
特定年の除外: 「2023年（令和5年）10月29日」は毎年の開催日ではない。直前16字に
西暦・元号・第N回があり毎年/例年を伴わない場合は棄却する(_tainted)。
独立検証: 規則から過去年の日付を計算し、本文中の『YYYY年…M月D日』(沿革や日程表)と突合。
導入部の規則文とは別箇所での符合なので、二つ目の根拠として機能する。
festivals に date_rule / date_rule_json / date_rule_src / date_verified を追加(非破壊)。
なお第N曜日型でも自治体判断で例外年がある。verified 以外は表示時に断定しないこと。
"""
def s6():
    import nxdoc
    try: nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError: nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    print("  key count = %d" % open(DOC, encoding="utf-8").read().count(KEY)); return {"ok": True}

sec("backup", s0); sec("date", s1); sec("cols", s2)
sec("parse", s3); sec("verify", s4); sec("save", s5); sec("doc", s6)
def _j(o):
    if isinstance(o, dict): return {("|".join(map(str,k)) if isinstance(k,tuple) else str(k)): _j(v) for k,v in o.items()}
    if isinstance(o, (list, tuple)): return [_j(x) for x in o]
    return o
j = os.path.join(SNAP, "step74_" + TS + ".json")
try:
    open(j, "w", encoding="utf-8").write(json.dumps(_j(R), ensure_ascii=False, indent=1, default=str))
except Exception as e:
    open(j + ".txt", "w", encoding="utf-8").write(repr(R)); print("[warn] JSON化失敗 %r" % (e,))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
