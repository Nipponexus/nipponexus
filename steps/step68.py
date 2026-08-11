# -*- coding: utf-8 -*-
# step68 : jawiki 本文からの事実抽出の実効性を実測(読み取りのみ)。抽出できる/できないの線引きを出す。
import os, sys, re, json, time, sqlite3, datetime, collections, urllib.request, urllib.parse
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); SNAP = os.path.join(ROOT, "snapshots")
DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
UA = os.environ.get("NX_UA", "nipponexus/1.0 (contact: yuki.shiori@nexus-ds.jp)")
N = int(os.environ.get("NX_N", "30"))
sys.path.insert(0, SCR)

def fetch_extract(titles):
    url = ("https://ja.wikipedia.org/w/api.php?action=query&format=json&prop=extracts"
           "&explaintext=1&exintro=&redirects=1&titles=" + urllib.parse.quote("|".join(titles)))
    rq = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(rq, timeout=45) as f:
        d = json.loads(f.read().decode("utf-8"))
    return {p.get("title"): (p.get("extract") or "") for p in d.get("query", {}).get("pages", {}).values()}

# 抽出規則。いずれも「原文をそのまま根拠として残せる」ものだけ。
RX = {
 "開催日_確定日": re.compile(r"(\d{1,2})月(\d{1,2})日"),
 "開催日_序数曜日": re.compile(r"(\d{1,2})月(?:の)?第([一二三四五1-5])(日|月|火|水|木|金|土)曜日"),
 "開催日_旬": re.compile(r"(\d{1,2})月(上旬|中旬|下旬)"),
 "開催期間": re.compile(r"(\d{1,2})月(\d{1,2})日\s*(?:から|〜|～|-)\s*(?:(\d{1,2})月)?(\d{1,2})日"),
 "文化財": re.compile(r"(国|都|道|府|県|市|町|村)?(?:の)?(重要無形民俗文化財|無形民俗文化財|重要無形文化財|"
                    r"記録作成等の措置を講ずべき無形の民俗文化財|ユネスコ無形文化遺産)"),
 "所在地": re.compile(r"([\u4e00-\u9fa5]{2,4}[都道府県])([\u4e00-\u9fa5\u3040-\u30ff]{1,8}[市区町村])"),
 "神社仏閣": re.compile(r"([\u4e00-\u9fa5\u3040-\u30ff]{2,8}(?:神社|大社|神宮|八幡宮|寺|院))"),
}
def extract(text):
    out = {}
    for k, rx in RX.items():
        ms = list(rx.finditer(text))
        if ms:
            out[k] = [{"v": m.group(0), "ctx": text[max(0, m.start()-40):m.end()+40].replace("\n", " ")} for m in ms[:3]]
    return out

con = sqlite3.connect(DB)
EMPTY = ("(manual_content_ja is null or manual_content_ja='') and "
         "(manual_content_en is null or manual_content_en='')")
rows = con.execute("select qid,label_ja,wikipedia_ja,prefecture,start_month from festivals "
                   "where %s and status='pending' and wikipedia_ja is not null and wikipedia_ja<>'' "
                   "order by priority_score desc, qid limit ?" % EMPTY, (N,)).fetchall()
print("対象 %d 件" % len(rows))
titles, meta = [], {}
for qid, lj, wj, pref, sm in rows:
    t = urllib.parse.unquote(wj.rstrip("/").split("/")[-1]).replace("_", " ") if "/" in (wj or "") else (wj or lj)
    titles.append(t); meta[t] = (qid, lj, pref, sm)

pages = {}
for i in range(0, len(titles), 20):
    try:
        pages.update(fetch_extract(titles[i:i+20]))
    except Exception as e:
        print("  [warn] %r" % e)
    time.sleep(1.0)
print("取得 %d ページ" % sum(1 for v in pages.values() if v))

cnt = collections.Counter(); nolead = []
print("=" * 72)
for t, (qid, lj, pref, sm) in meta.items():
    txt = pages.get(t, "")
    if not txt:
        cnt["本文取得できず"] += 1; nolead.append((qid, lj, t)); continue
    cnt["本文あり"] += 1
    ex = extract(txt)
    date = [k for k in ex if k.startswith("開催")]
    if date: cnt["日付らしきもの検出"] += 1
    if "文化財" in ex: cnt["文化財表記"] += 1
    if "所在地" in ex: cnt["所在地"] += 1
    if not date: cnt["日付なし"] += 1
    print("%-11s %-22s lead=%d字 %s" % (qid, (lj or "")[:22], len(txt), "県=" + str(pref)))
    for k in ("開催期間", "開催日_確定日", "開催日_序数曜日", "開催日_旬", "文化財", "所在地"):
        if k in ex:
            print("    %-10s %s" % (k, " / ".join(x["v"] for x in ex[k])))
            print("      原文: …%s…" % ex[k][0]["ctx"][:90])
print("=" * 72)
print("集計 = %s" % dict(cnt))
n = cnt["本文あり"] or 1
print("  日付検出率 %.0f%% / 文化財 %.0f%% / 所在地 %.0f%%"
      % (100.0*cnt["日付らしきもの検出"]/n, 100.0*cnt["文化財表記"]/n, 100.0*cnt["所在地"]/n))
if nolead:
    print("  本文取得できず(タイトル解決の失敗 %d件):" % len(nolead))
    for x in nolead[:8]: print("    %-11s %-20s title=%s" % x)
con.close()
