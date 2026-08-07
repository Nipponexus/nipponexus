# -*- coding: utf-8 -*-
# NXALLOW_v1 (2026-08-07): 人が本文で確認して却下した赤字を gate_log に記録し、
# 同一 qid+detector+target の再出現時のみ停止を免除する。ガードの無効化ではない。
import os, sqlite3, datetime
DB = os.path.expanduser("~/nipponexus/data/sqlite/nipponexus.db")
ACTION = "ALLOW(人手却下)"

def _norm(s):
    return (str(s or "")).strip()[:200]

def allow(qid, detector, target, note=""):
    c = sqlite3.connect(DB)
    c.execute("INSERT INTO gate_log(qid,detector,target,verdict,note,action,created_at)"
              " VALUES(?,?,?,?,?,?,?)",
              (qid, detector, _norm(target), "human_rejected", _norm(note)[:300], ACTION,
               datetime.datetime.now().isoformat(timespec="seconds")))
    c.commit()
    return {"qid": qid, "detector": detector, "target": _norm(target), "action": ACTION}

def is_allowed(qid, detector, target):
    try:
        c = sqlite3.connect(DB)
        return c.execute("SELECT COUNT(*) FROM gate_log WHERE qid=? AND detector=? AND target=?"
                         " AND action=?", (qid, detector, _norm(target), ACTION)).fetchone()[0] > 0
    except Exception:
        return False

def listing(qid=None):
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    sql = "SELECT qid,detector,target,note,created_at FROM gate_log WHERE action=?"
    a = [ACTION]
    if qid: sql += " AND qid=?"; a.append(qid)
    return [dict(r) for r in c.execute(sql + " ORDER BY id DESC", a)]
