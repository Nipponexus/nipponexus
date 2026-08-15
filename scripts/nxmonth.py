# NXMONTH_v1 (2026-08-15) date_rule を「仲裁役」として使う月確定。既存値の上書きはしない。
import json, re
_KAN={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'十一':11,'十二':12}
# date_rule が信用できない文脈（過去の暦・改暦前の記述を拾ったもの）
_STALE=re.compile(r'旧暦|以前は|かつて|明治以前|改暦|江戸時代まで')

def month_from_rule(rule, rjson=None):
    """(month|None, why)。date_rule 単体から月を読む。信用できない文脈なら None。"""
    if rjson:
        try:
            d=json.loads(rjson) or {}
            if _STALE.search(str(d.get('ctx') or '')): return None, 'stale-ctx'
            v=d.get('month')
            if isinstance(v,int) and 1<=v<=12: return v, 'json'
        except Exception: pass
    t=rule or ''
    if _STALE.search(t): return None, 'stale-rule'
    ms={int(m.group(1)) for m in re.finditer(r'(\d{1,2})月', t)}
    for m in re.finditer(r'([一二三四五六七八九]|十[一二]?)月', t):
        v=_KAN.get(m.group(1))
        if v: ms.add(v)
    ms={v for v in ms if 1<=v<=12}
    if len(ms)==1: return ms.pop(), 'rule'
    return None, ('multi:'+str(sorted(ms)) if ms else 'none')

def arbitrate(body_cands, rule_month):
    """本文推定の候補集合と規則の月から結論を出す。(month|None, why)
    仲裁(本文が割れた時に規則を採る)は既存168件で当たり18/外れ3と精度不足のため採用しない。
    割れたら必ず hold に落として人が見る。"""
    b=set(body_cands or [])
    if rule_month is None:
        return (b.pop(), 'body-only') if len(b)==1 else (None, 'no-rule')
    if not b: return rule_month, 'rule-only'
    if b=={rule_month}: return rule_month, 'agree'
    return None, 'conflict:body=%s rule=%s' % (sorted(b), rule_month)
