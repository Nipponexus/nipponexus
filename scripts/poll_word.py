"""ポーリング語句の自動選定(2026-07-31・128本目の偽陽性を受けた還元)。

背景: 118魚津と128フラワーフェスティバルで、旧本番にも存在する語をポーリングに使い
『反映していないのに反映したと誤認する偽陽性』を2度起こした。128では事前確認を
echoで表示しただけでゲートにせず素通りさせた。人が語を思いつく工程自体を廃止する。

方針: DBの新本文にあり、かつ現本番HTMLに不在の部分文字列をコードで選ぶ。
候補が1つも無い場合は非ゼロ終了し、投入者に判断を強制する(黙って進ませない)。
"""
import sqlite3, sys, urllib.request

DB = "/Users/openclaw_ks/nipponexus/data/sqlite/nipponexus.db"
UA = {"User-Agent": "Mozilla/5.0 (nipponexus poll-word picker)"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


def load(qid):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT slug_ja, slug_en, manual_content_ja, manual_content_en "
                "FROM festivals WHERE qid=?", (qid,))
    row = cur.fetchone()
    con.close()
    if not row:
        raise SystemExit("qid not found: %s" % qid)
    return row


def candidates(text, width):
    """本文を文単位に割り、各文の先頭からwidth文字の断片を候補にする。"""
    out = []
    for chunk in text.replace("\n", "。").split("。"):
        c = chunk.strip()
        if len(c) >= width and not c.startswith(("#", "-", "*")):
            out.append(c[:width])
    return out


def pick(new_text, live_html, width):
    for c in candidates(new_text, width):
        if new_text.count(c) == 1 and c not in live_html:
            return c
    return None


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: poll_word.py <qid>")
    qid = sys.argv[1]
    slug_ja, slug_en, ja, en = load(qid)
    ja_url = "https://nipponexus.com/%s/" % slug_ja
    en_url = "https://nipponexus.com/en/%s/" % slug_en
    ja_live, en_live = fetch(ja_url), fetch(en_url)
    w_ja = pick(ja, ja_live, 14)
    w_en = pick(en, en_live, 40)
    print("JA_URL=%s" % ja_url)
    print("EN_URL=%s" % en_url)
    print("JA_WORD=%r" % w_ja)
    print("EN_WORD=%r" % w_en)
    if not w_ja or not w_en:
        raise SystemExit("[NG] 新本文にあり現本番に不在の語が見つからない。"
                         "既に反映済みかDB未更新のいずれか。投入前に必ず解消する")
    print("[OK] 両言語の probe を確定")


if __name__ == "__main__":
    main()
