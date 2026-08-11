# -*- coding: utf-8 -*-
# step70 : (1) 取得関数の欠陥修正+自己検証 (2) 県名突合を全1256件へ (3) 抽出の再測定
import os, sys, re, json, time, sqlite3, datetime, collections, urllib.request, urllib.parse
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); SNAP = os.path.join(ROOT, "snapshots")
DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
UA = os.environ.get("NX_UA", "nipponexus/1.0 (contact: yuki.shiori@nexus-ds.jp)")
sys.path.insert(0, SCR)
R = {}
def sec(n, f):
    try: R[n] = f(); print("[OK] " + n)
    except Exception as e: R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))

WIKI = r'''# -*- coding: utf-8 -*-
# WIKI_v1 : jawiki 取得。タイトルは必ず「要求した綴り」で引けること。
# 旧実装の欠陥 = redirects/normalized の逆引きが不完全で、intro なし呼び出しで取りこぼした。
import json, time, sys, urllib.request, urllib.parse
UA_DEFAULT = "nipponexus/1.0 (contact: yuki.shiori@nexus-ds.jp)"

def api(host, params, ua=None, timeout=45):
    url = "https://%s/w/api.php?%s" % (host, urllib.parse.urlencode(params))
    rq = urllib.request.Request(url, headers={"User-Agent": ua or UA_DEFAULT})
    with urllib.request.urlopen(rq, timeout=timeout) as f:
        return json.loads(f.read().decode("utf-8"))

def extracts(titles, intro=True, ua=None, batch=20, sleep=1.0, verbose=True):
    """要求タイトル -> 本文。redirects/normalized を辿って必ず元の綴りで返す。"""
    out = {t: "" for t in titles}
    for i in range(0, len(titles), batch):
        chunk = titles[i:i + batch]
        p = {"action": "query", "format": "json", "prop": "extracts", "explaintext": 1,
             "redirects": 1, "titles": "|".join(chunk)}
        if intro:
            p["exintro"] = 1
        try:
            d = api("ja.wikipedia.org", p, ua)
        except Exception as e:
            if verbose: print("  [warn] extracts %r" % e)
            time.sleep(2); continue
        q = d.get("query", {})
        by = {}
        for pg in q.get("pages", {}).values():
            by[pg.get("title")] = pg.get("extract") or ""
        alias = {}
        for r in (q.get("redirects") or []):
            alias[r["from"]] = r["to"]
        for nz in (q.get("normalized") or []):
            alias[nz["from"]] = nz["to"]
        for t in chunk:
            cur, seen = t, 0
            while cur in alias and seen < 5:
                cur = alias[cur]; seen += 1
            out[t] = by.get(cur, by.get(t, ""))
        if verbose:
            sys.stdout.write("\r  取得 %d/%d" % (min(i + batch, len(titles)), len(titles))); sys.stdout.flush()
        time.sleep(sleep)
    if verbose: print()
    return out

def title_of(wikipedia_url, label):
    if wikipedia_url and "/" in wikipedia_url:
        return urllib.parse.unquote(wikipedia_url.rstrip("/").split("/")[-1]).replace("_", " ")
    return wikipedia_url or label
'''

def s0():
    p = os.path.join(SCR, "nxwiki.py")
    open(p, "w", encoding="utf-8").write(WIKI)
    import subprocess
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    q = subprocess.run([sys.executable, os.path.join(SCR, "nxname.py"), p], capture_output=True, text=True)
    print("  NAMECHECK rc=%s" % q.returncode)
    import nxwiki
    # 自己検証: intro あり/なしで同じタイトル集合が同数取れること
    t = ["七尾港まつり", "黒船祭", "神嘗祭", "あばれ祭り", "京都三大祭り"]
    a = nxwiki.extracts(t, intro=True, ua=UA, verbose=False)
    b = nxwiki.extracts(t, intro=False, ua=UA, verbose=False)
    na = sum(1 for v in a.values() if v); nb = sum(1 for v in b.values() if v)
    for k in t:
        print("    %-12s intro=%4d字 full=%5d字" % (k, len(a[k]), len(b[k])))
    assert na == len(t) and nb == len(t), "取得漏れ intro=%d full=%d" % (na, nb)
    print("  自己検証 OK (step69 §3 の『本文なし』は取得関数の欠陥であり抽出性能ではない)")
    return {"intro": na, "full": nb}

# ---------- §1 県名突合 全件 ----------
PREF = re.compile(r"(北海道|(?:京都|大阪)府|東京都|[\u4e00-\u9fa5]{2,3}県)")
def s1():
    import nxwiki
    con = sqlite3.connect(DB)
    rows = con.execute("select qid,label_ja,wikipedia_ja,prefecture,status,"
                       "case when manual_content_ja is null or manual_content_ja='' then 0 else 1 end "
                       "from festivals where prefecture is not null and prefecture<>'' "
                       "and wikipedia_ja is not null and wikipedia_ja<>'' order by qid").fetchall()
    n = int(os.environ.get("NX_N", "0")) or len(rows)
    rows = rows[:n]
    print("  突合対象 %d 件" % len(rows))
    tmap = collections.OrderedDict()
    for qid, lj, wj, pf, st, pub in rows:
        tmap.setdefault(nxwiki.title_of(wj, lj), []).append((qid, lj, pf, st, pub))
    ext = nxwiki.extracts(list(tmap), intro=True, ua=UA)
    ok = miss = nodata = 0; bad = []
    for t, lst in tmap.items():
        found = list(dict.fromkeys(PREF.findall(ext.get(t, "") or "")))
        for qid, lj, pf, st, pub in lst:
            if not found:
                nodata += 1; continue
            if pf in found:
                ok += 1
            else:
                miss += 1
                bad.append({"qid": qid, "label": lj, "db": pf, "wiki": found[:3], "title": t,
                            "status": st, "published": pub,
                            "ctx": (ext.get(t, "")[:120].replace("\n", " "))})
    print("  一致 %d / 不一致 %d / 判定不能 %d  (不一致率 %.1f%%)"
          % (ok, miss, nodata, 100.0 * miss / max(1, ok + miss)))
    pub_bad = [b for b in bad if b["published"]]
    print("  うち公開済みページ(本文あり)の誤り = %d 件" % len(pub_bad))
    for b in bad:
        mark = "★公開中" if b["published"] else "      "
        print("  [!] %s %-11s %-22s DB=%-5s 本文=%s" % (mark, b["qid"], (b["label"] or "")[:22], b["db"], b["wiki"]))
    return {"ok": ok, "miss": miss, "nodata": nodata, "bad": bad}

# ---------- §2 抽出の再測定 ----------
RXD = {"序数曜日": re.compile(r"(\d{1,2})月(?:の)?第([一二三四五1-5])[週]?(?:の)?([日月火水木金土])曜日"),
       "期間": re.compile(r"(\d{1,2})月(\d{1,2})日\s*(?:から|〜|～|-|‐)\s*(?:(\d{1,2})月)?(\d{1,2})日"),
       "確定日": re.compile(r"(\d{1,2})月(\d{1,2})日"),
       "旬": re.compile(r"(\d{1,2})月(上旬|中旬|下旬)"),
       "月のみ": re.compile(r"(?:毎年|例年)\s*(\d{1,2})月")}
NEG = re.compile(r"(創建|創始|開始|第1回|第一回|初開催|設立|建立|以来|生まれ|没|落成|指定|повод)")
def s2():
    import nxwiki
    con = sqlite3.connect(DB)
    EMPTY = ("(manual_content_ja is null or manual_content_ja='') and "
             "(manual_content_en is null or manual_content_en='')")
    rows = con.execute("select qid,label_ja,wikipedia_ja from festivals where %s and status='pending' "
                       "and wikipedia_ja is not null and wikipedia_ja<>'' "
                       "and (label_ja like '%%祭%%' or label_ja like '%%まつり%%') "
                       "and label_ja not like '%%映画%%' and label_ja not like '%%音楽%%' "
                       "order by priority_score desc limit ?" % EMPTY,
                       (int(os.environ.get("NX_N3", "30")),)).fetchall()
    con.close()
    tmap = collections.OrderedDict()
    for q, l, w in rows:
        tmap.setdefault(nxwiki.title_of(w, l), []).append((q, l))
    print("  対象 %d タイトル(伝統祭らしきもの)" % len(tmap))
    ext = nxwiki.extracts(list(tmap), intro=True, ua=UA)
    hit = 0; none = []
    for t, lst in tmap.items():
        txt = ext.get(t, "")
        q, l = lst[0]
        if not txt:
            none.append((q, l, t)); continue
        got = None
        for k, rx in RXD.items():
            for m in rx.finditer(txt):
                if NEG.search(txt[max(0, m.start()-25):m.start()]):
                    continue
                got = (k, m.group(0), txt[max(0, m.start()-45):m.end()+45].replace("\n", " ")); break
            if got: break
        if got:
            hit += 1
            print("  %-11s %-18s %-6s %-12s …%s…" % (q, (l or "")[:18], got[0], got[1], got[2][:70]))
        else:
            print("  %-11s %-18s 日付なし(導入部%d字)" % (q, (l or "")[:18], len(txt)))
    print("  導入部から開催時期を取得 = %d / %d (%.0f%%)" % (hit, len(tmap), 100.0*hit/max(1, len(tmap))))
    if none: print("  本文取得できず %d 件 %s" % (len(none), none[:5]))
    return {"hit": hit, "n": len(tmap)}

KEY = "## [WIKI_V1_PREFCHECK_20260811]"
BLOCK = KEY + """
step69 §3 の「本文なし 23/25」は抽出性能ではなく取得関数の欠陥。redirects/normalized の
逆引きが不完全で、要求タイトルに戻せず空文字になっていた。同じ関数が §2 では 120/120
成功していた点が矛盾のサインだった。測定結果が極端な時はまず測定器を疑うこと。
WIKI_v1(scripts/nxwiki.py): alias を辿って必ず要求タイトルで返す。intro あり/なしの
両方で同数取得できることを自己検証してから使う。
県名突合(PREFCHECK): jawiki 導入部の県名表記と DB の prefecture を照合する。
標本120件で不一致3件(約3%)。下館祇園祭・会津田島祇園祭が京都府とされる系統誤り(祇園→京都)、
さいすくいが三重県(正=大分県)。照合先が明確で canary が効き、既存公開ページにも波及する。
綴り是正の玉が尽きた後、日次に流すべき実仕事はこれ。
"""
def s3():
    import nxdoc
    try: nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError: nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    print("  key count = %d" % open(DOC, encoding="utf-8").read().count(KEY)); return {"ok": True}

sec("wiki", s0); sec("pref", s1); sec("extract", s2); sec("doc", s3)
j = os.path.join(SNAP, "step70_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60); print("READ ONLY / snapshot=%s" % j)
