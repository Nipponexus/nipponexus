#!/usr/bin/env python3
# CLAIM_PROBE_v1 (2026-08-09)
# 目的: Pro照合ループへの入力を作る。「照合すべき主張」を型で抽出し、
# 検索クエリを《抽出済みエンティティ + 固定属性語》からのみ組む。
# 本文スライスは原理的にクエリへ入らない(provenance whitelist)。
import re, os, json, sqlite3

HOME = os.path.expanduser("~")
DB   = os.path.join(HOME, "nipponexus/data/sqlite/nipponexus.db")
TBL  = os.path.join(HOME, "nipponexus/data/muni_pref.json")
KINDS = ("NUM_PEOPLE","NUM_SHOP","NUM_PRICE","NUM_OTHER","EDITION","DATE","ORG","PLACE")
ATTR = {"NUM_PEOPLE":["来場者数"],"NUM_SHOP":["参加店舗数"],"NUM_PRICE":["料金"],
        "NUM_OTHER":["公式発表"],"EDITION":["開催日"],"DATE":["日程 公式"],
        "ORG":["主催"],"PLACE":["所在地 都道府県"]}
NUM  = re.compile(r"(?:約)?([0-9][0-9,，]{1,})\s*(万人|人|名|店舗|店|部|円|票|作品)")
EDIT = re.compile(r"第\s*([0-9]{1,3})\s*回")
DATE = re.compile(r"(20[0-9]{2})\s*年\s*([0-9]{1,2})\s*月")
PREFS = ["北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県","茨城県","栃木県","群馬県",
"埼玉県","千葉県","東京都","神奈川県","新潟県","富山県","石川県","福井県","山梨県","長野県","岐阜県",
"静岡県","愛知県","三重県","滋賀県","京都府","大阪府","兵庫県","奈良県","和歌山県","鳥取県","島根県",
"岡山県","広島県","山口県","徳島県","香川県","愛媛県","高知県","福岡県","佐賀県","長崎県","熊本県",
"大分県","宮崎県","鹿児島県","沖縄県"]
PREF_RE = re.compile("|".join(PREFS))
def _muni_re():
    k = sorted(load_tbl().keys(), key=len, reverse=True)
    return re.compile("|".join(map(re.escape, k))) if k else None
ORGN = re.compile(r"((?:公益財団法人|公益社団法人|一般財団法人|一般社団法人|特定非営利活動法人)?"
                  r"[^\s、。「」（）()はがをにでとも]{2,24}?"
                  r"(?:実行委員会|振興協会|協会|振興会|委員会|連合会|組合))")
def _norm_nums(t):
    t = t.replace("，", ",")
    t = re.sub(r"([0-9]+)万([0-9][0-9,]*)", lambda m: str(int(m.group(1))*10000+int(m.group(2).replace(",",""))), t)
    t = re.sub(r"([0-9]+)万(?![0-9])", lambda m: str(int(m.group(1))*10000), t)
    out = set()
    for x in re.findall(r"[0-9][0-9,]*", t):
        v = x.replace(",", "")
        if len(v) >= 3 and not (1800 <= int(v) <= 2100 and len(v) == 4): out.add(v)
    return out

def _ok(toks):
    "同語反復・包含・空トークンを排除"
    if len(toks) < 2: return False
    for i, a in enumerate(toks):
        for j, b in enumerate(toks):
            if i != j and a and (a in b): return False
    return True

def _q(parts):
    seen = []
    for t in parts:
        t = (t or "").strip()
        if t and t not in seen: seen.append(t)
    seen = seen[:4]
    return " ".join(seen), _ok(seen)

def load_tbl():
    return json.load(open(TBL, encoding="utf-8")) if os.path.exists(TBL) else {}

def extract(label, ja):
    "照合対象の主張を型で抽出。戻り値は Pro への作業指示 JSON"
    out, tbl = [], load_tbl()
    for i, raw in enumerate(ja.split("\n"), 1):
        s = raw.strip()
        if not s or s.startswith(("#", ">")): continue
        y = DATE.search(s)
        year = y.group(1) if y else None
        def add(kind, claim, parts):
            q, ok = _q(parts)
            out.append({"line": i, "kind": kind, "claim": claim, "query": q,
                        "query_ok": ok, "snippet": s[:110]})
        for m in NUM.finditer(s):
            u = m.group(2)
            k = ("NUM_PEOPLE" if u in ("人","名","万人") else
                 "NUM_SHOP" if u in ("店","店舗") else
                 "NUM_PRICE" if u == "円" else "NUM_OTHER")
            add(k, m.group(0), [label, (year + "年") if year else None] + ATTR[k])
        for m in EDIT.finditer(s):
            add("EDITION", m.group(0), [label, m.group(0)] + ATTR["EDITION"])
        for m in ORGN.finditer(s):
            org = m.group(1)
            add("ORG", org, ([org] if label in org else [label, org]) + ATTR["ORG"])
        mre = _muni_re()
        if PREF_RE.search(s) and mre:
            for m in mre.finditer(s):
                add("PLACE", m.group(0), [m.group(0)] + ATTR["PLACE"])
    return out

# ---- 決定論検出器 ----
def d9_muni_pref(ja):
    """9 市町村-都道府県の整合。県名が市町村の直前(15字以内・列挙区切りなし)、
    または直後の括弧内にある場合のみ判定する。並列列挙(『桑名市周辺の北勢地区や
    愛知県尾張地区』2026-08-09 石取祭FP)には沈黙する。"""
    tbl, ng, mre = load_tbl(), [], _muni_re()
    if not mre: return ng
    SEP = "、。，,;；・や及びおよびまた周辺近隣から"
    for i, raw in enumerate(ja.splitlines(), 1):
        s = raw.strip()
        for m in mre.finditer(s):
            mu = m.group(0); true = tbl.get(mu)
            if not true: continue
            head = s[:m.start()]; pm = None
            for p in PREF_RE.finditer(head): pm = p
            if pm:
                gap = head[pm.end():]
                if len(gap) <= 15 and not any(c in gap for c in SEP):
                    if pm.group(0) != true:
                        ng.append((i, mu, f"表={true} / 本文={pm.group(0)}"))
                    continue
            tail = s[m.end():m.end() + 10]
            t2 = PREF_RE.search(tail)
            if t2 and tail[:t2.start()].strip("（(「 ") == "" and t2.group(0) != true:
                ng.append((i, mu, f"表={true} / 本文={t2.group(0)}(括弧)"))
    return ng

def d10_end_kind(qid):
    "10 event_end.kind が banner() の辞書キーであること"
    if not os.path.exists(DB): return []
    con = sqlite3.connect(DB)
    try:
        r = con.execute("SELECT kind FROM event_end WHERE qid=?", (qid,)).fetchone()
    except sqlite3.OperationalError:
        return []
    if r and r[0] not in ("終了", "休止", "改称"):
        return [(0, "event_end.kind", f"{r[0]} は banner() 未対応(壊れた注記になる)")]
    return []

def d11_parity(ja, en):
    "11 JA/EN の有意数値・回次のパリティ(差異はWARN)"
    a, b = _norm_nums(ja), _norm_nums(en)
    w = []
    if a - b: w.append(("JA only", sorted(a - b)[:6]))
    if b - a: w.append(("EN only", sorted(b - a)[:6]))
    je = set(EDIT.findall(ja))
    ee = set(re.findall(r"([0-9]{1,3})(?:st|nd|rd|th)\s+(?:edition|annual|[A-Z])", en))
    if je and ee and je != ee: w.append(("回次不一致", [sorted(je), sorted(ee)]))
    return w

def run(qid, label, ja, en):
    cl = extract(label, ja)
    seen = set(); ded = []
    for c in cl:
        k = (c["kind"], c["claim"])
        if k in seen: continue
        seen.add(k); ded.append(c)
    return {"qid": qid, "claims": ded,
            "d9": d9_muni_pref(ja), "d10": d10_end_kind(qid), "d11": d11_parity(ja, en)}


# ===== QUERY_SANITIZER_20260810 =====
# 退化クエリ(「沖縄県那覇市 沖縄県」型)の根絶。原因は3つ:
#  (1) _ORG が自治体名/総称を団体名として拾う (2) 助詞食い込み「って実行委員会」
#  (3) 先頭欠け「縄エンタテインメント振興協会」
GENERIC_ORG = {"実行委員会", "委員会", "協会", "組合", "市町村", "各市町村", "国内主要都市",
               "主要都市", "事務局", "会場", "公園", "駅", "관", "地元", "関係者", "各地"}
_ORG_TAIL = re.compile(r"(協会|委員会|振興会|連合会|保存会|奉賛会|組合|財団|法人|会社|興業|"
                       r"神社|寺|市役所|町役場|観光局|事業団|放送|新聞社)$")
_FAC_TAIL = re.compile(r"(公園|ホール|会館|劇場|センター|ドーム|スタジアム|城|寺|神社|"
                       r"ビーチ|通り|広場|駅)$")
_EXPAND_OK = re.compile(r"[一-龥ァ-ヶーA-Za-z]")

def clean_term(term, src_line=""):
    """助詞食い込みを除去し、左方向へ最大8字まで語を復元する。"""
    t = re.sub(r"^[ぁ-ん\s、。，,・「」『』（）()]+", "", (term or "").strip())
    t = re.sub(r"[のをがはにでとやへ]$", "", t)
    if src_line and t:
        i = src_line.find(t)
        n = 0
        while i > 0 and n < 8 and _EXPAND_OK.match(src_line[i-1]):
            t = src_line[i-1] + t; i -= 1; n += 1
    return t

def term_role(t):
    """語の役割を返す: org / facility / None(照合に使わない)。"""
    tbl = load_tbl()
    if not t or len(t) < 4: return None
    if t in GENERIC_ORG: return None
    if t in tbl or t in PREFS: return None
    if re.fullmatch(r"[^\s]{0,4}[都道府県][^\s]{0,4}[市区町村]", t): return None
    if re.search(r"[市区町村]$", t) and not _ORG_TAIL.search(t): return None
    if _ORG_TAIL.search(t): return "org"
    if _FAC_TAIL.search(t): return "facility"
    return None

def query_ok(q, pref=""):
    """クエリの健全性。本文スライス混入と県名重複を弾く。"""
    if not q or len(q) > 40: return False
    if re.search(r"[。、「」『』（）]", q): return False
    if len(q.split()) > 4: return False
    if pref and q.count(pref) > 1: return False
    core = q.replace(pref, "").strip()
    if pref and (not core or core == pref): return False
    return True

def queries_for_block(label, pref, name, text):
    """ブロック本文から固有名詞+属性語のクエリだけを作る。本文スライスは一切通さない。"""
    ATTR = {"ORG": "主催", "NUMBER": "来場者数", "ATTEND": "来場者数",
            "DATE": "開催日", "EDITION": "開催日", "PLACE": "所在地", "FACILITY": "所在地"}
    out, seen = [], set()
    try:
        claims = extract(label, text) or []
    except Exception:
        claims = []
    order = {"ORG": 0, "NUMBER": 1, "ATTEND": 1, "DATE": 2, "EDITION": 3}
    for c in sorted(claims, key=lambda x: order.get(x.get("kind"), 9)):
        kind = c.get("kind"); raw = c.get("claim") or ""
        line = c.get("snippet") or text
        if kind in ("ORG", "PLACE", "FACILITY"):
            t = clean_term(raw, line)
            role = term_role(t)
            if not role: continue
            q = t + " 主催" if role == "org" else t + " " + pref + " 所在地"
        else:
            t = clean_term(raw, line)
            if not t: continue
            q = label + " " + t + " " + ATTR.get(kind, "")
        q = re.sub(r"\s+", " ", q).strip()
        if query_ok(q, pref) and q not in seen:
            seen.add(q); out.append(q)
    return out


# ===== QUERY_SANITIZER_V2_20260810 =====
# V1残存の3不具合を修正: (a)Markdown装飾混入「**問い合わせ**：〜」
# (b)料金/価格を照合対象にしていた「A料金5,000円」 (c)左方向復元の行き過ぎ「開催された第11回政府間委員会」
_DECOR = re.compile(r"[*_`#〜~]|^[\s]*[-・]\s*")
_LEAD_JUNK = re.compile(r"^(?:.*?[:：]|第\d+回|同|当|本|翌|各|全|約)")
_STOP_LEFT = re.compile(r"[ぁ-ん0-9０-９\s、。，,：:（）()「」*]")
_PRICE = re.compile(r"(円|ドル|料金|価格|チケット|席|\d+%|パーセント)")
_v1_clean, _v1_role = clean_term, term_role

def clean_term(term, src_line=""):
    t = _DECOR.sub("", (term or "")).strip()
    t = re.sub(r"^[ぁ-ん\s、。，,・「」『』（）()：:]+", "", t)
    t = re.sub(r"[のをがはにでとやへ]$", "", t)
    if src_line and t:
        i = src_line.find(t); n = 0
        while i > 0 and n < 8 and not _STOP_LEFT.match(src_line[i-1]):
            t = src_line[i-1] + t; i -= 1; n += 1
    t = _LEAD_JUNK.sub("", t).strip()
    return t

def term_role(t):
    if not t or _PRICE.search(t): return None
    if re.search(r"(政府間委員会|専門機関|事務局長)$", t): return None
    return _v1_role(t)

_v1_qok = query_ok
def query_ok(q, pref=""):
    if not q or _DECOR.search(q) or _PRICE.search(q.split(" ")[0]): return False
    return _v1_qok(q, pref)


# ===== QUERY_SANITIZER_V3_20260810 =====
# V2残存: 料金除外が term_role(ORG/PLACE系)にしか効かず、NUMBER系のelse分岐を素通りしていた
# (「kusatsu A料金5,000円」)。query_ok は先頭トークンしか見ていなかったため全体判定に変更。
_v2_qok = query_ok

def query_ok(q, pref=""):
    if not q: return False
    if _PRICE.search(q): return False          # 料金・価格・席種は照合対象外(単年変動)
    if re.search(r"[A-Za-z]料金|\d+[,，]\d{3}円", q): return False
    return _v2_qok(q, pref)
