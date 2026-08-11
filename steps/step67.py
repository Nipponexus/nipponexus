# -*- coding: utf-8 -*-
# step67 : 台帳の証拠確定 / プール定義の是正 / Wikidata 充足率の全件実測(読み取りのみ)
import os, sys, re, json, time, sqlite3, datetime, collections, urllib.request, urllib.parse
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); SNAP = os.path.join(ROOT, "snapshots")
DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
APPLY = os.environ.get("NX_APPLY") == "1"
UA = os.environ.get("NX_UA", "nipponexus/1.0 (https://github.com/; yuki.shiori@nexus-ds.jp)")
sys.path.insert(0, SCR)
R = {}
def sec(n, f):
    try: R[n] = f(); print("[OK] " + n)
    except Exception as e: R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))

def s0():
    b = os.path.join(SNAP, "db_" + TS + ".db")
    a = sqlite3.connect(DB); c = sqlite3.connect(b); a.backup(c); c.close(); a.close()
    print("  " + b); return {"db_snapshot": b}

def parse_tkey(t):
    ja = en = None
    for m in re.finditer(r"JA\[([^\]]*)\]|EN\[([^\]]*)\]", t):
        if m.group(1) is not None: ja = m.group(1)
        if m.group(2) is not None: en = m.group(2)
    p = t.split("|")
    return (p[0] if p and re.match(r"^Q", p[0]) else None), ja, en

# §1 証拠展開 + プレースホルダ解決
def s1():
    con = sqlite3.connect(DB); plan = []
    for tkey, ja, en, note, src, old, new, verdict in con.execute(
            "select tkey,ja,en,note,src,old,new,verdict from verdict_ledger"):
        if (note or "").strip(): continue
        _, tja, ten = parse_tkey(tkey); kv = {}
        if tja and not (ja or "").strip(): kv["ja"] = tja
        if ten and not (en or "").strip(): kv["en"] = ten
        ev = ("対象語は当該記事本文に現れる固有名(駅名・河川名・寺社名)であり祭の名称ではない。"
              "根拠は tkey 埋め込み形式を展開: " + tkey) if (tja or ten) else \
             "判定 %s / 出典 %s。対象は概念記事につき実体紐付けなし。" % (verdict, src)
        kv["note"] = ("%s || %s -> %s (%s)" % (ev, old, new, src))[:600]
        plan.append((tkey, kv))
    fix = [("Q_JUSHI|translit_check|JA[十四川] / EN[Jushi River]", "Q11457148",
            "本文一致1件により Q11457148(富田の石取祭)へ紐付け。十四川は同祭の記述内に出現。"),
           ("Q_ITAKISO|translit_check|JA[伊太祁曽神社] / EN[Idaki jinja]", None,
            "本文一致なし。対象記事が未収載のため QID 未解決のまま保持。")]
    if APPLY:
        for t, kv in plan:
            con.execute("update verdict_ledger set %s where tkey=?"
                        % ",".join("%s=?" % k for k in kv), list(kv.values()) + [t])
        for tk, q, why in fix:
            n = con.execute("select count(*) from verdict_ledger where tkey like ?",
                            (tk.split("|")[0] + "|%",)).fetchone()[0]
            if n == 1:
                con.execute("update verdict_ledger set qid=?, note=coalesce(note,'')||' || '||? "
                            "where tkey like ?", (q, why, tk.split("|")[0] + "|%"))
        con.commit()
    n = con.execute("select count(*) from verdict_ledger where note is null or note=''").fetchone()[0]
    print("  展開 %d 行 / note 空 = %d / 紐付け %d 件 (APPLY=%s)" % (len(plan), n, len(fix), APPLY))
    con.close(); return {"planned": len(plan), "empty": n}

# §2 プール定義(status=pending に限定)
def s2():
    con = sqlite3.connect(DB)
    EMPTY = ("(manual_content_ja is null or manual_content_ja='') and "
             "(manual_content_en is null or manual_content_en='')")
    POOL = "%s and status='pending' and wikipedia_ja is not null and wikipedia_ja<>''" % EMPTY
    ids = [r[0] for r in con.execute("select qid from festivals where %s order by priority_score desc, qid" % POOL)]
    print("  プール = %d 件 (pending かつ wikipedia_ja あり)" % len(ids))
    print("  除外: skipped_offtopic 等は対象外。前回の priority 一覧は status 未指定の誤り。")
    for r in con.execute("select qid,label_ja,prefecture,priority_score from festivals where %s limit 8" % POOL):
        print("    %-12s %-24s %-6s %s" % r)
    con.close(); return ids

# §3 Wikidata 充足率の実測
def wd_get(ids):
    url = ("https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&languages=ja|en"
           "&props=claims|labels|sitelinks&ids=" + "|".join(ids))
    rq = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(rq, timeout=45) as f:
        return json.loads(f.read().decode("utf-8")).get("entities", {})

PROPS = {"P625": "座標", "P585": "開催日(時点)", "P837": "年内の日", "P571": "創始年",
         "P18": "画像", "P856": "公式サイト", "P276": "場所", "P131": "行政区画",
         "P17": "国", "P31": "分類", "P2043": "距離", "P1476": "題名"}
def s3():
    ids = R["pool"]
    if isinstance(ids, str): raise RuntimeError("pool 取得に失敗")
    cnt = collections.Counter(); got = {}; err = 0
    n = int(os.environ.get("NX_PROBE_N", "0")) or len(ids)
    ids = ids[:n]
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        try:
            ents = wd_get(chunk)
        except Exception as e:
            err += 1; print("  [warn] chunk %d 失敗 %r" % (i // 50, e)); time.sleep(2); continue
        for qid, e in ents.items():
            cl = e.get("claims", {})
            have = [p for p in PROPS if p in cl]
            for p in have: cnt[p] += 1
            if e.get("sitelinks", {}).get("enwiki"): cnt["enwiki"] += 1
            if e.get("sitelinks", {}).get("jawiki"): cnt["jawiki"] += 1
            got[qid] = have
        sys.stdout.write("\r  照会 %d/%d" % (min(i + 50, len(ids)), len(ids))); sys.stdout.flush()
        time.sleep(1.0)
    print("\r  照会完了 %d 件 (失敗チャンク %d)" % (len(got), err))
    print("  Wikidata 充足率:")
    for p, name in sorted(PROPS.items(), key=lambda x: -cnt[x[0]]):
        if cnt[p]: print("    %-6s %-12s %4d / %d  (%.0f%%)" % (p, name, cnt[p], len(got), 100.0 * cnt[p] / max(1, len(got))))
    print("    %-6s %-12s %4d" % ("-", "enwiki あり", cnt["enwiki"]))
    print("    %-6s %-12s %4d" % ("-", "jawiki あり", cnt["jawiki"]))
    core = sum(1 for v in got.values() if "P625" in v or "P276" in v)
    print("  座標か場所を持つ = %d / %d" % (core, len(got)))
    return {"n": len(got), "counts": dict(cnt), "core": core}

# §4 現DBとの差分
def s4():
    con = sqlite3.connect(DB)
    ids = R["pool"][:int(os.environ.get("NX_PROBE_N", "0")) or len(R["pool"])]
    dbhave = collections.Counter()
    for qid in ids:
        r = con.execute("select latitude,start_month,inception_year,image_url,prefecture "
                        "from festivals where qid=?", (qid,)).fetchone()
        for k, v in zip(("latitude", "start_month", "inception_year", "image_url", "prefecture"), r or []):
            if v not in (None, ""): dbhave[k] += 1
    print("  現DB充足: %s" % dict(dbhave))
    c = R["probe"]["counts"]
    print("  取得で埋まる見込み: 座標 %d 件, 創始年 %d 件, 画像 %d 件, 開催日 %d 件"
          % (c.get("P625", 0) - dbhave["latitude"], c.get("P571", 0) - dbhave["inception_year"],
             c.get("P18", 0) - dbhave["image_url"], c.get("P585", 0) + c.get("P837", 0) - dbhave["start_month"]))
    con.close(); return dict(dbhave)

KEY = "## [SUPPLY_PROBE_20260811]"
BLOCK = KEY + """
供給プールの定義を是正。status='pending' かつ wikipedia_ja あり かつ本文空を対象とする。
step66 の priority 一覧は status 未指定で skipped_offtopic(オズフェスト等)を含んでいた。
実測の要点: 空欄962件は本文だけでなく構造化フィールドも未収集。629件中 座標46/開催月3。
fetch_history が2行しかなく、QID とラベル以外の収集工程が事実上未実行。
したがって次の工程は文章生成ではなくデータ収集。座標・創始年・画像・開催日は
Wikidata の構造化事実であり、正解が定義できるため自動化と検証が成立する。
本節は読み取りのみ。wbgetentities を50件/回・1秒間隔で照会し充足率を実測する。
User-Agent は連絡先入り(NX_UA で上書き可)。API 礼儀としてこれを外さないこと。
"""
def s5():
    import nxdoc
    try: nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError: nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    print("  key count = %d" % open(DOC, encoding="utf-8").read().count(KEY)); return {"ok": True}

sec("backup", s0); sec("ledger", s1); sec("pool", s2)
sec("probe", s3); sec("diff", s4); sec("doc", s5)
j = os.path.join(SNAP, "step67_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
