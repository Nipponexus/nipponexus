# -*- coding: utf-8 -*-
"""検出器 9/10 の実体。register() は fn(text, qid) で呼ぶため2引数固定。
lambda 不可(inspect.getsource がヒアドキュメント内 lambda を取れない / 2026-08-09)。"""
import os, sys, re, sqlite3
sys.path.insert(0, os.path.expanduser("~/nipponexus/scripts"))
import claim_probe as cp

KIND_OK = ("終了", "休止", "改称")
DB = os.path.expanduser("~/nipponexus/data/sqlite/nipponexus.db")
ENUM_LEAK = re.compile(r"(?:\d{4}年|年に)\s*(succeeded|discontinued|renamed|paused|suspended|ended|cancelled)")

def d9(text, qid=None):
    """9 市町村-都道府県の整合。県名が市町村の直前15字以内(列挙区切りなし)、
    または直後の括弧内にある場合のみ判定。並列列挙(石取祭 Q6080166 FP)には沈黙。"""
    return cp.d9_muni_pref(text or "")

def d10(text, qid=None):
    """10 終了注記の enum 崩れ。本文に『2024年succeeded』等の英語 enum が漏れた場合、
    または当該 qid の event_end.kind が banner() 非対応値(終了/休止/改称 以外)の場合に赤。"""
    hits = [m.group(0) for m in ENUM_LEAK.finditer(text or "")]
    if qid:
        con = sqlite3.connect(DB)
        try:
            r = con.execute("SELECT kind FROM event_end WHERE qid=?", (qid,)).fetchone()
        finally:
            con.close()
        if r and r[0] not in KIND_OK:
            hits.append("event_end.kind=" + str(r[0]))
    return hits
