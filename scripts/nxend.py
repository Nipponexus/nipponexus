"""NXEND_v1: 終了・休止イベントの登録簿(既存schema非改変)"""
import re, sqlite3, datetime
DB = "data/sqlite/nipponexus.db"
DDL = """CREATE TABLE IF NOT EXISTS event_end(
 qid TEXT PRIMARY KEY, end_year INTEGER, kind TEXT,
 successor_qid TEXT, successor_label TEXT, note TEXT, created_at TEXT)"""
def _c():
    con = sqlite3.connect(DB); con.execute(DDL); return con
def mark(qid, end_year, kind="終了", successor_qid=None, successor_label=None, note=""):
    con = _c()
    con.execute("INSERT OR REPLACE INTO event_end VALUES(?,?,?,?,?,?,?)",
        (qid, end_year, kind, successor_qid, successor_label, note,
         datetime.datetime.now().isoformat(timespec="seconds")))
    con.commit(); con.close(); return {"qid": qid, "end_year": end_year, "kind": kind}
def get(qid):
    con = _c(); con.row_factory = sqlite3.Row
    r = con.execute("SELECT * FROM event_end WHERE qid=?", (qid,)).fetchone()
    con.close(); return dict(r) if r else None
def label(qid):
    r = get(qid)
    return f"{r['end_year']}年{r['kind']}" if r else None
def listing():
    con = _c(); con.row_factory = sqlite3.Row
    rs = [dict(x) for x in con.execute("SELECT * FROM event_end ORDER BY end_year DESC")]
    con.close(); return rs


END_NOTE = re.compile(r"(?:終了|休止|廃止)(?:し|され|して|となり|となっ)|現在は(?:開催|実施)されて(?:いない|いません)|過去のイベント|開催は行われて(?:いない|いません)")
END_NOTE_EN = re.compile(r"no longer held|discontinued|was (?:last )?held (?:in|until)|"
                         r"has (?:since )?ended|on hiatus", re.I)

def require_note(qid, ja, en):
    """NXEND_v1: event_end 登録済みの記事に終了注記が無ければNG。
    未登録qidは常にOK(既存236本に影響させない)。公式確認注記(継続前提)では
    代替不可 -- 終了イベントに『公式で最新をご確認ください』は誤誘導のため。"""
    r = get(qid)
    if not r:
        return False, []
    ng = []
    if not END_NOTE.search(ja or ""):
        ng.append(("JA", f"{r['end_year']}年{r['kind']}の注記なし"))
    if not END_NOTE_EN.search(en or ""):
        ng.append(("EN", f"{r['end_year']}年{r['kind']}の注記なし"))
    return (len(ng) > 0), ng


def banner(qid, lang="ja"):
    """NXEND_v1 追尾バナー。event_end 登録記事の冒頭に常時表示する。
    本文を書き換えずに現況を訂正できるため、終了年の判明・後継の変更に
    1行で追随できる。ただし検索スニペットには載らないため、開催継続の
    断定(毎年開催されています等)は本文側で直す必要がある(役割分担)。"""
    r = get(qid)
    if not r:
        return None
    y, k, suc = r["end_year"], r["kind"], r["successor_label"]
    if lang == "ja":
        t = {"終了": "このイベントは%d年をもって終了しています。" % y,
             "休止": "このイベントは%d年をもって休止しています。" % y,
             "改称": "このイベントは%d年に終了し、名称を改めて継続しています。" % y,
             }.get(k, "このイベントは%d年に%sしています。" % (y, k))
        if suc:
            t += "（現在の後継: %s）" % suc
        return "> **ご注意** " + t
    t = {"終了": "This event was discontinued in %d." % y,
         "休止": "This event has been on hiatus since %d." % y,
         "改称": "This event ended in %d and continues under a new name." % y,
         }.get(k, "This event ended in %d." % y)
    if suc:
        t += " (Successor: %s)" % suc
    return "> **Note** " + t


SCHED_ASSERT = re.compile(r"毎年開催されて|現在も(?:毎年)?(?:開催|実施)されて|継続して開催されて|"
                          r"今も(?:毎年)?(?:開催|実施)されて|例年[^。]{0,25}開催されています")
SCHED_ASSERT_EN = re.compile(r"is (?:still )?held annually|continues to be held|"
                             r"takes place (?:every|each) year", re.I)

def check_body(qid, ja, en):
    """NXEND_v1: 終了イベント本文の検査。2026-08-07の実測5件で確定した線引き。
    ★NG=開催スケジュールの現在形断定。検索スニペットに抜かれると
      クリック前に誤情報が届くため本文で直す必要がある。
    ★WARN=終了注記の不在。banner()が表示層で常時補うため停止不要。
    ★後継イベント名を含む文はNG対象外(TOKYO ILLUMILIAの現行開催記述は正しい)。
    評価・記憶の現在形(親しまれています等)は終了後も真であり一切触れない。"""
    r = get(qid)
    if not r:
        return False, [], []
    suc = r["successor_label"] or "\x00"
    ng = []
    for tag, txt, rx, sep in (("JA", ja or "", SCHED_ASSERT, "。"),
                              ("EN", en or "", SCHED_ASSERT_EN, ".")):
        for sent in txt.split(sep):
            if rx.search(sent) and suc not in sent:
                ng.append((tag, sent.strip()[:70]))
    warn = []
    if not END_NOTE.search(ja or ""):
        warn.append(("JA", "終了注記なし(バナーで補完)"))
    if not END_NOTE_EN.search(en or ""):
        warn.append(("EN", "終了注記なし(バナーで補完)"))
    return (len(ng) > 0), ng, warn
