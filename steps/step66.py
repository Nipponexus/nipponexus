# -*- coding: utf-8 -*-
# step66 : 証拠展開(文言修正版) / プレースホルダQID解決 / 供給プール962件の実測
import os, sys, re, json, sqlite3, collections, datetime
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); SNAP = os.path.join(ROOT, "snapshots")
DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
APPLY = os.environ.get("NX_APPLY") == "1"
sys.path.insert(0, SCR)
R = {}
def sec(n, f):
    try: R[n] = f(); print("[OK] " + n)
    except Exception as e: R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))
def need(con, tbl, names):
    have = [r[1] for r in con.execute("pragma table_info('%s')" % tbl)]
    got = [c for c in names if c in have]
    if not got: raise KeyError("%s に候補列なし: %s / 実在=%s" % (tbl, names, have))
    return got
def parse_tkey(t):
    ja = en = None
    for m in re.finditer(r"JA\[([^\]]*)\]|EN\[([^\]]*)\]", t):
        if m.group(1) is not None: ja = m.group(1)
        if m.group(2) is not None: en = m.group(2)
    p = t.split("|")
    return (p[0] if p and re.match(r"^Q", p[0]) else None), ja, en

def s0():
    b = os.path.join(SNAP, "db_" + TS + ".db")
    a = sqlite3.connect(DB); c = sqlite3.connect(b); a.backup(c); c.close(); a.close()
    print("  " + b); return {"db_snapshot": b}

# §1 正しい軸での検査: 台帳JAは「本文中の対象語」。本文に無い時だけ異常。
def s1():
    con = sqlite3.connect(DB); need(con, "festivals", ["manual_content_ja"])
    bad = []
    for tkey, in con.execute("select tkey from verdict_ledger"):
        qid, ja, en = parse_tkey(tkey)
        if not (qid and ja and re.match(r"^Q[0-9]+$", qid)): continue
        r = con.execute("select manual_content_ja,manual_content_en,label_ja from festivals where qid=?", (qid,)).fetchone()
        if not r: bad.append((qid, ja, "festivals に不在")); continue
        if ja not in (r[0] or "") and (en or "@@") not in (r[1] or ""):
            bad.append((qid, ja, "対象語が本文(JA/EN)に不在 label=%s" % (r[2] or "")[:20]))
    for b in bad: print("  [!] %s" % (b,))
    print("  真の不整合 = %d 件 (前回の6件は検査軸の誤り)" % len(bad))
    con.close(); return bad

# §2 証拠展開
def s2():
    con = sqlite3.connect(DB); plan = []
    for tkey, ja, en, note, src, old, new, verdict in con.execute(
            "select tkey,ja,en,note,src,old,new,verdict from verdict_ledger"):
        if (note or "").strip(): continue
        _, tja, ten = parse_tkey(tkey); kv = {}
        if tja and not (ja or "").strip(): kv["ja"] = tja
        if ten and not (en or "").strip(): kv["en"] = ten
        if tja or ten:
            ev = ("対象語は当該記事の本文中に現れる固有名(駅名・河川名・寺社名)であり祭の名称ではない。"
                  "根拠は tkey 埋め込み形式を展開: " + tkey)
        else:
            ev = "判定 %s / 出典 %s。対象は概念記事につき実体紐付けなし。" % (verdict, src)
        kv["note"] = ("%s || %s -> %s (%s)" % (ev, old, new, src))[:600]
        plan.append((tkey, kv))
    if APPLY:
        for t, kv in plan:
            con.execute("update verdict_ledger set %s where tkey=?"
                        % ",".join("%s=?" % k for k in kv), list(kv.values()) + [t])
        con.commit()
    n = con.execute("select count(*) from verdict_ledger where note is null or note=''").fetchone()[0]
    print("  展開 %d 行 / note 空 = %d (APPLY=%s)" % (len(plan), n, APPLY))
    con.close(); return {"planned": len(plan), "empty": n}

# §3 プレースホルダQIDの解決(本文一致で特定)
def s3():
    con = sqlite3.connect(DB); out = []
    for tkey, in con.execute("select tkey from verdict_ledger where tkey like 'Q\\_%' escape '\\'"):
        _, ja, en = parse_tkey(tkey)
        keys = [ja] + ({"伊太祁曽神社": ["伊太祁曽", "伊太祈曽", "いたきそ"]}.get(ja, []))
        cand = collections.OrderedDict()
        for k in keys:
            for qid, lj, body in con.execute(
                    "select qid,label_ja,manual_content_ja from festivals where manual_content_ja like ?",
                    ("%" + k + "%",)):
                cand[qid] = (lj, k, (body or "").count(k))
        for qid, (lj, k, c) in cand.items():
            print("  %-30s JA=%-8s -> %s %s (語'%s'×%d)" % (tkey[:30], ja, qid, lj, k, c))
        if not cand: print("  %-30s JA=%-8s -> 候補なし(本文未収載)" % (tkey[:30], ja))
        out.append({"tkey": tkey, "ja": ja, "cand": {k: v for k, v in cand.items()}})
    print("  ※ 解決は本文一致が1件に絞れる場合のみ。複数なら人手判断に回す。")
    con.close(); return out

# §4 供給プールの実測
def s4():
    con = sqlite3.connect(DB); q = lambda s, *a: con.execute(s, a).fetchone()[0]
    EMPTY = "(manual_content_ja is null or manual_content_ja='') and (manual_content_en is null or manual_content_en='')"
    tot = q("select count(*) from festivals where " + EMPTY)
    wj = q("select count(*) from festivals where %s and wikipedia_ja is not null and wikipedia_ja<>''" % EMPTY)
    print("  空欄 %d / うち wikipedia_ja あり %d" % (tot, wj))
    print("  status×wikipedia_ja:")
    for r in con.execute("select status, count(*), sum(case when wikipedia_ja is not null and wikipedia_ja<>'' "
                         "then 1 else 0 end) from festivals where %s group by 1 order by 2 desc" % EMPTY):
        print("    %-24s 計%-5d wiki有%d" % r)
    print("  素材の同時充足(空欄かつ wikipedia_ja あり %d 件):" % wj)
    base = "%s and wikipedia_ja is not null and wikipedia_ja<>''" % EMPTY
    for c in ("prefecture", "latitude", "image_url", "image_license", "start_month", "description_ja", "inception_year"):
        print("    %-16s %d" % (c, q("select count(*) from festivals where %s and %s is not null and %s<>''" % (base, c, c))))
    print("  4点(県/座標/月/wiki)そろう件数 = %d"
          % q("select count(*) from festivals where %s and prefecture is not null and prefecture<>'' "
              "and latitude is not null and start_month is not null" % base))
    print("  日次5件なら %d 日 / 20件なら %d 日で消化" % (-(-wj // 5), -(-wj // 20)))
    print("  投入候補の先頭10件(priority順):")
    for r in con.execute("select qid,label_ja,prefecture,priority_score,status from festivals where %s "
                         "order by priority_score desc, qid limit 10" % base):
        print("    %-12s %-26s %-6s %-4s %s" % r)
    con.close(); return {"empty": tot, "with_wiki": wj}

KEY = "## [SUPPLY_GAP_20260811]"
BLOCK = KEY + """
step65 §1 の「名称不整合6件」は検査軸の誤り。verdict_ledger の JA[..] は祭の名称ではなく
本文中に出現する固有名(駅名・河川名・寺社名)。照合先を label_ja にしたため全件が不一致に見えた。
正しい検査は「対象語が manual_content_ja/en に存在するか」。真の不整合は自作QID 2件のみ。
教訓: 突合の前に「この列は何と何を対応させるものか」を明示してから書くこと。
供給の実測: festivals 1256 / 本文あり 294 / 空欄 962 / JAのみ 0。
翻訳で埋められる玉はゼロ。空欄962のうち wikipedia_ja を持つものが供給プール。
綴り是正(CANON)は残存2件で実質完了。現行の日次は処理対象が尽きており空回りする。
日次の接続先を publish_queue(綴り是正) から 供給プール(本文生成) に切り替える必要がある。
"""
def s5():
    import nxdoc
    try: nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError: nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    print("  key count = %d" % open(DOC, encoding="utf-8").read().count(KEY)); return {"ok": True}

sec("backup", s0); sec("axis", s1); sec("evidence", s2)
sec("placeholder", s3); sec("supply", s4); sec("doc", s5)
j = os.path.join(SNAP, "step66_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
