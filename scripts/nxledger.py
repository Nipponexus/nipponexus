# -*- coding: utf-8 -*-
# LEDGER_v3 : verdict_ledger への書き込みは必ずこの関数経由。
# v2 からの変更 = (1) tkey 衝突は例外でなく upsert (2) 未知キーを黙って捨てない
import os, re as _re
_IDENT = _re.compile(r"^[a-z][a-z0-9_]{0,30}$")
ALLOW_EXT = {"tkey","qid","ja","en","old","new","verdict","wd_label","wd_url",
             "decided_at","src","note","url","evidence","excerpt","target_excerpt","status"}

def cols(con):
    return [r[1] for r in con.execute("pragma table_info('verdict_ledger')")]

def exists(con, tkey, new):
    c = cols(con)
    if "tkey" in c and "new" in c:
        return con.execute("select 1 from verdict_ledger where tkey=? and new=?",
                           (tkey, new)).fetchone() is not None
    return False

def ensure_cols(con, keys):
    """ALLOW_EXT の未知キーは列を足す。範囲外は例外。黙って捨てるのを禁止する。"""
    have = set(cols(con)); added = []
    for k in keys:
        if k in have:
            continue
        if k in ALLOW_EXT and _IDENT.match(k):
            con.execute("alter table verdict_ledger add column %s TEXT" % k)
            added.append(k); have.add(k)
        elif os.environ.get("NX_LEDGER_LAX") == "1":
            print("[LEDGER][WARN] dropped key: %s" % k)
        else:
            raise ValueError("unknown ledger key: %s (ALLOW_EXT に追加するか綴りを確認)" % k)
    return added

def put(con, **kv):
    """tkey 必須。既存 tkey は upsert。戻り値 = (使った列, 追加した列)"""
    if not kv.get("tkey"):
        raise ValueError("put() requires tkey")
    added = ensure_cols(con, list(kv))
    have = set(cols(con))
    keys = [k for k in kv if k in have]
    ph = ",".join("?" * len(keys))
    upd = [k for k in keys if k != "tkey"]
    tail = ("do update set " + ",".join("%s=excluded.%s" % (k, k) for k in upd)) if upd else "do nothing"
    con.execute("insert into verdict_ledger(%s) values(%s) on conflict(tkey) %s"
                % (",".join(keys), ph, tail), [kv[k] for k in keys])
    return keys, added
