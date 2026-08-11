# -*- coding: utf-8 -*-
# step71 : exlimit 修正 / 県名リスト厳密化 / 不一致を二系統(jawiki+Wikidata)で交差検証 / 原因究明
import os, sys, re, json, time, sqlite3, datetime, collections, subprocess, urllib.request, urllib.parse
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); SNAP = os.path.join(ROOT, "snapshots")
DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
UA = os.environ.get("NX_UA", "nipponexus/1.0 (contact: yuki.shiori@nexus-ds.jp)")
APPLY = os.environ.get("NX_APPLY") == "1"
sys.path.insert(0, SCR)
R = {}
def sec(n, f):
    try: R[n] = f(); print("[OK] " + n)
    except Exception as e: R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))

WIKI2 = r'''# -*- coding: utf-8 -*-
# WIKI_v2 : jawiki 取得。v1 の欠陥 = exlimit 未指定。
# MediaWiki の prop=extracts は exintro 無し(全文)だと exlimit が 1 に制限され、
# 20件バッチで投げると先頭1件しか返らない。全文取得は必ず1件ずつ。
import json, time, sys, urllib.request, urllib.parse
UA_DEFAULT = "nipponexus/1.0 (contact: yuki.shiori@nexus-ds.jp)"

PREFS = ["\u5317\u6d77\u9053","\u9752\u68ee\u770c","\u5ca9\u624b\u770c","\u5bae\u57ce\u770c","\u79cb\u7530\u770c",
"\u5c71\u5f62\u770c","\u798f\u5cf6\u770c","\u8328\u57ce\u770c","\u6803\u6728\u770c","\u7fa4\u99ac\u770c",
"\u57fc\u7389\u770c","\u5343\u8449\u770c","\u6771\u4eac\u90fd","\u795e\u5948\u5ddd\u770c","\u65b0\u6f5f\u770c",
"\u5bcc\u5c71\u770c","\u77f3\u5ddd\u770c","\u798f\u4e95\u770c","\u5c71\u68a8\u770c","\u9577\u91ce\u770c",
"\u5c90\u961c\u770c","\u9759\u5ca1\u770c","\u611b\u77e5\u770c","\u4e09\u91cd\u770c","\u6ecb\u8cc0\u770c",
"\u4eac\u90fd\u5e9c","\u5927\u962a\u5e9c","\u5175\u5eab\u770c","\u5948\u826f\u770c","\u548c\u6b4c\u5c71\u770c",
"\u9ce5\u53d6\u770c","\u5cf6\u6839\u770c","\u5ca1\u5c71\u770c","\u5e83\u5cf6\u770c","\u5c71\u53e3\u770c",
"\u5fb3\u5cf6\u770c","\u9999\u5ddd\u770c","\u611b\u5a9b\u770c","\u9ad8\u77e5\u770c","\u798f\u5ca1\u770c",
"\u4f50\u8cc0\u770c","\u9577\u5d0e\u770c","\u718a\u672c\u770c","\u5927\u5206\u770c","\u5bae\u5d0e\u770c",
"\u9e7f\u5150\u5cf6\u770c","\u6c96\u7e04\u770c"]
_PREF_RX = None
def pref_findall(text):
    """正規表現の総称パターンは『年千葉県』のような誤検出を生む。47固定リストで走査する。"""
    global _PREF_RX
    import re
    if _PREF_RX is None:
        _PREF_RX = re.compile("|".join(sorted(PREFS, key=len, reverse=True)))
    return list(dict.fromkeys(_PREF_RX.findall(text or "")))

def api(host, params, ua=None, timeout=45):
    url = "https://%s/w/api.php?%s" % (host, urllib.parse.urlencode(params))
    rq = urllib.request.Request(url, headers={"User-Agent": ua or UA_DEFAULT})
    with urllib.request.urlopen(rq, timeout=timeout) as f:
        return json.loads(f.read().decode("utf-8"))

def extracts(titles, intro=True, ua=None, sleep=1.0, verbose=True):
    out = {t: "" for t in titles}
    batch = 20 if intro else 1
    for i in range(0, len(titles), batch):
        chunk = titles[i:i + batch]
        p = {"action": "query", "format": "json", "prop": "extracts", "explaintext": 1,
             "redirects": 1, "exlimit": (20 if intro else 1), "titles": "|".join(chunk)}
        if intro:
            p["exintro"] = 1
        try:
            d = api("ja.wikipedia.org", p, ua)
        except Exception as e:
            if verbose: print("  [warn] %r" % e)
            time.sleep(2); continue
        q = d.get("query", {})
        by = {pg.get("title"): (pg.get("extract") or "") for pg in q.get("pages", {}).values()}
        alias = {}
        for r in (q.get("redirects") or []): alias[r["from"]] = r["to"]
        for nz in (q.get("normalized") or []): alias[nz["from"]] = nz["to"]
        for t in chunk:
            cur, k = t, 0
            while cur in alias and k < 5:
                cur = alias[cur]; k += 1
            out[t] = by.get(cur, by.get(t, ""))
        if verbose:
            sys.stdout.write("\r  取得 %d/%d" % (min(i + batch, len(titles)), len(titles))); sys.stdout.flush()
        time.sleep(sleep)
    if verbose: print()
    return out

def title_of(url, label):
    if url and "/" in url:
        return urllib.parse.unquote(url.rstrip("/").split("/")[-1]).replace("_", " ")
    return url or label
'''

def s0():
    p = os.path.join(SCR, "nxwiki.py")
    open(p, "w", encoding="utf-8").write(WIKI2)
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    subprocess.run([sys.executable, os.path.join(SCR, "nxname.py"), p], check=True)
    import importlib, nxwiki; importlib.reload(nxwiki)
    t = ["七尾港まつり", "黒船祭", "神嘗祭", "あばれ祭り", "京都三大祭り"]
    a = nxwiki.extracts(t, intro=True, ua=UA, verbose=False)
    b = nxwiki.extracts(t, intro=False, ua=UA, verbose=False)
    for k in t:
        print("    %-12s intro=%4d字 full=%6d字" % (k, len(a[k]), len(b[k])))
    assert all(a.values()) and all(b.values()), "取得漏れ"
    assert nxwiki.pref_findall("2019年千葉県香取市") == ["千葉県"], nxwiki.pref_findall("2019年千葉県香取市")
    print("  自己検証 OK (exlimit=1 で全文取得可 / 『年千葉県』誤検出も解消)")
    return {"ok": True}

def wd(ids, props="claims", langs=None):
    import nxwiki
    out = {}
    for i in range(0, len(ids), 50):
        p = {"action": "wbgetentities", "format": "json", "props": props, "ids": "|".join(ids[i:i+50])}
        if langs: p["languages"] = langs
        try:
            out.update(wdapi(p))
        except Exception as e:
            print("  [warn] wd %r" % e)
        time.sleep(1.0)
    return out
def wdapi(p):
    import nxwiki
    return nxwiki.api("www.wikidata.org", p, UA).get("entities", {})

def claim_ids(ent, prop):
    r = []
    for c in ent.get("claims", {}).get(prop, []):
        v = (c.get("mainsnak", {}).get("datavalue", {}) or {}).get("value", {})
        if isinstance(v, dict) and v.get("id"): r.append(v["id"])
    return r

def wd_prefecture(qids):
    """P131/P276 を上位へ辿り、47都道府県のいずれかに到達したら返す。"""
    import nxwiki
    ents = wd(qids)
    result = {}; frontier = {}
    for q in qids:
        e = ents.get(q, {})
        frontier[q] = claim_ids(e, "P131") + claim_ids(e, "P276")
    for _ in range(3):
        need = sorted({x for v in frontier.values() for x in v} - set())
        if not need: break
        info = wd(need, props="claims|labels", langs="ja")
        lab = {q: (i.get("labels", {}).get("ja", {}).get("value") or "") for q, i in info.items()}
        nxt = {}
        for q, cands in frontier.items():
            if q in result: continue
            up = []
            for c in cands:
                if lab.get(c) in nxwiki.PREFS:
                    result[q] = lab[c]; break
                up += claim_ids(info.get(c, {}), "P131")
            if q not in result: nxt[q] = up
        frontier = nxt
        if not frontier: break
    return result

# ---------- §1 交差検証 ----------
def s1():
    import nxwiki
    con = sqlite3.connect(DB)
    rows = con.execute("select qid,label_ja,wikipedia_ja,prefecture,location_qid,location_label_ja,status,"
                       "case when manual_content_ja is null or manual_content_ja='' then 0 else 1 end "
                       "from festivals where prefecture is not null and prefecture<>'' "
                       "and wikipedia_ja is not null and wikipedia_ja<>'' order by qid").fetchall()
    n = int(os.environ.get("NX_N", "0")) or len(rows)
    rows = rows[:n]
    tmap = collections.OrderedDict()
    for r in rows: tmap.setdefault(nxwiki.title_of(r[2], r[1]), []).append(r)
    print("  対象 %d 件 / %d タイトル" % (len(rows), len(tmap)))
    ext = nxwiki.extracts(list(tmap), intro=True, ua=UA)
    cand = []
    for t, lst in tmap.items():
        found = nxwiki.pref_findall(ext.get(t, ""))
        for r in lst:
            if found and r[3] not in found:
                cand.append({"qid": r[0], "label": r[1], "db": r[3], "wiki": found[:3], "title": t,
                             "loc_qid": r[4], "loc_label": r[5], "status": r[6], "pub": r[7],
                             "intro": (ext.get(t, "")[:150].replace("\n", " "))})
    print("  jawiki 不一致 = %d 件。Wikidata で交差検証する" % len(cand))
    wdp = wd_prefecture([c["qid"] for c in cand]) if cand else {}
    conf = hold = 0
    for c in cand:
        c["wd"] = wdp.get(c["qid"], "")
        if c["wd"] and c["wd"] in c["wiki"]:
            c["verdict"] = "confirmed"; conf += 1
        elif c["wd"] and c["wd"] == c["db"]:
            c["verdict"] = "db_ok(誤検出)"; hold += 1
        else:
            c["verdict"] = "hold(二系統不一致)"; hold += 1
    print("  %-11s %-20s %-6s %-10s %-10s %s" % ("QID", "名称", "DB", "jawiki", "Wikidata", "判定"))
    for c in cand:
        print("  %-11s %-20s %-6s %-10s %-10s %s%s"
              % (c["qid"], (c["label"] or "")[:20], c["db"], "/".join(c["wiki"])[:10],
                 c["wd"] or "-", c["verdict"], " ★公開中" if c["pub"] else ""))
        if c["verdict"].startswith("hold") or c["verdict"].startswith("db_ok"):
            print("        導入部: …%s…" % c["intro"][:120])
    print("  二系統一致(訂正確定) %d / 要確認 %d" % (conf, hold))
    con.close(); return cand

# ---------- §2 原因究明 ----------
def s2():
    con = sqlite3.connect(DB)
    bad = [c for c in R["cross"] if c["verdict"] == "confirmed"]
    print("  誤り %d 件の location 列の状態:" % len(bad))
    nq = sum(1 for c in bad if not c["loc_qid"])
    for c in bad[:12]:
        print("    %-11s %-18s loc_qid=%-10s loc_label=%s" % (c["qid"], (c["label"] or "")[:18],
              c["loc_qid"] or "None", c["loc_label"] or "None"))
    print("    location_qid が空 = %d / %d" % (nq, len(bad)))
    tot = con.execute("select count(*) from festivals where prefecture is not null and prefecture<>''").fetchone()[0]
    noloc = con.execute("select count(*) from festivals where prefecture is not null and prefecture<>'' "
                        "and (location_qid is null or location_qid='')").fetchone()[0]
    print("  全体: prefecture あり %d 件中 location_qid 空 %d 件 (%.0f%%)" % (tot, noloc, 100.0*noloc/max(1,tot)))
    print("  推定: location_qid が無い行の prefecture は名称推測で埋められた疑い。")
    print("  祇園/阿波踊り/よさこい/ねぷた を含み location_qid 空の件数:")
    for kw, p in (("祇園", "京都府"), ("阿波踊", "徳島県"), ("よさこい", "高知県"), ("ねぷた", "青森県"), ("天神祭", "大阪府")):
        n = con.execute("select count(*) from festivals where label_ja like ? and prefecture=? "
                        "and (location_qid is null or location_qid='')", ("%" + kw + "%", p)).fetchone()[0]
        m = con.execute("select count(*) from festivals where label_ja like ? and prefecture=?",
                        ("%" + kw + "%", p)).fetchone()[0]
        print("    %-8s -> %-5s  %d 件 (うち loc_qid 空 %d)" % (kw, p, m, n))
    con.close(); return {"noloc": noloc, "total": tot}

# ---------- §3 反映 ----------
def s3():
    import nxledger
    con = sqlite3.connect(DB)
    ok = [c for c in R["cross"] if c["verdict"] == "confirmed"]
    for c in ok:
        new = c["wd"]
        if APPLY:
            cur = con.execute("update festivals set prefecture=?, updated_at=? where qid=? and prefecture=?",
                              (new, TS, c["qid"], c["db"]))
            if cur.rowcount != 1: raise RuntimeError("CAS failed %s" % c["qid"])
            nxledger.put(con, tkey="pref|%s" % c["qid"], qid=c["qid"], ja=c["label"], old=c["db"], new=new,
                         verdict="apply", decided_at=TS, src="step71/PREFCHECK_v2",
                         note=("jawiki導入部=%s / Wikidata P131=%s の二系統一致。DB値 %s は名称由来の推測誤り。導入部: %s"
                               % ("/".join(c["wiki"]), c["wd"], c["db"], c["intro"][:200]))[:600],
                         url="https://ja.wikipedia.org/wiki/" + urllib.parse.quote(c["title"].replace(" ", "_")))
    if APPLY: con.commit()
    print("  訂正 %d 件 (APPLY=%s)" % (len(ok), APPLY))
    for c in ok: print("    %-11s %-20s %s -> %s" % (c["qid"], (c["label"] or "")[:20], c["db"], c["wd"]))
    con.close(); return [c["qid"] for c in ok]

KEY = "## [EXLIMIT_PREFCHECK_V2_20260811]"
BLOCK = KEY + """
取得関数の真因: prop=extracts は exintro を付けない全文取得だと exlimit が 1 に制限され、
20件バッチでは先頭1件しか返らない。step69 §3 の「本文なし23/25」はこれ。API 仕様を
読まずにバッチ設計したのが原因。全文取得は 1 件ずつ、導入部は exlimit=20 で 20 件まで。
県名検出の誤り: [一-龥]{2,3}県 は「2019年千葉県」を『年千葉県』と拾う。総称パターンを廃し
47都道府県の固定リストで走査する(nxwiki.pref_findall)。
単一情報源での断定を禁止する。jawiki 導入部と Wikidata P131/P276 の二系統が一致した時のみ
訂正を確定し、食い違えば hold。神戸ルミナリエ(DB=兵庫県が正)のような誤検出をこれで止める。
系統的誤りの発見: 下館/小見川/小鶴/桶川/氷見/山口の祇園祭=京都府、南越谷阿波踊り=徳島県、
坂戸よさこい=高知県、尾島ねぷた=青森県、山口天神祭=大阪府、浦安三社祭=東京都。
派生祭に本家の所在地を割り当てている。prefecture を名称から推測した工程が存在する疑い。
location_qid の有無との相関を §2 で検査する。
"""
def s4():
    import nxdoc
    try: nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError: nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    print("  key count = %d" % open(DOC, encoding="utf-8").read().count(KEY)); return {"ok": True}

sec("wiki", s0); sec("cross", s1); sec("cause", s2); sec("apply", s3); sec("doc", s4)
j = os.path.join(SNAP, "step71_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
