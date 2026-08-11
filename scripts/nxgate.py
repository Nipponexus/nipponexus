# -*- coding: utf-8 -*-
"""未解決赤字の決定論トリアージ(2026-08-06)。判定はしない=『停止に値するか』だけを機械で決める。

原則: 停止には『検証された誤りの証拠』が要る。
 - judge=False の列挙型検出器(translit_check)は検出器自身が誤りと主張しない。
   そのProの修正案が evidence_gate を通らなければ、誰も誤りを立証していない → 停止しない(記録は残す)。
 - judge=True の判定型検出器は従来どおり停止させる(C-3b堅持)。

★no-op判定の厳格化: 初版は部分文字列一致で、候補 'Peace' が既存 'Peace Memorial Park' に含まれる
  だけで『対応済み』と誤判定した(146広島)。結論は偶然正しかったが理由が誤り。
  語境界一致 かつ 置換対象が不在 の場合のみ no-op とする。
"""
import os, re, sqlite3, datetime
DB = os.path.expanduser('~/nipponexus/data/sqlite/nipponexus.db')
ENUM_ONLY = ('translit_check',)
import nxallow  # NXALLOW_v1

def _log(qid, u, action):
    try:
        c=sqlite3.connect(DB)
        c.execute("INSERT INTO gate_log(qid,detector,target,verdict,note,action,created_at) "
                  "VALUES(?,?,?,?,?,?,?)",(qid,u.get('detector'),str(u.get('target_excerpt'))[:200],
                  str(u.get('verdict')),(str(u.get('note'))[:300]+' | keys='+str(sorted(u.keys()))),
                  action,datetime.datetime.now().isoformat(timespec='seconds')))
        c.commit()
    except Exception: pass

def _present(s, text):
    """ASCIIは語境界、日本語はそのまま。短すぎる候補は判定に使わない。"""
    if not s or not text or len(s) < 3: return False
    if re.fullmatch(r'[\x20-\x7e]+', s):
        return re.search(r'(?<![A-Za-z])'+re.escape(s)+r'(?![A-Za-z])', text) is not None
    return s in text

import re as _re

def triage(qid, unresolved, ja='', en=''):
    try:  # NXAPPLY_v2: 立証済みの列挙型は人手に回さず本文へ反映
        import nxapply
        unresolved = nxapply.consume(qid, unresolved, ja, en)
    except Exception as _e:
        print('[nxapply] skip: %r' % (_e,))
    keep=[]
    for u in (unresolved or []):
        det=(u.get('detector') or '')
        cand=(u.get('selected_candidate') or u.get('new') or '').strip()
        old=(u.get('target_excerpt') or u.get('old') or '').strip()
        body=(ja or '')+'\n'+(en or '')
        if _re.search(r'Pro照合失敗|OperationalError|DatabaseError|URLError|Timeout',
                      str(u.get('note') or '')+str(u.get('new') or '')):   # INFRA_SPLIT_v1
            _log(qid,u,'照合基盤の障害(内容の判定ではない)。停止しない'); continue
        if det in ENUM_ONLY:   # ORDER_FIX_v1 列挙型を先に判定(理由の取り違え防止)
            _log(qid,u,('列挙型: evidence通過だが本文位置を一意特定できず自動反映不可'
                        if u.get('evidence_verified')
                        else '列挙型かつevidence未通過=立証なし。停止しない')); continue
        if cand and _present(cand, body) and old and not _present(old, body):
            _log(qid,u,'no-op(候補が語境界で存在し置換対象は不在)'); continue
        if (u.get('verdict')=='unverifiable' and not u.get('evidence_verified')
                and old.startswith('[OK]')):   # UNVERIF_OK_v1 2026-08-11
            _log(qid,u,'検出器OK項目の確認不可=誤りの立証なし。停止しない'); continue
        if nxallow.is_allowed(qid, det, old):
            _log(qid,u,'人手却下(NXALLOW_v1)=偽陽性として通過'); continue
        keep.append(u)
    if len(keep)!=len(unresolved or []):
        print("[nxgate] 未解決%d件 → 停止対象%d件(除外分はgate_logへ)"%(len(unresolved or []),len(keep)))
    return keep

def recent(n=30):
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    return [dict(r) for r in c.execute("SELECT * FROM gate_log ORDER BY id DESC LIMIT ?",(n,))]

def stats():
    c=sqlite3.connect(DB)
    return c.execute("SELECT action,COUNT(*) FROM gate_log GROUP BY action ORDER BY 2 DESC").fetchall()
