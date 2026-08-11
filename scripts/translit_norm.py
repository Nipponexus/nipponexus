"""TRANSLIT_NORM_20260810 rev3 — as_defects(kana版)出力の整形のみ。判定はしない。
rev2: 中黒U+30FB除外 / EN側は完全一致重複のみ除去。
rev4: ALWAYS(無条件)/GENERIC(要文脈)に二分・旧淀川は実在名につき除外
rev3: (1)語頭復元は『短い形が本文に単独出現しない』時だけ(阿佐ケ谷駅→南阿佐ケ谷駅の別駅化を封鎖)
      (2)復元は行政字(都道府県市区町村郡州)とバスを跨がない
      (3)_generic の直前文字を漢字/カタカナに限定(『市の中央公園』の誤判定)・中央公園をGENERICから除外"""
import re

ADMIN = re.compile(r'^(?:東京都立|都立|府立|県立|市立|東京都|北海道|京都府|大阪府|.{2,3}県|.{1,4}市|.{1,3}町)')
PREF = {'IC': re.compile(r'^.*?(?:自動車道|高速道路|バイパス|圏央道|道路)'),
        '駅': re.compile(r'^.*?(?:鉄道|電鉄|地下鉄|新交通|新幹線|バス|.{1,6}線)')}
BACK = re.compile(r'[\u4e00-\u9fff\u30a1-\u30fa\u30fc]')      # 中黒は含めない
STOP = set('都道府県市区町村郡州')                              # 復元はここを跨がない
HEAD = re.compile(r'[\u4e00-\u9fff\u30a1-\u30fa]')            # 一般語判定の直前文字
ALWAYS = {'史跡公園','都市公園','仏教寺','関連神社','有力神社','停車駅'}
GENERIC = {'水景公園','湖畔公園','城址公園','中央公園','太鼓橋'}
ENHEAD = {'Inside','Within','Information','Lower','Parent','Smart','Near','At','The','Main','Eight'}
SUFFIX = {'公園':'公園','駅':'駅','神社':'神社','寺':'寺','城':'城','川':'川','橋':'橋','IC':'IC'}

def _dedup_ja(ts):
    ts = list(dict.fromkeys(ts))
    return [t for t in ts if not any(t != u and t in u for u in ts)]

def _dedup_en(ts):
    return list(dict.fromkeys(ts))

def _standalone(t, body):
    """直前が漢字/カタカナでない出現が1つでもあれば、独立した固有名とみなす。"""
    for m in re.finditer(re.escape(t), body):
        if m.start() == 0 or not BACK.match(body[m.start()-1]): return True
    return False

def _strip(kind, t, body):
    for rx in (PREF.get(kind), ADMIN):
        if not rx: continue
        s = rx.sub('', t)
        if s != t and len(s) >= 3 and s in body: t = s
    return t

def _recover(t, body, kind):
    if _standalone(t, body): return t          # 単独で立つ名は伸ばさない
    best = t
    for m in re.finditer(re.escape(t), body):
        i, j = m.start(), m.start()
        while j > 0 and i - j < 4 and BACK.match(body[j-1]) and body[j-1] not in STOP: j -= 1
        cand = body[j:m.end()]
        if len(cand) > len(best) and cand.endswith(SUFFIX.get(kind, '')) \
           and not (set(cand[:len(cand)-len(t)]) & STOP) and 'バス' not in cand[:len(cand)-len(t)]:
            best = cand
    return best

def _generic(t, body, kind):
    if t in ALWAYS: return True
    if t.endswith('河川'): return True
    if t not in GENERIC: return False
    for m in re.finditer(re.escape(t), body):
        if m.start() and HEAD.match(body[m.start()-1]): return True
    return False

def normalize(kind, ja, en, ja_body, en_body):
    dropped, out = [], []
    for t in ja:
        t2 = _recover(t, ja_body, kind)
        if t2 != t: dropped.append(('語頭復元', t, t2))
        t3 = _strip(kind, t2, ja_body)
        if t3 != t2: dropped.append(('接頭辞', t2, t3))
        if _generic(t3, ja_body, kind):
            dropped.append(('一般語', t3, '')); continue
        if len(t3) >= 2: out.append(t3)
    e2 = []
    for x in en:
        w = x.split()
        if w and w[0] in ENHEAD and len(w) > 1:
            y = ' '.join(w[1:])
            if y in en_body: dropped.append(('EN先頭語', x, y)); x = y
        elif x in ENHEAD:
            dropped.append(('EN機能語', x, '')); continue
        e2.append(x)
    return _dedup_ja(out), _dedup_en(e2), dropped
