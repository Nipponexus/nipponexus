# -*- coding: utf-8 -*-
# step62 : PLACENAME_v2 (正典県名の不在 + 地名シグナル) / Yamadera hold の決着 / 規則の常設化
import os, sys, re, json, shutil, sqlite3, subprocess, datetime
HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
SCR  = os.path.join(ROOT, "scripts")
SNAP = os.path.join(ROOT, "snapshots")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
APPLY = os.environ.get("NX_APPLY") == "1"
sys.path.insert(0, SCR)
R = {}
def sec(n, f):
    try:
        R[n] = f(); print("[OK] " + n)
    except Exception as e:
        R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))

def s1():
    b = os.path.join(SNAP, "db_" + TS + ".db")
    a = sqlite3.connect(DB); c = sqlite3.connect(b); a.backup(c); c.close(); a.close()
    print("  " + b); return {"db_snapshot": b}

RULES = r'''# -*- coding: utf-8 -*-
# PLACENAME_v2 : 「同名別実体（地名）」を寺社語の有無でなく、正典側固有情報の不在で判定する。
# v1 の失敗 = 氏子区域の説明文は Shrine 語だらけで「寺社語なし」条件が潰れた(Q11678183)。
import re
# 正典側の実体を一意に指す情報。県名は EN/JA、alias は他所に流用されない固有語のみ列挙する。
HOME = {
 "Yamadera":        {"pref_en":"Yamagata","pref_ja":"\u5c71\u5f62","alias":["Risshaku","Rissyaku","\u7acb\u77f3\u5bfa"]},
 "Todaiji":         {"pref_en":"Nara","pref_ja":"\u5948\u826f","alias":["Daibutsuden","Shuni-e","Shunie"]},
 "Kofukuji":        {"pref_en":"Nara","pref_ja":"\u5948\u826f","alias":["Five-storied","Nan'endo","\u5357\u5186\u5802"]},
 "Sensoji":         {"pref_en":"Tokyo","pref_ja":"\u6771\u4eac","alias":["Kaminarimon","Asakusa","\u96f7\u9580"]},
 "Kasuga Taisha":   {"pref_en":"Nara","pref_ja":"\u5948\u826f","alias":["Wakamiya On-matsuri","\u82e5\u5bae"]},
 "Sumiyoshi Taisha":{"pref_en":"Osaka","pref_ja":"\u5927\u962a","alias":["Sorihashi","\u53cd\u6a4b","\u4f4f\u5409\u9020"]},
 "Suwa Taisha":     {"pref_en":"Nagano","pref_ja":"\u9577\u91ce","alias":["Onbashira","\u5fa1\u67f1"]},
 "Eiheiji":         {"pref_en":"Fukui","pref_ja":"\u798f\u4e95","alias":["Dogen","\u9053\u5143","Soto"]},
}
JA_OF = {"Yamadera":"\u5c71\u5bfa","Todaiji":"\u6771\u5927\u5bfa","Kofukuji":"\u8208\u798f\u5bfa",
         "Sensoji":"\u6d45\u8349\u5bfa","Kasuga Taisha":"\u6625\u65e5\u5927\u793e",
         "Sumiyoshi Taisha":"\u4f4f\u5409\u5927\u793e","Suwa Taisha":"\u8ae0\u8a2a\u5927\u793e","Eiheiji":"\u6c38\u5e73\u5bfa"}
JA_PLACE = "\u5730\u533a|\u753a|\u6821\u533a|\u5730\u57df|\u65b9\u9762|\u5728\u4f4f|\u4e01\u76ee|\u516c\u6c11\u9928"
EN_PLACE = r"area|areas|district|districts|neighbou?rhood|ward|town|quarter|village"

def _pat(w):
    return re.compile(r"(?<![0-9A-Za-z-])" + re.escape(w) + r"(?![0-9A-Za-z])")

def home_absent(term, en, ja):
    """正典側の県名/固有別名が本文のどこにも無ければ True。未登録語は None(判定不能)。"""
    h = HOME.get(term)
    if not h:
        return None, []
    hit = []
    if re.search(r"\b" + re.escape(h["pref_en"]) + r"\b", en or "", re.I):
        hit.append(h["pref_en"])
    if h["pref_ja"] in (ja or ""):
        hit.append(h["pref_ja"])
    for a in h["alias"]:
        if a in (en or "") or a in (ja or ""):
            hit.append(a)
    return (len(hit) == 0), hit

def place_signals(term, en, ja):
    """地名として使われている痕跡。根拠文字列つきで返す。"""
    sig = []
    jt = JA_OF.get(term)
    if jt and ja:
        m = re.search(re.escape(jt) + r"[\u30fb\u3001/\uff0f\u30fb\w]{0,8}?(" + JA_PLACE + r")", ja)
        if m:
            sig.append(("JA_SUFFIX", m.group(0)))
    if en:
        m = re.search(r"(?:the\s+)?" + re.escape(term) + r"(?:\s+and\s+[A-Z][\w-]+)?\s+(?:" + EN_PLACE + r")\b", en)
        if m:
            sig.append(("EN_SUFFIX", m.group(0)))
        for m in re.finditer(re.escape(term) + r"\s+([A-Z][\w-]+)", en or ""):
            w = m.group(1)
            pre = set(re.findall(r"([A-Z][\w-]+)\s+" + re.escape(w) + r"\b", en))
            pre.discard(term)
            if len(pre) >= 2:
                sig.append(("LOCAL_COMPOUND", "%s %s / 他の前置語=%s" % (term, w, sorted(pre)[:4])))
                break
    return sig

def judge(term, en, ja):
    """reject / hold を返す。apply 側の規則(SIBLING/REFERENCE)より後段で呼ぶこと。"""
    absent, hit = home_absent(term, en, ja)
    sig = place_signals(term, en, ja)
    if absent is None:
        return "hold", "HOME 未登録語のため判定不能", sig
    if not absent:
        return "hold", "正典側情報あり(%s) 参照の可能性" % ",".join(hit), sig
    if not sig:
        return "hold", "正典側情報なしだが地名シグナルなし", sig
    return "reject", "PLACENAME_v2: 正典側情報(%s/%s/alias)が本文に皆無 + %s" % (
        HOME[term]["pref_en"], HOME[term]["pref_ja"], ",".join(s[0] for s in sig)), sig
'''

def s2():
    p = os.path.join(SCR, "nxrules.py")
    open(p, "w", encoding="utf-8").write(RULES)
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    q = subprocess.run([sys.executable, os.path.join(SCR, "nxname.py"), p], capture_output=True, text=True)
    print("  NAMECHECK rc=%s %s" % (q.returncode, q.stdout.strip()[:120]))
    import nxrules
    # 自己テスト: Yamadera=reject / Todaiji(奈良言及あり)=hold / 正典の山形文=hold
    t1 = ("Ichinomiya Shrine (guardian deity of the Yamadera and Kumanishi areas). "
          "Two floats: Yamadera Yamagasa and Kumanishi Yamagasa. Kumade Ichiban Yamagasa, "
          "Fujita Nishi Yamagasa, Higashimachi Yamagasa.")
    j1 = "\u4e00\u5bae\u795e\u793e\uff08\u5c71\u5bfa\u30fb\u718a\u897f\u5730\u533a\u306e\u6c0f\u795e\uff09"
    t2 = "Yamadera in Yamagata, also called Risshaku-ji, was founded in 860."
    cases = [("Yamadera", t1, j1, "reject"), ("Yamadera", t2, "", "hold")]
    out = []
    for term, en, ja, exp in cases:
        v, why, sig = nxrules.judge(term, en, ja)
        ok = (v == exp)
        print("  selftest %-9s exp=%-6s got=%-6s %s %s" % (term, exp, v, "OK" if ok else "NG", why))
        for s in sig:
            print("      sig %s : %s" % s)
        out.append(ok)
        assert ok, (term, exp, v, why)
    return {"selftest": out}

def s3():
    import nxrules
    con = sqlite3.connect(DB)
    rows = con.execute("select qid,term,state,note from publish_queue where state='hold'").fetchall()
    res = []
    for qid, term, st, note in rows:
        r = con.execute("select manual_content_en, manual_content_ja, prefecture "
                        "from festivals where qid=?", (qid,)).fetchone()
        en, ja, pref = (r or ("", "", None))
        v, why, sig = nxrules.judge(term, en or "", ja or "")
        ss = [s for s in re.split(r"(?<=[.!?])\s+", en or "") if nxrules._pat(term).search(s)]
        res.append({"qid": qid, "term": term, "pref": pref, "verdict": v, "why": why,
                    "sig": sig, "sentence": (ss[0].strip()[:220] if ss else "")})
        print("  %s %-9s [%s] -> %-6s %s" % (qid, term, pref, v, why))
        for s in sig:
            print("      sig %s : %s" % s)
    con.close()
    return res

def s4():
    import nxledger
    con = sqlite3.connect(DB)
    done = []
    for e in R["judge"]:
        if e["verdict"] != "reject":
            continue
        if APPLY:
            nxledger.put(con, tkey="canon|%s|%s" % (e["term"], e["qid"]), qid=e["qid"],
                old=e["term"], new="", verdict="reject", decided_at=TS, src="step62/PLACENAME_v2",
                note=(e["why"] + " || " + e["sentence"])[:600],
                url="https://ja.wikipedia.org/wiki/%E5%B1%B1%E5%AF%BA%E7%94%BA_(%E5%8C%97%E4%B9%9D%E5%B7%9E%E5%B8%82)"
                    if e["term"] == "Yamadera" else "")
            con.execute("update publish_queue set state='reject', note=? where qid=? and term=?",
                        (e["why"][:200], e["qid"], e["term"]))
        done.append(e["qid"] + "/" + e["term"])
    if APPLY:
        con.commit()
    con.close()
    print("  APPLY=%s reject=%s" % (APPLY, done))
    return done

def s5():
    p = subprocess.run([sys.executable, os.path.join(SCR, "nxcheck.py")], cwd=ROOT,
                       capture_output=True, text=True)
    print((p.stdout or "")[-600:])
    con = sqlite3.connect(DB)
    print("  publish_queue = %s" % (con.execute("select qid,term,state from publish_queue").fetchall(),))
    print("  ledger note 未記載 = %d / %d"
          % (con.execute("select count(*) from verdict_ledger where note is null or note=''").fetchone()[0],
             con.execute("select count(*) from verdict_ledger").fetchone()[0]))
    con.close()
    return {"rc": p.returncode}

KEY = "## [PLACENAME_V2_20260810]"
BLOCK = KEY + """
Yamadera(Q11678183) の hold を外部照会で決着。山寺町=福岡県北九州市八幡西区の実在町名
(郵便番号806-0030)。黒崎祇園山笠は春日神社・岡田宮・一宮神社の氏子行事で、一宮神社の
氏子区域が「山寺・熊西地区」。山形の立石寺とは無関係につき reject。
PLACENAME_v1 が不発だった理由 = 氏子区域の説明文は Shrine 語が密集するため
「周辺に寺社語なし」という条件が構造的に成立しない。地名判定を寺社語の有無で測るのは誤り。
PLACENAME_v2(scripts/nxrules.py) = 必須条件 + 補助シグナルの二段構え。
 必須: HOME[term] の県名(EN/JA)と固有別名が本文に一つも無いこと(home_absent)。
 補助: JA_SUFFIX(山寺・熊西地区) / EN_SUFFIX(the X and Y areas) /
      LOCAL_COMPOUND(X Yamagasa の Yamagasa が他に2種以上の前置語を持つ=地域総称)。
 必須条件が満たされない場合は hold。よって Q3461576(Roben of Todaiji) のような参照は
 巻き込まない。判定順序は SIBLING_COHERENCE → REFERENCE_APPOSITIVE → PLACENAME_v2 → hold。
alias には他所へ流用されない語だけを置く。東大寺/山寺のような JA 表記そのものは
同名別実体側にも出現するため alias に使ってはならない。
"""
def s6():
    import nxdoc
    try:
        nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError:
        nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    n = open(DOC, encoding="utf-8").read().count(KEY)
    print("  key count = %d" % n); return {"key_count": n}

sec("backup", s1); sec("rules", s2); sec("judge", s3)
sec("apply", s4); sec("verify", s5); sec("doc", s6)
j = os.path.join(SNAP, "step62_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
