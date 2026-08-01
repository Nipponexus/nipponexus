# -*- coding: utf-8 -*-
"""detect_en_term_mismatch: JA固有名詞に対するEN訳語の食い違い検出。

設計原則(2026-07-27・実測に基づく):
  1) 辞書は「正しさの承認」に使わない。食い違いの検知のみ。緑は出さない。
     根拠=Wikipedia言語間リンクは 北海->North Sea / 梵天->Brahma / 屋台->Yatai(food cart)
     のように別語義を返す。承認に使うと95本目の致命エラーを追認してしまう。
  2) 任意抽出せず祭事ドメイン語に限定(多義語の暴発防止)。
  3) 発火はJA本文に該当語がある時だけ(条件付き発火)。
戻り値: (hit: bool, items: list[dict])
"""

# JA語 -> (期待されるEN表記の候補, 誤訳として禁止するEN表記)
# forbidden が EN に出たら即NG。expected が1つも無ければ WARN(要確認)。
TERM_TABLE = {
    # 110小樽=致命。国体は制度名。全日本スキー選手権(National Ski Championships)は別大会。
    "国体": (["National Sports Festival"],
             ["National Ski Championships", "All Japan Ski Championships"]),
    "国民体育大会": (["National Sports Festival"],
                     ["National Ski Championships", "National Athletic Meet Championships"]),
    # 87八戸=致命。打毬は馬上球技。流鏑馬(騎射)と別競技。
    "打毬": (["dakyu", "Dakyu", "ball game", "polo"],
             ["yabusame", "Yabusame", "horseback archery", "mounted archery"]),
    "流鏑馬": (["yabusame", "Yabusame", "horseback archery", "mounted archery"],
               ["dakyu", "Dakyu", "polo"]),
    # 95北海へそ祭り=致命。北海は北海道の略。海ではない。
    "北海": (["Hokkai", "Hokkaido"], ["North Sea", "Northern Sea"]),
    # 109梵天=祭具の梵天棒。仏教神Brahmaではない。
    "梵天": (["bonten", "Bonten"], ["Brahma", "Brahman", "Brahm"]),
    # 曳山/山車/山鉾は祭り屋台。food cartではない。
    "曳山": (["float", "Float"], ["food cart", "food stall"]),
    "山車": (["float", "Float"], ["food cart", "food stall"]),
    "山鉾": (["float", "Float"], ["food cart", "food stall"]),
    # ねぶた/ねぷたは固有名。lanternのみに潰さない。
    "ねぶた": (["Nebuta", "nebuta"], []),
    "ねぷた": (["Neputa", "neputa"], []),
}

# 文化財種別=文化庁分類の閉じた有限集合(辞書でなく定数表)
HERITAGE_TABLE = {
    "重要無形民俗文化財": (["Important Intangible Folk Cultural Property"],
                           ["Important Intangible Cultural Property",
                            "Tangible Folk Cultural Property"]),
    "重要有形民俗文化財": (["Important Tangible Folk Cultural Property"],
                           ["Intangible Folk Cultural Property"]),
    "記録作成等の措置を講ずべき無形の民俗文化財":
        (["Selected Intangible Folk Cultural Property",
          "Intangible Folk Cultural Property Selected"], []),
}


def _mask_expected(en, expected):
    """EN本文から期待語の出現を伏せ字化。
    禁止語が期待語の部分文字列である場合の誤検出を防ぐ。
    例: Important Intangible Folk Cultural Property は
        禁止語 Tangible Folk Cultural Property を内包する。"""
    masked = en
    for e in sorted(expected, key=len, reverse=True):
        masked = masked.replace(e, "\x00" * len(e))
    return masked


def _en_scope(ja, en, term):
    """JA側で term を含む段落に対応する EN 段落を返す。
    局所化の理由(2026-07-31・128ひろしまフラワーフェスティバル):
    JAが山車(=float)と屋台(=食の出店)を併用する題材で、文書全体の共起判定が
    正しい food stall を誤訳と判定した。両者は同じ##ブロック(見どころ)内の
    別の太字小見出しに属するため、ブロック単位では粗く段落単位まで下ろす。
    対応が取れない場合は None を返し、呼び出し側は文書全体を対象にする
    (フォールバックにより検出力は落とさない)。"""
    try:
        import pair_check as pc
        jb, eb = pc._blocks(ja), pc._blocks(en)
    except Exception:
        return None
    if not jb or len(jb) != len(eb):
        return None
    out = []
    for i, b in enumerate(jb):
        jtext = "\n".join(l for _, l in b[1])
        etext = "\n".join(l for _, l in eb[i][1])
        if term not in (b[0] or "") and term not in jtext:
            continue
        jp = [x for x in jtext.split("\n\n") if x.strip()]
        ep = [x for x in etext.split("\n\n") if x.strip()]
        if len(jp) > 1 and len(jp) == len(ep):
            out += [ep[k] for k, x in enumerate(jp) if term in x]
        else:
            out.append(etext)
    return "\n".join(out) if out else None


def _scan(ja, en, table):
    out = []
    for term, (expected, forbidden) in table.items():
        if term not in ja:
            continue
        scope = _en_scope(ja, en, term) or en
        # テーブル横断マスク(2026-08-01・偽陽性走査で判明):
        # 日立風流物やたてもん祭りは有形と無形の両方の指定を持ち、正しい
        # 「Important Tangible Folk Cultural Property」が無形側の禁止語
        # 「Tangible Folk Cultural Property」として拾われていた。自エントリの
        # 期待語だけでなく全テーブルの期待語をマスクしてから禁止語を探す
        # (82本目の還元C『正しいEN表記を機械適用で壊さない』のテーブル横断版)。
        # 条件付き横断マスク: 他エントリの期待語をマスクするのは、その語が
        # JA本文に実在する場合のみ。一律マスクすると『打毬の禁止語horseback
        # archeryは流鏑馬の期待語』のような相互参照で検出力が落ちる(回帰で捕捉)。
        all_expected = list(expected)
        for _tbl in (TERM_TABLE, HERITAGE_TABLE):
            for _t, (_e, _f) in _tbl.items():
                # 核語一致(2026-08-01): 犬山祭やたてもん祭りはJA側が
                # 「県指定有形民俗文化財」と書くためキー完全一致では
                # マスクが効かない。「有形民俗文化財」等の核部分で判定する。
                _core = _t.replace("重要", "")
                if _t != term and (_t in ja or (len(_core) >= 4 and _core in ja)):
                    # 接頭辞なし形も併せてマスク(2026-08-01): JAが「県指定有形民俗
                    # 文化財」の場合、EN側も Important を伴わない Tangible Folk
                    # Cultural Property と書かれるため、Important 付きだけを
                    # マスクしても禁止語判定を素通りできない。
                    all_expected += _e + [x.replace("Important ", "") for x in _e]
        probe = _mask_expected(scope, all_expected) if all_expected else scope
        bad = [f for f in forbidden if f in probe]
        if bad:
            out.append({"term": term, "level": "NG",
                        "reason": "誤訳語がEN本文に出現", "found": bad,
                        "expected": expected})
            continue
        if expected and not any(e in en for e in expected):
            out.append({"term": term, "level": "WARN",
                        "reason": "期待訳語がEN本文に不在(要確認)",
                        "found": [], "expected": expected})
    return out


def detect_en_term_mismatch(ja, en):
    items = _scan(ja, en, TERM_TABLE) + _scan(ja, en, HERITAGE_TABLE)
    hit = any(i["level"] == "NG" for i in items)
    return (hit, items)
