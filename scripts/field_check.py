# -*- coding: utf-8 -*-
"""必須フィールドの存在検査(2026-08-03新設・141たけふ)
照合型検出器(authority_check)は本文に記述が有る場合のみ発火し、
記述が丸ごと無い=欠落を原理的に検出できない(141で主催の記載0件を素通り)。
真偽判定を伴わない純粋な存在検査なので決定論で書ける。
"""
import re
import os as _os
# 2026-08-08: 全国行事判定でDBを引くため。cwd非依存にする(nightly等から呼ばれるため)
_DB = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                    'data', 'sqlite', 'nipponexus.db')
_ORG_JA = re.compile(r'主催|主催者')
_ORG_EN = re.compile(r'\b(organiz|organis|hosted by|host(s)? the)', re.I)
# 電話番号を書かずに「公式で確認」と逃げるメタ的但し書き(130霧島/141たけふ)
_META_TEL = re.compile(r'電話番号[^。\n]{0,30}(公式|確認|割愛|記載しない)')
# 実番号が同一行にあれば「公式で確認」は補足であり欠落でない(新川市/黒崎で偽陽性)
_TEL_NUM = re.compile(r'0\d{1,4}[-(]\d{2,4}[-)]\d{3,4}')
# 神社主体の例祭はJAが「主催神社」と書きENは訳し方が異なる(多度/くらやみ/采女/潮来で偽陽性)
_ORG_SHRINE = re.compile(r'主催神社|主催[：:]\s*\S{0,12}(神社|大社|神宮|寺)')
_META_TEL_EN = re.compile(r'(telephone|phone)[^.\n]{0,40}(official (web)?site|omitted)', re.I)
_FIELDS = [('開催時期', r'開催時期|開催期間|会期|開催年|開催日'), ('開催場所', r'開催場所|会場|開催地|鑑賞スポット|観覧場所|実施場所'),
           ('料金', r'入場料|料金|観覧料|参加費|無料'), ('アクセス', r'アクセス|交通|最寄|駅|バス'),
           ('問い合わせ', r'問い合わせ|問合|連絡先')]

def run(qid, ja, en, inception=None):
    lines=[]; ng=False
    ja=ja or ''; en=en or ''
    ja_org=bool(_ORG_JA.search(ja)); en_org=bool(_ORG_EN.search(en))
    modern = (inception is not None and inception >= 1900)
    if not ja_org:
        if modern:
            ng=True; lines.append('[NG] 主催の記載なし(JA)=近代イベントで欠落。公式で主催団体を確認し明記する')
        else:
            lines.append('[WARN] 主催の記載なし(JA)=伝統祭事は神社等が主体のため許容')
    elif not en_org:
        if _ORG_SHRINE.search(ja):
            lines.append('[WARN] 主催が神社主体でENに organiz 系の語なし=訳し方の差として許容')
        else:
            ng=True; lines.append('[NG] 主催がJAのみでENに対応記述なし=日英ペア漏れ')
    else:
        lines.append('[OK] 主催 JA/EN 双方に記載')
    meta_tel=False
    for ln in ja.split('\n'):
        if _META_TEL.search(ln) and not _TEL_NUM.search(ln): meta_tel=True; break
    if not meta_tel and _META_TEL_EN.search(en) and not _TEL_NUM.search(en): meta_tel=True
    if meta_tel:
        ng=True; lines.append('[NG] 電話番号のメタ的但し書き(公式で確認/割愛)=実番号か記載なしのどちらかにする')
    # 2026-08-07: 終了イベント(event_end)は現行の料金・連絡先が存在しないため必須から外す。
    # 実測5件中4件が料金、3件が問い合わせでWARNを出しており、記事の欠陥ではない。
    # 開催時期は「かつていつ開催されたか」を書けるため除外しない(両国花火の欠落は実質的)。
    _skip = set()
    try:
        import nxend as _ne
        if _ne.get(qid):
            _skip = {'料金', '問い合わせ'}
    except Exception:
        pass
    # 2026-08-08: 全国行事(prefecture NULL)は特定会場が存在しないため開催場所を必須から外す。
    # 実測17件中6件(七五三/半夏生/新嘗祭/日本の七夕/裸祭り/初午)が該当。迎え火・送り火は
    # NULLだが会場記述を持ち検出できているため、除外による取りこぼしは生じない。
    try:
        import sqlite3 as _s
        _c=_s.connect(_DB); _r=_c.execute(
            'SELECT prefecture FROM festivals WHERE qid=?', (qid,)).fetchone(); _c.close()
        if _r and not (_r[0] or '').strip():
            _skip = _skip | {'開催場所'}
    except Exception:
        pass
    miss=[n for n,p in _FIELDS if n not in _skip and not re.search(p, ja)]
    if miss: lines.append('[WARN] 開催情報の項目が見当たらない: '+','.join(miss))
    return ng, lines
