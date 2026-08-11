"""JA漢字固有名とEN音写の対応を『列挙するだけ』の抽出器(2026-08-04)。
★判定しない。正誤の判断はProの検索接地に委ねる。
★理由=音写の正誤は音写距離/頻度/読み/提示型の4方式すべてで機械判定が不成立と実測で確定(02参照)。
  しかし『対応づけて並べる』工程は決定論で書ける。142三国花火でClaudeが手でやったのはこれだけ。
★種別語(駅/川/神社/寺/公園/橋/城/IC)を持つ固有名に限る=JA/EN双方に対応語があるため対応が構造的に決まる。
  任意の固有名を拾うと1本あたり中央値65件で面積が減らない(提示型の失敗)。本方式は中央値6件。
★2026-08-06: EN側で『From Hiroshima Station』→"From Hiroshima"、『Hibiya Line Hibiya Station』
  →"Line Hibiya" のように、直前の前置詞・路線語まで固有名として切り出していた。146広島で
  この断片をProへ投げ、Proが誤って修正案を出し、停止条件になった(自律駆動の律速)。
  先頭の機能語・交通事業者語を剥がす _clean_en を追加。判定はせず、列挙の質だけを直す。
"""
import re as _re
_JA_TAIL = [('城址公園','Park'),('城跡公園','Park'),('記念公園','Park'),('公園','Park'),
            ('神社','Shrine'),('大社','Shrine'),('八幡宮','Shrine'),('東照宮','Shrine'),('宮','Shrine'),
            ('寺','Temple'),('城','Castle'),('駅','Station'),('川','River'),('橋','Bridge'),
            ('美術館','Museum'),('博物館','Museum'),('会館','Hall'),('ホール','Hall'),
            ('海岸','Beach'),('海水浴場','Beach'),('湖','Lake'),('滝','Falls'),('池','Pond'),
            ('庭園','Garden'),('タワー','Tower'),('港','Port'),('通り','Street')]
_GEN_TAIL = _re.compile(r'\b(River|Park|Station|Shrine|Temple|Castle|Bridge|Museum|Hall|Beach|Lake|Falls|Garden|Tower|Port|Street|Pond)\b')
def _expected_tail(ja_term):
    """JA側の最右の接尾辞から、EN側に来るべき一般名詞を一意に決める。
    本文の出現順から推測すると 深谷駅→Fukaya Castle のような誤結合が起きるため。"""
    best, pos = None, -1
    for suf, en in _JA_TAIL:
        i = (ja_term or '').rfind(suf)
        if i > pos: best, pos = en, i
    return best
def _with_tail(tok, en, ja_term=''):
    """ENトークンが末尾一般名詞を落としている場合のみ、JA側から決まる尾に限って延長する。
    期待と違う尾しか本文に無ければ延長しない(現状維持=無害)。"""
    tok = (tok or '').strip()
    if not tok or not en: return tok
    if _GEN_TAIL.search(tok.split()[-1] if tok.split() else ''): return tok
    tail = _expected_tail(ja_term)
    if not tail: return tok
    m = _re.search(_re.escape(tok) + r'(\s+)' + tail + r'\b', en)
    return tok + m.group(1) + tail if m else tok


import re

JA_RE = {
 '駅':   re.compile(r'([一-龥ァ-ヴ]{2,8})駅'),
 '川':   re.compile(r'([一-龥ァ-ヴ]{2,6})川'),
 '神社': re.compile(r'([一-龥ァ-ヴ]{2,8})神社'),
 '寺':   re.compile(r'([一-龥ァ-ヴ]{2,8})寺'),
 '公園': re.compile(r'([一-龥ァ-ヴ]{2,8})公園'),
 '橋':   re.compile(r'([一-龥ァ-ヴ]{2,6})橋'),
 '城':   re.compile(r'([一-龥ァ-ヴ]{2,6})城'),
 'IC':   re.compile(r'([一-龥ァ-ヴ]{2,8})(?:IC|インターチェンジ)'),
}
EN_RE = {
 '駅':   re.compile(r'\b([A-Z][A-Za-z\-\u2019]{1,24}(?:\s+[A-Z][A-Za-z\-]{1,20})?)\s+Station\b'),
 '川':   re.compile(r'\b([A-Z][A-Za-z\-]{1,20})\s+River\b'),
 '神社': re.compile(r'\b([A-Z][A-Za-z\-\u2019]{1,24})\s+(?:Shrine|Jinja)\b'),
 '寺':   re.compile(r'\b([A-Z][A-Za-z\-\u2019]{1,24})\s+Temple\b'),
 '公園': re.compile(r'\b([A-Z][A-Za-z\-]{1,20}(?:\s+[A-Z][A-Za-z\-]{1,20})?)\s+Park\b'),
 '橋':   re.compile(r'\b([A-Z][A-Za-z\-]{1,20})\s+Bridge\b'),
 '城':   re.compile(r'\b([A-Z][A-Za-z\-]{1,20})\s+Castle\b'),
 'IC':   re.compile(r'\b([A-Z][A-Za-z\-]{1,24})\s+(?:Interchange|IC)\b'),
}

# JA側の抽出崩れ(種別語の直前が普通名詞)。正誤判定ではなく列挙ノイズの除去のみ。
_JA_NG = ('最寄', '各', '同', '当', '本', '複数', '臨時', '有料', '無料', '会場', '周辺', '河')
# 2026-08-05: 県名(神奈川/石川/香川/旭川市等)と広域道路の断片(圏央道相模原愛+川)を誤って
# 『川』として拾っていた。存在しない地名の確認をProへ投げるため過剰捕捉は害になる。
_PREF_KAWA = ('神奈', '石', '香')          # 神奈川県/石川県/香川県
_ROAD_FRAG = re.compile(r'(道|自動車|高速|国道)')  # 『央道相模原愛』型の断片

# EN側の先頭に紛れる機能語・交通事業者語。固有名の一部ではないので剥がす。
_EN_LEAD = ('From', 'To', 'At', 'In', 'On', 'Near', 'The', 'A', 'An', 'Via', 'By', 'And', 'Or',
            'Of', 'For', 'With', 'Around', 'Between', 'Through', 'After', 'Before', 'During',
            'Take', 'Walk', 'Board', 'Alight', 'Exit', 'Nearest',
            'JR', 'Line', 'Metro', 'Subway', 'Railway', 'Railways', 'Toei', 'Shinkansen',
            'Bus', 'Tram', 'Streetcar', 'Local', 'Express', 'Rapid', 'Limited')


def _drop_ja(kind, w):
    if w in _JA_NG or len(w) < 2: return True
    if kind == '川' and (w in _PREF_KAWA or _ROAD_FRAG.search(w)): return True
    return False


def _clean_en(w):
    """先頭の機能語・路線語を剥がす。剥がした結果が空/1字なら列挙しない(空文字を返す)。"""
    parts = w.split()
    while parts and parts[0] in _EN_LEAD:
        parts.pop(0)
    out = ' '.join(parts)
    return out if len(out) >= 2 else ''


def collect(ja, en):
    """種別ごとに {kind, ja[], en[]} を返す。判定は行わない。"""
    out = []
    for k in JA_RE:
        js = sorted({m for m in JA_RE[k].findall(ja or '') if not _drop_ja(k, m)})
        es = sorted({c for c in (_clean_en(m) for m in EN_RE[k].findall(en or '')) if c})
        if js or es:
            out.append({'kind': k, 'ja': js, 'en': es})
    return out


def size(rows):
    return sum(max(len(r['ja']), len(r['en'])) for r in rows)


def as_defects(ja, en):
    """Pro照合ループへ渡す形。judge=Falseで『判定済みの赤字ではない』ことを明示する。"""
    ds = []
    seen = set()
    for r in collect(ja, en):
        if not r['ja'] and not r['en']:
            continue
        # 2026-08-06(146広島): 駅と城など別種別から同一の JA/EN 組が出て同じ問いを二度Proへ投げ、
        # 『偽陽性』と『検証不能』の相反する答えが返った。非決定性の除去とPro呼数の削減。
        _k = ('、'.join(r['ja']), ', '.join(_with_tail(t, en, '、'.join(r['ja'])) for t in r['en']))
        if _k in seen:
            continue
        seen.add(_k)
        ds.append({
            'detector': 'translit_check',
            'judge': False,
            'kind': r['kind'],
            'target': 'JA[%s] / EN[%s]' % ('、'.join(r['ja']), ', '.join(_with_tail(t, en, '、'.join(r['ja'])) for t in r['en'])),
            'ask': ('JA本文の固有名とEN本文のローマ字表記が同一の対象を指し、'
                    'かつENの表記が公式表記と一致しているかを検索で確認せよ。'
                    '意味翻訳が正当な語(神社→Shrine等)は一致とみなす。'),
        })
    return ds


### NOISE_GUARD_v1 — EN空・3件以上の列挙はProで検証不能なので送らない
import re as _re
_JA_RE=_re.compile(r"JA\[(.*?)\]"); _EN_RE=_re.compile(r"EN\[(.*?)\]")
def _noise_reason(d):
    s=str(d)
    mj=_JA_RE.search(s); me=_EN_RE.search(s)
    if not mj or not me: return None
    ja=[x for x in _re.split(r"[、,\uff0f/\s]+", mj.group(1)) if x]
    en=[x for x in _re.split(r"[,\uff0f/]+", me.group(1)) if x.strip()]
    if not en: return "EN側が空(照合対象なし)"
    if len(ja)>2 or len(en)>2: return f"列挙JA{len(ja)}/EN{len(en)}件(一括では検証不能)"
    return None
_raw_as_defects = as_defects
def as_defects(*a, **k):
    out = _raw_as_defects(*a, **k)
    keep=[]
    for d in out:
        r=_noise_reason(d)
        if r: print(f"  [prefilter] Pro送信除外: {str(d)[:60]} | {r}")
        else: keep.append(d)
    return keep


# ===== PAIRWISE_ALIGN_20260810 =====
# 旧 collect() はJA/ENを全文から別々に集めて種別ごとに束ねるだけで、対応関係を作っていなかった。
# 結果 JA[圓徳、大和西大、東大…]/EN[Entoku-ji, Kannon, Kiyomizudera…] という塊をProへ渡し、
# 「本文に該当の記述が存在しない」等の unverifiable を量産(53件中19件・translit由来が大半)。
# また種別語の剥がし過ぎで実在しない語を生成していた(大和西大寺→『大和西大』、神田小川町→『神田小』、
# 千代田区立今川中学校→『千代田区立今』)。
# 新方式: (1)剥がし後の語が本文に単独で実在するか検証 (2)段落位置でJA/ENを対応付け
# (3)1対1で確定した組だけをProへ渡す。曖昧な組は送らない(検証不能な問いを投げない)。
import re as _re3

_SUFFIX = {'駅': '駅', '川': '川', '神社': '神社', '寺': '寺', '公園': '公園',
           '橋': '橋', '城': '城', 'IC': 'IC'}

def _ja_exists(ja, word, kind):
    """剥がした語+種別語が本文に実在し、かつ語の直前が漢字でない(=語頭が正しい)ことを確認。"""
    suf = _SUFFIX.get(kind, '')
    full = word + suf
    for m in _re3.finditer(_re3.escape(full), ja or ''):
        i = m.start()
        if i == 0 or not _re3.match(r'[一-龥ァ-ヴ]', (ja or '')[i-1]):
            return True
    return False

def _para_index(text, term):
    """termが最初に現れる段落番号。見つからなければ -1。"""
    for i, p in enumerate((text or '').split('\n')):
        if term and term in p:
            return i
    return -1

def collect_pairs(ja, en):
    """JA/ENを段落位置で対応付け、1対1で確定した組のみ返す。"""
    pairs = []
    for k in JA_RE:
        js = sorted({m for m in JA_RE[k].findall(ja or '')
                     if not _drop_ja(k, m) and _ja_exists(ja, m, k)})
        es = sorted({c for c in (_clean_en(m) for m in EN_RE[k].findall(en or '')) if c})
        if not js or not es:
            continue
        nj, ne = len(ja or '') or 1, len(en or '') or 1
        used = set()
        for j in js:
            pj = _para_index(ja, j + _SUFFIX.get(k, '')) / nj
            best, bd = None, 9.9
            for e in es:
                if e in used:
                    continue
                d = abs(_para_index(en, e) / ne - pj)
                if d < bd:
                    best, bd = e, d
            # 位置が近い(相対距離0.15以内)場合のみ対応確定
            if best and bd <= 0.15:
                used.add(best)
                pairs.append({'kind': k, 'ja': j + _SUFFIX.get(k, ''), 'en': best})
    return pairs

def as_defects_pairs(ja, en):
    """1語対1語の確定組だけをProへ。塊で投げない。"""
    ds, seen = [], set()
    for p in collect_pairs(ja, en):
        key = (p['ja'], _with_tail(p['en'], en, p['ja']))
        if key in seen:
            continue
        seen.add(key)
        ds.append({
            'detector': 'translit_check', 'judge': False, 'kind': p['kind'],
            'target': 'JA[%s] / EN[%s]' % (p['ja'], _with_tail(p['en'], en, p['ja'])),
            'ask': ('JA本文の固有名「%s」とEN本文の表記「%s」が同一対象を指し、'
                    'ENが公式表記と一致するかを検索で確認せよ。'
                    '意味翻訳が正当な語(神社→Shrine等)は一致とみなす。' % (p['ja'], _with_tail(p['en'], en, p['ja']))),
        })
    return ds


# ===== KANA_ALIGN_20260810 =====
# PAIRWISE_ALIGN(段落位置)は失敗: 東大寺<->Kofukuji, 清水寺<->Todaiji と総崩れになり、
# 「もっともらしく誤った組」を作る分だけ旧方式より有害だった。位置ではなく読みで突き合わせる。
# pykakasi で JA を hepburn 化し、EN 側の綴りと正規化比較(長音・促音・ハイフン・接尾辞を吸収)。
# 対応が付かない語は捨てる(検証不能な問いをProへ投げない)。
try:
    import pykakasi as _pkk
    _KKS = _pkk.kakasi()
except Exception:
    _KKS = None

_SUF_EN = {'駅': ('station',), '川': ('river', 'gawa', 'kawa'), '神社': ('shrine', 'jinja', 'taisha'),
           '寺': ('temple', 'ji', 'dera', 'in'), '公園': ('park', 'koen', 'kouen'),
           '橋': ('bridge', 'bashi', 'hashi'), '城': ('castle', 'jo', 'jou'), 'IC': ('interchange', 'ic')}

def _norm(s):
    s = (s or '').lower()
    s = _re3.sub(r"[^a-z]", "", s)
    s = s.replace('oh', 'o').replace('ou', 'o').replace('uu', 'u').replace('oo', 'o')
    s = s.replace('aa', 'a').replace('ee', 'e').replace('ii', 'i')
    return s

def _hep(ja_word):
    if not _KKS: return ''
    return _norm(''.join(x['hepburn'] for x in _KKS.convert(ja_word)))

def _match(ja_word, en_word, kind):
    """読みが一致するか。EN側の種別語(Temple/ji等)は落として比較する。"""
    a = _hep(ja_word)
    b = _norm(en_word)
    if not a or not b: return False
    for suf in _SUF_EN.get(kind, ()):
        if b.endswith(_norm(suf)) and len(b) > len(_norm(suf)) + 1:
            b = b[:-len(_norm(suf))]
    for x in (a, b):
        if not x: return False
    return a == b or a.startswith(b) or b.startswith(a)

def collect_pairs(ja, en):
    """読み一致でJA/ENを1対1対応。曖昧・不一致は返さない。"""
    pairs = []
    for k in JA_RE:
        js = sorted({m for m in JA_RE[k].findall(ja or '')
                     if not _drop_ja(k, m) and _ja_exists(ja, m, k)})
        es = sorted({c for c in (_clean_en(m) for m in EN_RE[k].findall(en or '')) if c})
        used = set()
        for j in js:
            core = j
            cands = [e for e in es if e not in used and _match(core, e, k)]
            if len(cands) == 1:
                used.add(cands[0])
                pairs.append({'kind': k, 'ja': j + _SUFFIX.get(k, ''), 'en': cands[0], 'status': 'matched'})
    return pairs

def unmatched_report(ja, en):
    """読みが一致しなかった語。誤訳・誤記の候補としてINFO扱いで見るためのもの。"""
    out = []
    for k in JA_RE:
        js = sorted({m for m in JA_RE[k].findall(ja or '')
                     if not _drop_ja(k, m) and _ja_exists(ja, m, k)})
        es = sorted({c for c in (_clean_en(m) for m in EN_RE[k].findall(en or '')) if c})
        mj = {p['ja'].replace(_SUFFIX.get(k, ''), '') for p in collect_pairs(ja, en) if p['kind'] == k}
        me = {p['en'] for p in collect_pairs(ja, en) if p['kind'] == k}
        for j in js:
            if j not in mj: out.append({'kind': k, 'side': 'JA', 'term': j + _SUFFIX.get(k, '')})
        for e in es:
            if e not in me: out.append({'kind': k, 'side': 'EN', 'term': e})
    return out


# ===== KANA_ALIGN_V2_20260810 =====
# 残存: 『サクラ公園』『上野駅公園』のような実在しない語。_ja_exists は種別語込みで見るため
# 「桜が咲く公園」「上野駅…公園」から切り出した偽の固有名を通していた。
# 対策: 語の直前が読点/助詞/句点/空白でない場合は固有名の先頭とみなさない。
_BOUND_OK = _re3.compile(r'[、。「」『』（）\s，,・:：]')
_JOSHI = ('の', 'は', 'が', 'を', 'に', 'で', 'と', 'や', 'へ', 'も', 'から', 'まで', 'る', 'た', 'い', 'く')
_v1_exists = _ja_exists

def _ja_exists(ja, word, kind):
    if not _v1_exists(ja, word, kind): return False
    suf = _SUFFIX.get(kind, '')
    full = word + suf
    for m in _re3.finditer(_re3.escape(full), ja or ''):
        i = m.start()
        if i == 0: return True
        prev = (ja or '')[i-1]
        if _BOUND_OK.match(prev): return True
        if prev in _JOSHI: return True
        if _re3.match(r'[一-龥ァ-ヴA-Za-z0-9]', prev): continue
        return True
    return False


# ===== COMMON_NOUN_GUARD_20260810 =====
# 残存する抽出ミスは全て『普通名詞+種別語』(母体神社/主催神社/主要駅/毎年両神社/以降神社/歴史公園)。
# ブラックリスト(_JA_NG)では追いつかないため、固有名詞らしさで判定する。
# 判定: 語が本文中で種別語なしに単独出現するか(固有名は「上野公園」だけでなく「上野」単独でも出る)、
# または既知の固有名パターン(地名接尾・カタカナ・旧国名等)を持つか。
_COMMON = ('母体', '主催', '主要', '毎年両', '以降', '歴史', '当該', '該当', '対象', '関係',
           '中心', '周辺', '近隣', '地元', '現地', '各種', '複数', '一部', '全体', '共同',
           '合同', '記念', '公式', '通常', '特別', '臨時', '有料', '無料', '最寄', '所在',
           '併設', '隣接', '同名', '別',  '新旧', '前後', '両', '本', '当', '同', '各')
_PROPER_HINT = _re3.compile(r'[ァ-ヴ]{3,}|[一-龥]{2,}(?:町|市|区|村|山|島|野|原|田|川|谷|坂|橋|台|丘|沢|浜)$')
_v2_exists = _ja_exists

def _ja_exists(ja, word, kind):
    if not _v2_exists(ja, word, kind): return False
    if word in _COMMON: return False
    for c in _COMMON:
        if word.startswith(c) and len(word) <= len(c) + 1: return False
    suf = _SUFFIX.get(kind, '')
    # 固有名なら種別語を伴わない単独出現があるか、固有名らしい形をしている
    bare = len(_re3.findall(_re3.escape(word) + r'(?!' + _re3.escape(suf) + r')', ja or ''))
    if bare > 0: return True
    if _PROPER_HINT.search(word): return True
    if len(word) >= 3: return True
    return False


# ===== MINLEN_BY_KIND_20260810 =====
# COMMON_NOUN_GUARD で東大寺/興福寺/清水寺(2字)が落ちた。寺社名は2字が標準で、
# 一律 len>=3 は誤り。種別ごとに最小長を設定し、普通名詞は _COMMON で個別に落とす。
_MINLEN = {'寺': 2, '神社': 2, '城': 2, '川': 2, '橋': 2, '駅': 2, '公園': 2, 'IC': 2}
_v3_exists = _ja_exists

def _ja_exists(ja, word, kind):
    if not _v2_exists(ja, word, kind): return False      # 語頭境界(V2)まで
    if word in _COMMON: return False
    for c in _COMMON:
        if word.startswith(c) and len(word) <= len(c) + 1: return False
    if len(word) < _MINLEN.get(kind, 2): return False
    return True


# ===== SWITCH_TO_KANA_20260810 =====
# 読み一致で機械確定した組(716件)はPro不要。両側に未対応が残った種別のみ送る(387件/22.1%)。
# NX_TRANSLIT_LEGACY=1 で旧方式へ戻せる。
def as_defects_kana(ja, en):
    ds = []
    byk = {}
    for u in unmatched_report(ja, en):
        d = byk.setdefault(u['kind'], {'JA': [], 'EN': []})
        d[u['side']].append(u['term'])
    for k, d in byk.items():
        if not (d['JA'] and d['EN']):
            continue          # 片側のみ=相手言語で言及なし。正常なので送らない
        # TRANSLIT_NORM_WIRED_20260810 判定はせず列挙の質だけを直す(接頭辞/一般語/EN機能語)
        try:
            import translit_norm as _tn
            d['JA'], d['EN'], _ = _tn.normalize(k, d['JA'], d['EN'], ja, en)
        except Exception:
            pass              # 整形は任意。失敗しても素の列挙で続行する
        if not (d['JA'] and d['EN']):
            continue          # 整形で両側一般語だけになった=検証不能
        if len(d['JA']) > 3 or len(d['EN']) > 3:
            continue          # 多対多は一括では検証不能
        ds.append({
            'detector': 'translit_check', 'judge': False, 'kind': k,
            'target': 'JA[%s] / EN[%s]' % ('、'.join(d['JA']), ', '.join(_with_tail(t, en, '、'.join(d['JA'])) for t in d['EN'])),
            'ask': ('JA本文の固有名とEN本文の表記が同一対象を指すか、'
                    'ENが公式表記かを検索で確認せよ。読み一致で機械確認済みの組は除外済みで、'
                    'ここには意味翻訳(平和公園→Peace Memorial Park等)と'
                    '訳語不整合の候補のみが含まれる。意味翻訳が正当なら一致とみなす。'),
        })
    return ds

_kana_prev = as_defects
def as_defects(ja, en):
    import os as _os
    if _os.environ.get('NX_TRANSLIT_LEGACY') == '1':
        return _kana_prev(ja, en)
    return as_defects_kana(ja, en)
