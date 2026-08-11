# -*- coding: utf-8 -*-
# step75 : 検証器の精度改善(多日開催・文脈語) / 規則の本保存 / 第二段「今週の祭り」試作
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

VERIFY2 = r'''
# >>>NX:VERIFY2
# verify_v2 : v1 の欠陥を修正した独立検証。
#  欠陥1 = 多日開催を考慮せず開始日のみ比較。川越氷川祭(第3土曜と日曜)で偽の不一致。
#  欠陥2 = 同月の無関係な日付(文化財指定日・別行事)を拾う。文脈語で絞る。
HELD = re.compile(r"(開催|行われ|行なわれ|実施|挙行|斎行|催さ|開かれ)")
NOTHELD = re.compile(r"(指定|創建|設立|認定|登録|選択|竣工|落成|廃止|中止|生まれ|死去)")

def verify_v2(rule, fulltext, tol=3):
    """規則から計算した日付と、本文中の実績日を突き合わせる。
    tol 日以内は多日開催の別日とみなし一致扱い。判定材料は文脈語で絞る。"""
    if not rule or not fulltext:
        return None
    match, mism = [], []
    for m in re.finditer(r"(\d{4})年[^。]{0,30}?(\d{1,2})月(\d{1,2})日", fulltext):
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if not (1990 <= y <= 2035) or mo != rule.get("month"):
            continue
        ctx = fulltext[max(0, m.start() - 30): m.end() + 30]
        if NOTHELD.search(ctx) and not HELD.search(ctx):
            continue
        if not HELD.search(ctx):
            continue
        got = evaluate(rule, y)
        if not got:
            continue
        diff = abs((datetime.date(y, mo, d) - got[0]).days)
        rec = "%d年%d月%d日(計算%d日 差%d)" % (y, mo, d, got[0].day, diff)
        (match if diff <= tol else mism).append(rec)
    if not match and not mism:
        return None
    return {"match": match[:4], "mismatch": mism[:4],
            "ok": len(match) > 0 and len(match) > len(mism)}

# カレンダーに置ける型。固定日・期間も毎年同じ日付なので配置可能。
PLACEABLE = ("nth_dow", "last_dow", "fixed", "range_fixed")
# 年ごとに計算が要る型(それ以外は毎年同一日)
NEEDS_CALC = ("nth_dow", "last_dow")
# <<<NX:VERIFY2
'''

def s1():
    p = os.path.join(SCR, "nxdate.py")
    s = open(p, encoding="utf-8").read()
    if ">>>NX:VERIFY2" in s:
        s = re.sub(r"\n# >>>NX:VERIFY2.*?# <<<NX:VERIFY2\n", "\n", s, flags=re.S)
    open(p, "w", encoding="utf-8").write(s + VERIFY2)
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    subprocess.run([sys.executable, os.path.join(SCR, "nxname.py"), p], check=True)
    import importlib, nxdate; importlib.reload(nxdate)
    r = nxdate.parse("毎年10月第3日曜日に行われる")
    t = "2022年10月15日に川越氷川祭が開催された。1988年10月20日に国の文化財に指定された。"
    v = nxdate.verify_v2(r, t)
    print("    多日開催の許容: %s" % v)
    assert v and v["ok"], v
    t2 = "1981年7月26日に国の重要無形民俗文化財に指定された。"
    assert nxdate.verify_v2(nxdate.parse("毎年7月第4土曜日に行われる"), t2) is None, "指定日を拾っている"
    print("  自己検証 OK (土日開催の差1日を一致 / 指定日を除外)")
    print("  PLACEABLE = %s" % (nxdate.PLACEABLE,))
    return {"ok": True}

def s2():
    import nxdate
    con = sqlite3.connect(DB)
    rows = con.execute(
        "select qid,label_ja,wikipedia_ja,prefecture,"
        "case when manual_content_ja is null or manual_content_ja='' then 0 else 1 end "
        "from festivals where wikipedia_ja is not null and wikipedia_ja<>'' "
        "and status in ('pending','drafted') order by (manual_content_ja is null), priority_score desc").fetchall()
    n = int(os.environ.get("NX_N", "300"))
    rows = rows[:n]
    tmap = collections.OrderedDict()
    for r in rows: tmap.setdefault(nxwiki.title_of(r[2], r[1]), []).append(r)
    print("  対象 %d 件 / %d タイトル" % (len(rows), len(tmap)))
    ext = nxwiki.extracts(list(tmap), intro=True, ua=UA)
    res, cnt = [], collections.Counter()
    for t, lst in tmap.items():
        rule = nxdate.parse(ext.get(t, ""))
        for qid, lab, wj, pf, pub in lst:
            cnt[rule["type"] if rule else "none"] += 1
            if rule: cnt["placeable"] += 1
            if rule and rule["type"] in nxdate.NEEDS_CALC: cnt["needs_calc"] += 1
            res.append({"qid": qid, "label": lab, "title": t, "pref": pf, "pub": pub,
                        "rule": rule, "desc": nxdate.describe(rule)})
    print("  種別内訳 = %s" % dict(cnt))
    print("  カレンダーに配置可能 = %d / %d (%.0f%%)  うち年次計算が要る型 %d"
          % (cnt["placeable"], len(res), 100.0*cnt["placeable"]/max(1,len(res)), cnt["needs_calc"]))
    con.close(); return res

def s3():
    import nxdate
    cand = [x for x in R["parse"] if x["rule"] and x["rule"]["type"] in nxdate.NEEDS_CALC]
    n = int(os.environ.get("NX_V", "20"))
    cand = cand[:n]
    print("  年次計算型 %d 件を全文で再検証" % len(cand))
    ok = ng = na = 0
    for x in cand:
        full = nxwiki.extracts([x["title"]], intro=False, ua=UA, verbose=False).get(x["title"], "")
        v = nxdate.verify_v2(x["rule"], full)
        x["verify"] = v
        if v is None: na += 1; mk = "材料なし"
        elif v["ok"]: ok += 1; mk = "一致 " + ",".join(v["match"][:2])
        else: ng += 1; mk = "不一致 " + ",".join(v["mismatch"][:2])
        print("    %-11s %-18s %-16s %s" % (x["qid"], (x["label"] or "")[:18], x["desc"], mk))
        sys.stdout.flush()
    print("  一致 %d / 不一致 %d / 材料なし %d  (v1 は 4/6/5)" % (ok, ng, na))
    return {"ok": ok, "ng": ng, "na": na}

def s4():
    import nxdate
    con = sqlite3.connect(DB); n = 0
    for x in R["parse"]:
        r = x["rule"]
        if not r: continue
        v = x.get("verify")
        if v and v.get("ok"): conf = "verified"
        elif v and not v.get("ok"): conf = "conflict"
        elif r["type"] in nxdate.NEEDS_CALC: conf = "rule_only"
        else: conf = "fixed_rule"
        if APPLY:
            con.execute("update festivals set date_rule=?, date_rule_json=?, date_rule_src=?, "
                        "date_verified=?, updated_at=? where qid=?",
                        (x["desc"], json.dumps(r, ensure_ascii=False),
                         "jawiki導入部: " + r["ctx"][:200], conf, TS, x["qid"]))
            n += 1
    if APPLY: con.commit()
    print("  保存 %d 件 (APPLY=%s)" % (n, APPLY))
    print("  信頼度内訳 = %s" % dict(collections.Counter(
        ("verified" if (x.get("verify") or {}).get("ok") else
         "conflict" if x.get("verify") else
         "rule_only" if x["rule"] and x["rule"]["type"] in nxdate.NEEDS_CALC else "fixed_rule")
        for x in R["parse"] if x["rule"])))
    con.close(); return n

def s5():
    import nxdate
    today = datetime.date.today()
    rows = []
    for x in R["parse"]:
        if not x["rule"]: continue
        for y in (today.year, today.year + 1):
            d = nxdate.evaluate(x["rule"], y)
            if not d: continue
            delta = (d[0] - today).days
            if 0 <= delta <= 60:
                rows.append((d[0], d[1], x, delta)); break
    rows.sort(key=lambda r: r[0])
    print("  ── 第二段の試作: 今日から60日以内に開催される祭 ──")
    print("  %-12s %-24s %-6s %-16s %s" % ("開催日", "名称", "県", "規則", "確度"))
    for d0, d1, x, delta in rows[:30]:
        v = x.get("verify")
        conf = "検証済" if (v and v.get("ok")) else ("要確認" if v else "規則のみ")
        span = d0.strftime("%m/%d(%a)") + ("" if d0 == d1 else "-" + d1.strftime("%m/%d"))
        print("  %-12s %-24s %-6s %-16s %s (%d日後)"
              % (span, (x["label"] or "")[:24], x["pref"] or "-", x["desc"], conf, delta))
    print("  60日以内 = %d 件 / 規則を持つ全 %d 件"
          % (len(rows), sum(1 for x in R["parse"] if x["rule"])))
    print("  ※ これが毎日自動で入れ替わる。外部照会ゼロ、計算のみで更新される。")
    return len(rows)

KEY = "## [DATE_VERIFY_V2_CALENDAR_20260811]"
BLOCK = KEY + """
verify_v1 の不一致6件は大半が検証器の欠陥だった。川越氷川祭は第3土曜と日曜の二日間開催で、
本文の実績日(土)と計算値(日)を別物と判定していた。戸畑祇園・貴船まつりの不一致は
同月の無関係な日付(文化財指定日など)を拾ったもの。
verify_v2: 多日開催を考慮し差3日以内を一致、日付近傍に開催語(開催/行われ/斎行)を要求し、
指定・創建・登録のみの文脈は除外する。検証器が出す極端な数字はまず検証器を疑うこと。
配置可能の再定義: 年次計算が要るのは第N曜日型と最終曜日型のみだが、固定日型と期間型も
毎年同じ日付でカレンダーに置ける。「計算型10%」は誤りで、実際は約46%が配置可能。
第二段(今週の祭り)の母数はこの46%であり、外部照会なしに毎日入れ替わる。
date_verified の四値: verified(実績日と符合) / conflict(符合しない) / rule_only(材料なし) /
fixed_rule(固定日で年次計算不要)。conflict と rule_only は表示時に断定しない。
"""
def s6():
    import nxdoc
    try: nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError: nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    print("  key count = %d" % open(DOC, encoding="utf-8").read().count(KEY)); return {"ok": True}

sec("backup", s0); sec("verify2", s1); sec("parse", s2)
sec("recheck", s3); sec("save", s4); sec("calendar", s5); sec("doc", s6)
def _j(o):
    if isinstance(o, dict): return {("|".join(map(str,k)) if isinstance(k,tuple) else str(k)): _j(v) for k,v in o.items()}
    if isinstance(o, (list, tuple)): return [_j(x) for x in o]
    return o
j = os.path.join(SNAP, "step75_" + TS + ".json")
try: open(j, "w", encoding="utf-8").write(json.dumps(_j(R), ensure_ascii=False, indent=1, default=str))
except Exception as e:
    open(j + ".txt", "w", encoding="utf-8").write(repr(R)); print("[warn] JSON化失敗 %r" % (e,))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
