# -*- coding: utf-8 -*-
"""NXAPPLY_v3 (2026-08-10) 列挙型(translit_check)のPro確定を本文へ自動反映する。
還元: 272件が人手だったのは判定不能だからでなく run_one.py:103 の設計判断
「EN側の機械適用は成立しない」が改修後も見直されず残っていたため(能力差ではない)。
v3の変更: 同一誤表記が複数回出る場合は全置換する(誤りの反復であって曖昧さではない)。
newがoldを含む場合(Peace Memorial -> Peace Memorial Park)は先にnewをマスクし二重付与を防ぐ。
書込条件: verdict==confirmed_wrong / evidence_verified / old,new非空 /
oldが本文に1回以上MAXHIT以下 / 改行数不変。既定dry-run、実書込は NX_APPLY=1。"""
import os, re, sqlite3, datetime
DB = os.path.expanduser('~/nipponexus/data/sqlite/nipponexus.db')
ENUM_ONLY = ('translit_check',)
MAXHIT = 8
_MASK = '\x00'

def _ascii(s): return bool(re.fullmatch(r'[\x20-\x7e]+', s or ''))

def _pat(s):
    return (re.compile(r'(?<![A-Za-z])' + re.escape(s) + r'(?![A-Za-z])') if _ascii(s)
            else re.compile(re.escape(s)))

def _mask_new(new, text):
    if new and new in text:
        return text.replace(new, _MASK * len(new)), True
    return text, False

def _count(s, text):
    if not s or not text: return 0
    return len(_pat(s).findall(text))

def hits(old, new, text):
    masked, _ = _mask_new(new, text or '')
    return len(_pat(old).findall(masked))

def parse_target(t):
    ja = re.search(r'JA\[(.*?)\]', t or ''); en = re.search(r'EN\[(.*?)\]', t or '')
    sp = lambda m: [x.strip() for x in re.split(r'[、,/]', m.group(1)) if x.strip()] if m else []
    return sp(ja), sp(en)

def _extend_old(old, new, text):
    """newの末尾語が本文でoldの直後にある場合、oldをそこまで延長する。
    検出器のENトークンが末尾の一般名詞(River/Park/Station等)を落とす事象への決定的修復。
    例: old='Shichikashuku' new='Nanakita River' 本文'Shichikashuku River' -> old='Shichikashuku River'"""
    t = (new or '').split()
    if not t or not old or not text: return old
    tail = t[-1]
    if old.endswith(tail): return old
    m = re.search(re.escape(old) + r'(\s+)' + re.escape(tail) + r'\b', text)
    return old + m.group(1) + tail if m else old

_FUNCW = {'from','the','of','in','at','to','near','and','a','an','on','by','for','with','its','this'}
def _ja_terms(u):
    # TKEYFALLBACK_v1: payload直渡し等でexcerpt不在でもtkeyからJAを拾う
    # TKEYFALLBACK_v2: 本番のfixは 'target_excerpt' を持つ。取り零すと全件fail-closed。
    t = (u.get('excerpt') or u.get('target_excerpt') or u.get('target')
         or u.get('tkey') or u.get('key') or '')
    m = re.search(r'JA\[(.*?)\]', t)
    return [x.strip() for x in re.split(r'[、,]', m.group(1)) if x.strip()] if m else []
def _wd_labels(term):
    """WDLABEL_v2 2026-08-10: 関数名の総当たりで _wd_get(地名) を呼び ValueError を出していた。
    正規の wikidata_en_label のみを使い、URLはラベルとして扱わない。"""
    try:
        import pro_verify_loop as _p
        lab, url = _p.wikidata_en_label(term)
    except Exception:
        return []
    return [lab] if lab else []

def _norm(s):
    import unicodedata as _u
    s = _u.normalize('NFKD', s or '')
    s = ''.join(ch for ch in s if not _u.combining(ch))
    return re.sub(r'[^a-z0-9]', '', s.lower())
def _entity_ok(u, old, new):
    """oldとnewが同一対象を指すかを、JA側を正として検証する。
    2026-08-10: newの実在性しか見ていなかったため、首里城公園の誤対から
    Naminoue Umisora Park -> Naminoue Shrine の破壊的置換が通過した。"""
    # PHRASE_v1: 固有名は高々5語。文頭大文字で始まる文まるごとの書換が
    # 'oldが固有名でない'判定をすり抜けて計画到達した(Q11259476)。語数と句読点で落とす。
    if len(old.split()) > 5 or re.search(r'[.;:!?]', old):
        return False, 'oldが文・長句(固有名の是正ではない)'
    w0 = (old.split() or [''])[0]
    if _ascii(old) and (w0.islower() or w0.lower() in _FUNCW):
        return False, 'oldが固有名でない(句の書換は自動反映外)'
    terms = _ja_terms(u)
    # ENTITYSTRICT_v1: 抽出失敗でのfail-openを禁止(L83と方針を一致させる)
    if not terms: return False, 'JA側の語を抽出できず(未検証では反映しない)'
    labs = []
    for t in terms: labs += _wd_labels(t)
    # FAILCLOSED_v1 2026-08-10: 取得失敗と真の不在を区別できない。
    # throttlingで砦が黙って開くのを避け、ラベル未取得なら自動反映しない。
    if not labs: return False, 'JA側の公式英名を取得できず(未検証では反映しない)'
    n = _norm(new)
    for l in labs:
        if n and (n == _norm(l) or n in _norm(l) or _norm(l) in n): return True, ''
    return False, 'newがJA側の公式英名と不一致 JA=%s WD=%s' % (terms[:2], labs[:3])

def plan(qid, u, ja, en):
    det = (u.get('detector') or '')
    if det not in ENUM_ONLY: return None, 'enum型でない'
    if (u.get('verdict') or '') != 'confirmed_wrong': return None, 'verdict!=confirmed_wrong'
    if not u.get('evidence_verified'): return None, 'evidence未通過'
    old = (u.get('old') or '').strip(); new = (u.get('new') or '').strip()
    if not old or not new: return None, 'old/newが空(Proが本文位置を書けていない)'
    if old == new: return None, 'old==new'
    _ok, _why = _entity_ok(u, old, new)
    if not _ok: return None, _why
    if len(old) < (4 if _ascii(old) else 2): return None, 'oldが短すぎる'
    side = 'en' if _ascii(old) else 'ja'
    text = en if side == 'en' else ja
    _o0 = old; old = _extend_old(old, new, text)
    if old != _o0: print('[nxapply] old延長 %r -> %r' % (_o0, old))
    n = hits(old, new, text)
    if n == 0: return None, 'oldが本文に不在'
    if n > MAXHIT: return None, 'oldの出現が%d回=多すぎ' % n
    return {'qid': qid, 'side': side, 'old': old, 'new': new, 'n': n, 'detector': det}, 'ok'

def _sub(old, new, text):
    masked, used = _mask_new(new, text)
    out = _pat(old).sub(lambda m: new, masked)
    if used: out = out.replace(_MASK * len(new), new)
    return out

def _log(qid, det, target, action):
    try:
        c = sqlite3.connect(DB)
        c.execute("INSERT INTO gate_log(qid,detector,target,verdict,note,action,created_at)"
                  " VALUES(?,?,?,?,?,?,?)", (qid, det, (target or '')[:200], 'confirmed_wrong',
                  'NXAPPLY_v3', action[:300],
                  datetime.datetime.now().isoformat(timespec='seconds')))
        c.commit()
    except Exception as e:
        print('[nxapply] log失敗 %r' % (e,))

def _writer():
    try:
        import nx
    except Exception as e:
        return None, 'nx import失敗(%r)' % (e,)
    f = getattr(nx, 'write', None)
    return (f, 'ok') if callable(f) else (None, 'nx.writeが無い')

def _sql_write(qid, ja, en):
    c = sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS nxapply_backup(qid TEXT, ja TEXT, en TEXT, created_at TEXT)")
    cur = c.execute("SELECT manual_content_ja, manual_content_en FROM festivals WHERE qid=?", (qid,)).fetchone()
    c.execute("INSERT INTO nxapply_backup VALUES(?,?,?,?)", (qid, cur[0] if cur else None,
              cur[1] if cur else None, datetime.datetime.now().isoformat(timespec='seconds')))
    c.execute("UPDATE festivals SET manual_content_ja=?, manual_content_en=? WHERE qid=?", (ja, en, qid))
    c.commit(); return 'sql'

def apply_plans(qid, plans, ja, en):
    ja2, en2, done = ja, en, []
    for p in plans:
        if p['side'] == 'ja':
            if hits(p['old'], p['new'], ja2) == 0: continue
            ja2 = _sub(p['old'], p['new'], ja2)
        else:
            if hits(p['old'], p['new'], en2) == 0: continue
            en2 = _sub(p['old'], p['new'], en2)
        done.append(p)
    if not done: return ja, en, []
    if ja2.count('\n') != ja.count('\n') or en2.count('\n') != en.count('\n'):
        print('[nxapply] 改行数が変化=中止'); return ja, en, []
    import re as _re
    _DUPW = _re.compile(r'\b(\w+)\s+\1\b')
    for _a, _b in ((ja, ja2), (en, en2)):
        if len(_DUPW.findall(_b)) > len(_DUPW.findall(_a)):
            print('[nxapply] 置換で語重複が発生=中止(oldの語境界が不足)'); return ja, en, []
    if os.environ.get('NX_APPLY') != '1':
        for p in done:
            print('[nxapply][dry] %s %s x%d: %s -> %s' % (qid, p['side'], p['n'], p['old'], p['new']))
        return ja, en, []
    w, why = _writer()
    if w:
        w(qid, ja2, en2, old_ja=ja, old_en=en, allow_line_delta=0, mode='replace'); route = 'nx.write'
    else:
        print('[nxapply] %s / SQL直書き' % why); route = _sql_write(qid, ja2, en2)
    for p in done:
        _log(qid, p['detector'], p['old'], '自動反映(%s) x%d: %s -> %s' % (route, p['n'], p['old'], p['new']))
    print('[nxapply] %s 計画%d件 / 実書込%s 経路=%s' % (qid, len(done), ('あり' if os.environ.get('NX_APPLY')=='1' else 'なし(dry)'), route))
    return ja2, en2, done

def consume(qid, unresolved, ja='', en=''):
    if not unresolved: return unresolved
    cand, rest = [], []
    for u in unresolved:
        p, why = plan(qid, u, ja, en)
        if p: cand.append((p, u))
        else:
            if (u.get('detector') or '') in ENUM_ONLY:
                _log(qid, u.get('detector'), str(u.get('target_excerpt') or '')[:80], '自動反映せず: ' + why)
            rest.append(u)
    if not cand: return rest
    ja2, en2, done = apply_plans(qid, [p for p, _ in cand], ja, en)
    ok = {p['old'] for p in done}
    rest += [u for p, u in cand if p['old'] not in ok]
    return rest


# --- ROMAJI_TAIL_v1 : new が英語正式名でない(ローマ字一般名詞終わり)場合は却下 ---
import inspect as _insp
_ROMAJI_TAIL = ("jinja","jinjya","jingu","jinguu","taisha","tera","dera","ji",
                "gawa","kawa","yama","san","zan","koen","kouen","eki",
                "jo","jou","shiro","gu","in","an")
def _romaji_tail_bad(new, old=""):
    w = (new or "").strip().split()
    if len(w) < 2: return False
    tail = w[-1].lower().strip(".,")
    if tail not in _ROMAJI_TAIL: return False
    ow = (old or "").strip().split()
    return not (ow and ow[-1].lower() == tail)

_entity_ok_base = _entity_ok
def _entity_ok(*a, **k):
    try:
        b = _insp.signature(_entity_ok_base).bind(*a, **k); b.apply_defaults()
        old = b.arguments.get("old",""); new = b.arguments.get("new","")
    except Exception:
        old, new = "", ""
    if _romaji_tail_bad(new, old):
        print("[nxapply] 却下(ローマ字一般名詞): %r -> %r" % (old, new))
        return (False, "romaji_tail")
    return _entity_ok_base(*a, **k)
