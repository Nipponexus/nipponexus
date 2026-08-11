# -*- coding: utf-8 -*-
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
