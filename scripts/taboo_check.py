#!/usr/bin/env python3
"""TABOO_v1 (2026-08-09): 禁忌語の混入検査。
照合型でも不在型でもない第三の型＝「その記事に書いてはいけない語」を見る。
真偽判定を含まない純粋な文字列検査なので決定論で書ける(93角館の判断軸)。

由来: 富田の石取祭(Q11457148)で、鉦の擬音に祇園祭の「コンチキチン」が使われ、
8つの検出器すべてがOKを出したまま公開に到達した。照合型は「書かれた固有名を
出典と突合する」ため、固有名でない誤用語には原理的に沈黙する。
"""
import re

# (禁忌語, 許可する記事の条件, 理由) 条件はラベル/本文に含まれるべき語
GLOBAL = [
    ("コンチキチン", ["祇園祭", "京都"], "祇園祭の鉦の擬音。他の祭りの囃子に流用しない"),
    ("ソイヤ", ["神輿"], "神輿の掛け声。山車・曳山行事には用いない"),
    ("エンヤー", ["神輿", "曳山"], "掛け声の流用に注意"),
]

# 混同されやすい同名・類似名の祭り。qid単位で「出てはいけない語」を持つ。
PAIRS = {
    "Q11457148": (["春日神社", "町屋川", "比与利", "員弁川", "聖武天皇社"],
                  "桑名/松原の石取祭の由緒。富田は虫送り＋祭車が由来"),
    "Q30925738": (["四谷", "新宿区", "八坂神社", "祇園社"],
                  "東京四谷の須賀神社・京都祇園社との混同。対象は岡崎市樫山町"),
    "Q11406993": (["御杖", "飯南", "半夏祭り"],
                  "同名の別行事(半夏祭り/ハンゲショウ群生地)との混同"),
}

def check(qid, ja, en="", label=None):
    """禁忌語の混入を返す。戻り値 (ng: bool, hits: list[dict])

    許可条件はラベル(祭りの名前)で判定する。本文照合にすると、
    須賀神社大祭(Q30925738)のように『かつては祇園祭として6月に行われていた』と
    正当に書いてある記事で許可語が成立し、禁忌語が素通りする(実データで判明)。
    labelがNoneならDBから引く。"""
    hits = []
    body = ja + "\n" + (en or "")
    if label is None:
        try:
            import sqlite3, os
            c = sqlite3.connect(os.path.expanduser("~/nipponexus/data/sqlite/nipponexus.db"))
            r = c.execute("SELECT label_ja FROM festivals WHERE qid=?", (qid,)).fetchone()
            c.close(); label = (r[0] if r else "") or ""
        except Exception:
            label = ""
    for word, allow_if, why in GLOBAL:
        if word in body:
            if any(a in label for a in allow_if):
                continue
            hits.append({"word": word, "level": "NG", "scope": "global", "why": why})
    words, why = PAIRS.get(qid, (None, None))
    if words:
        for w in words:
            if w in body:
                hits.append({"word": w, "level": "NG", "scope": qid, "why": why})
    return (any(h["level"] == "NG" for h in hits), hits)

def report(qid, ja, en="", label=None):
    ng, hits = check(qid, ja, en, label)
    lines = ["9 禁忌語の混入     : " + ("NG" if ng else "OK")]
    for h in hits:
        lines.append("     %s [%s] %s (%s)" % (h["word"], h["level"], h["why"], h["scope"]))
    return ng, lines

if __name__ == "__main__":
    # 回帰: 由来となった実データで再現するか
    t = [("Q30925738", "かつては祇園祭として6月に行われた。鉦がコンチキチンと鳴る", "", True,
          "★実データ由来: 本文に祇園祭があっても許可しない(ラベル照合)"),
         ("Q30925738", "かつては祇園祭として6月に行われていた", "", False,
          "★実データ由来: 祇園祭の言及だけなら正当"),
         ("Q11457148", "鉦が「コンチキチン」と鳴る", "", True, "富田の擬音誤用=今回の由来"),
         ("Q1074485",  "祇園祭の鉦がコンチキチンと鳴る京都の夏", "", False, "祇園祭なら正当"),
         ("Q11457148", "町屋川の石を春日神社に納める", "", True, "桑名の由緒の接ぎ木"),
         ("Q11457148", "鉦の音はゴンチキチキと響く", "", False, "正しい擬音は通る"),
         ("Q30925738", "東京四谷の総鎮守として知られる", "", True, "別の須賀神社との混同"),
         ("Q30925738", "岡崎市樫山町の須賀神社で山車が曳かれる", "", False, "正しい対象は通る"),
         ("Q11406993", "御杖村のハンゲショウ群生地", "", True, "同名別物"),
         ("Q99999999", "何の変哲もない本文", "", False, "未登録qidは素通り")]
    ok = 0
    LAB = {"Q1074485": "祇園祭", "Q30925738": "須賀神社大祭", "Q11457148": "富田の石取祭",
           "Q11406993": "半夏生", "Q99999999": ""}
    for qid, ja, en, want, note in t:
        got, _ = check(qid, ja, en, LAB.get(qid, ""))
        mark = "PASS" if got == want else "FAIL"
        ok += got == want
        print("%s %s / %s" % (mark, note, qid))
    print("回帰 %d/%d" % (ok, len(t)))
