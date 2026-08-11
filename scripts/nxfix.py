"""nxfix : 台帳から訂正履歴ページを生成する。DB のみ参照、外部照会ゼロ。"""
import os, re, json, sqlite3, datetime

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
OUTD = os.path.join(ROOT, "out")

PUBLIC = ("PREF", "CITYCHAIN", "PLACENAME", "CANON", "DATEGUARD")

def kind_of(tkey):
    """tkey は PREFIX[...] と prefix|... の二形式がある。両方に対応する。"""
    return re.split(r"[\[|]", tkey or "", 1)[0].strip().upper()

VERDICT_JA = {"apply": "訂正済み", "confirmed_wrong": "誤りを確認",
              "reject": "掲載見送り", "hold": "保留", "hold_geo": "保留（所在地）"}

# 用語置換。この表が置換と検査の唯一の出典で、両者が食い違わない。
# 長い語を先に置く (jawiki導入部 は jawiki より前)。
JARGON = [
    ("jawiki導入部", "記事冒頭の記述"),
    ("jawiki", "日本語版ウィキペディア"),
    ("Wikidata", "ウィキデータ"),
    ("P131", "所在地の情報"),
    ("P276", "所在地の情報"),
    ("P837", "開催日の情報"),
    ("PLACENAME_v2", "同名地名の判別"),
    ("PLACENAME_v1", "同名地名の判別"),
    ("SIBLING_COHERENCE_v1", "同一文内の表記統一"),
    ("REFERENCE_APPOSITIVE_v1", "所属先を示す表記"),
    ("CITYCHAIN_v2", "市区町村からの照合"),
    ("CITYCHAIN", "市区町村からの照合"),
    ("JA_SUFFIX", "地名としての用法"),
    ("EN_SUFFIX", "地名としての用法"),
    ("LOCAL_COMPOUND", "地名としての用法"),
    ("alias", "別名"),
    ("concept:", "一覧記事："),
    ("conflict:", "日付の不一致："),
    ("lunar:", "旧暦基準："),
    ("review:", "確認待ち："),
    ("past:", "過去の記述："),
]

# 全文が定型のものは丸ごと差し替える (部分置換より読みやすい)
CURATED = [
    (r"二系統確認|二系統照合",
     "記事冒頭の記述とウィキデータの二経路で所在地を確認。旧来の値は祭りの名称から推測された誤り"),
    (r"市区町村.*(チェーン|経由)|CITYCHAIN",
     "記事本文から市区町村を特定し、その所属県を照合（祭りの名称は使用せず）"),
    (r"^concept:", "一覧・総称を扱う記事のため、個別の開催日としては掲載しない"),
    (r"^conflict:", "記事本文の実際の日付と、記載の開催規則が一致しないため掲載しない"),
    (r"^lunar:", "旧暦を基準とする日付のため、新暦への換算が必要。未対応のため掲載しない"),
    (r"^review:", "自動判定では確証が得られず、人による確認待ち"),
    (r"PLACENAME_v2", "同名の地名との取り違え。本文に本家所在地を示す語が一切なく、別地点と判断"),
    (r"REFERENCE_APPOSITIVE", "人物の所属先を示す表記のため、正式表記に統一"),
    (r"SIBLING_COHERENCE", "同一文中の他の寺社が正式表記のため、表記を統一"),
]

def sanitize(t):
    for a, b in JARGON:
        t = t.replace(a, b)
    return re.sub(r"\s{2,}", " ", t).strip()

def humanize(note):
    t = (note or "").strip()
    for pat, msg in CURATED:
        if re.search(pat, t): return sanitize(msg)
    return sanitize(t)

def jargon_left(text):
    """公開文面に内部語彙が残っていないか。JARGON と同じ表を使う。"""
    return [a for a, _ in JARGON if a in text]

def _qid(tkey, col):
    """qid 列が空でも tkey から復元する。DATEGUARD 系は列が空のまま記録された。"""
    if (col or "").strip(): return col.strip()
    m = re.search(r"Q\d+", tkey or "")
    return m.group(0) if m else None

def _qid(tkey, col):
    """qid 列が空でも tkey から復元する。DATEGUARD 系は列が空のまま記録された。"""
    if (col or "").strip(): return col.strip()
    m = re.search(r"Q\d+", tkey or "")
    return m.group(0) if m else None

def load():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    lab = {}
    for r in c.execute("SELECT qid,label_ja FROM festivals WHERE qid IS NOT NULL"):
        lab[r["qid"]] = r["label_ja"]
    out, seen = [], set()
    for r in c.execute("SELECT tkey,qid,ja,old,new,verdict,wd_label,wd_url,note,url "
                       "FROM verdict_ledger ORDER BY rowid"):
        k = kind_of(r["tkey"])
        if k not in PUBLIC: continue
        note = (r["note"] or "").strip()
        if note.startswith("LEGACY"): continue
        old, new = (r["old"] or "").strip(), (r["new"] or "").strip()
        if not note and not (old and new): continue
        # 重複判定は tkey を含める。qid が空でも別行が潰れない。
        key = (r["tkey"], old, new, note)
        if key in seen: continue
        seen.add(key)
        q = _qid(r["tkey"], r["qid"])
        name = lab.get(q) or r["ja"] or r["wd_label"] or q or "-"
        out.append({"kind": k, "qid": q, "name": name, "old": old, "new": new,
                    "verdict": r["verdict"], "note": note, "human": humanize(note),
                    "url": (r["url"] or r["wd_url"] or "").strip()})
    c.close(); return out

def _src(u):
    return "[出典](" + u + ")" if (u or "").startswith("http") else "-"

def _cell(s):
    return (s or "").replace("|", "／").replace("\n", " ")

def _tbl_fix(rs):
    L = ["| 対象 | 修正前 | 修正後 | 確認方法 | 出典 |", "|---|---|---|---|---|"]
    for r in rs:
        L.append("| " + _cell(r["name"]) + " | " + (_cell(r["old"]) or "-") + " | "
                 + (_cell(r["new"]) or "-") + " | " + _cell(r["human"])[:80] + " | " + _src(r["url"]) + " |")
    return L

def _tbl_hold(rs):
    L = ["| 対象 | 判定 | 理由 | 出典 |", "|---|---|---|---|"]
    for r in rs:
        L.append("| " + _cell(r["name"]) + " | " + VERDICT_JA.get(r["verdict"], r["verdict"] or "")
                 + " | " + _cell(r["human"])[:80] + " | " + _src(r["url"]) + " |")
    return L

def render(today=None):
    today = today or datetime.date.today()
    rows = load()
    fixed = [r for r in rows if r["verdict"] in ("apply", "confirmed_wrong")]
    held  = [r for r in rows if r["verdict"] not in ("apply", "confirmed_wrong")]
    loc = [r for r in fixed if r["kind"] in ("PREF", "CITYCHAIN")]
    nam = [r for r in fixed if r["kind"] in ("CANON", "PLACENAME")]
    etc = [r for r in fixed if r not in loc and r not in nam]
    L = ["# 訂正・検証の記録", "",
         "最終更新: " + today.isoformat() + " / 訂正 " + str(len(fixed)) + " 件・保留 " + str(len(held)) + " 件", "",
         "当サイトは掲載前に、記事本文とウィキデータという二つの経路で内容を照合しています。",
         "一方だけでしか裏が取れない場合は採用せず、保留として記録します。",
         "以下は、その照合で見つかった誤りと、確証が得られず掲載を見送った項目です。", ""]
    if loc:
        L += ["## 所在地（都道府県）の訂正（" + str(len(loc)) + "件）", "",
              "祭りの名称から所在地が推測され、実際とは異なる県が記録されていたものです。", ""] + _tbl_fix(loc) + [""]
    if nam:
        L += ["## 名称・表記の訂正（" + str(len(nam)) + "件）", ""] + _tbl_fix(nam) + [""]
    if etc:
        L += ["## その他の訂正（" + str(len(etc)) + "件）", ""] + _tbl_fix(etc) + [""]
    if held:
        L += ["## 掲載を見送った項目（" + str(len(held)) + "件）", "",
              "誤った情報を載せないため、確証が得られないものは公開していません。", ""] + _tbl_hold(held) + [""]
    body = "\n".join(L) + "\n"
    os.makedirs(OUTD, exist_ok=True)
    md = os.path.join(OUTD, "corrections.md")
    open(md, "w", encoding="utf-8").write(body)
    js = os.path.join(OUTD, "corrections.json")
    json.dump({"generated": today.isoformat(), "fixed": len(fixed), "held": len(held), "items": rows},
              open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return {"fixed": len(fixed), "held": len(held), "loc": len(loc), "name": len(nam),
            "jargon": jargon_left(body), "md": md}

if __name__ == "__main__":
    print(json.dumps(render(), ensure_ascii=False))
