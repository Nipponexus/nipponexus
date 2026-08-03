# -*- coding: utf-8 -*-
"""authority_check: 権威属性フィールドの固有名を出典本文と共起照合する(還元U)。
真偽は判定しない。『その団体名が出典に一度も出ないか』だけを決定論で見る。
対象は主催/共催/後援/問い合わせ/正式名称/文化財指定名に限定(多義語の暴発防止)。"""
import re

FIELDS_JA = ['主催','共催','後援','主管','問い合わせ','問合せ','正式名称','指定名称']
FIELDS_EN = ['Organizer','Co-organizer','Sponsor','Contact','Official name']
_ORG_TAIL = r'(?:実行委員会|委員会|協議会|協会|振興会|保存会|商工会議所|観光協会|振興協会|奉賛会|組合|連合会|神社|寺|市役所|市|町|村)'
_PRE = r'(?:株式会社|有限会社|一般社団法人|公益社団法人|一般財団法人|公益財団法人|特定非営利活動法人|NPO法人)'
_ORG = re.compile(_PRE + r'[ぁ-んァ-ヴ一-龥A-Za-zー・]{2,20}'
                  r'|[ぁ-んァ-ヴ一-龥ー]{2,20}(?:事務局|実行委員会)'
                  r'|[ぁ-んァ-ヴ一-龥ー]{2,20}' + _ORG_TAIL)

def _trim_particles(name):
    """助詞の巻き込みを除去。『の』は名称内に頻出(みなとの祭実行委員会)のため対象にしない。
       2026-08-02: 生HTML照合をやめた途端に『主催はこまねこまつり実行委員会』『日に浜島町観光協会』
       のような文頭巻き込みが×出典に不在として大量に出たため、漢字+助詞で終わる接頭を剥がす。
       『はままつ祭り実行委員会』のような名称先頭の助詞を壊さないよう、助詞の直前が漢字の場合に限る。"""
    name = re.sub(r'^.{0,8}?[一-龥][はがもをにでと](?=[ぁ-んァ-ヴA-Za-z一-龥])', '', name)
    name = re.sub(r'^.*?[はがも](?=[ァ-ヴA-Za-z一-龥])', '', name)
    name = re.sub(r'[でにをはがともへや、。]+$', '', name)
    return name

_JUNK = ('なか', 'という', 'ため', 'こと', 'もの', 'など', 'ほか', '以外', '以降', '以上',
         'した', 'する', 'され', 'れた', 'として', 'および', '場合', '構成')
_HEAD_NG = re.compile(r'^[はがもをにでとへやのりるれた、。・]')
_TAIL_ONLY = re.compile(r'^[市町村所寺社会]')
_PREFIX_NG = ('開催', '中心', '近隣', '地元', '同', '当', '本', '各', '全', '都', '終戦', '境内')
_JOINED = re.compile(r'(?<=[一-龥ァ-ヴ])と(?=[一-龥ァ-ヴ])')
_PARTICLE_TAIL = re.compile(r'[やとはがをに](?:市|町|村|所|会|社|寺)$')

_HIRA_OK = ()  # 廃止(下記_FRAG_HEADへ移行・patch_fileの定義消失ガードのため名前は残す)
# 2026-08-03・138姫路: 当初『頭が全ひらがななら断片』としたが、ひらがなの祭事名を持つ
# 正しい団体(ゆかたまつり奉賛会等)を落とした=82還元Cの『正しい表記を機械適用で破壊』の
# 再演。辞書で承認する設計をやめ、助詞・動詞活用で始まる断片という文法特徴で落とす。
_FRAG_HEAD = re.compile(r'^(して|され|した|する|とし|であ|になっ|により|による|という|といった|'
                        r'ながら|つつ|ため|ほか|など|また|そして|しかし|なお|ただ|より|から|まで)')


def plausible_org(name):
    """抽出崩れの断片を落とす(2026-08-02)。生HTML照合では『どこかに文字列がある』で
       通っていたため露呈しなかったが、本文抽出へ切替えたところ23本中9本(39.1%)が
       『終戦後の混乱のなかで市』『という特異な都市』のような断片で×になった。"""
    if len(name) < 3 or any(j in name for j in _JUNK):
        return False
    if _HEAD_NG.match(name) or _TAIL_ONLY.match(name):
        return False
    if any(name.startswith(p) for p in _PREFIX_NG):
        return False
    if _JOINED.search(name) or _PARTICLE_TAIL.search(name):
        return False
    # 2026-08-03・138姫路: 『して市』が末尾『市』のため通っていた(134で除去したはずの型)。
    # 組織名の頭が全てひらがなの断片を落とす(ひらがな自治体名は_HIRA_OKで保護)。
    if _FRAG_HEAD.match(name):
        return False
    return True

def extract_authority_orgs(ja):
    out = []
    for i, line in enumerate(ja.split('\n'), 1):
        if not any(f in line for f in FIELDS_JA):
            continue
        for m in _ORG.finditer(line):
            name = _trim_particles(m.group(0).lstrip('・-* 　'))
            if plausible_org(name):
                out.append((i, name))
    seen, uniq = set(), []
    for ln, n in out:
        if n not in seen:
            seen.add(n); uniq.append((ln, n))
    return uniq

def check(ja, sources_text, label=""):
    """sources_text = citesの出典本文を連結した文字列。戻り値 (ng, lines)。
       還元S(2026-07-29・120神戸): coreフォールバックの誤爆/誤殺を是正。
       coreが(1)3文字以上 (2)祭りlabelの部分文字列でない (3)地名のみでない、
       の全条件を満たす場合のみ証拠とする。
       『神戸まつり実行委員会』(core=神戸まつり=labelと一致)はフォールバック不可で
       full不在=×(正しく赤字)、『神戸商工会議所』(core=神戸=2文字かつ地名)も
       フォールバック不可=full不在=×(×だがPro照合で実在の正しい団体と判定される想定)。"""
    # 地名のみのcoreを弾く(都道府県+主要市・祭り開催地で頻出するもの)
    _PLACE = re.compile(r'^(神戸|東京|大阪|京都|名古屋|横浜|福岡|札幌|仙台|広島|那覇|神戸市|川崎|埼玉|千葉|堺|静岡|浜松|新潟|岡山|熊本|鹿児島|相模原|姫路|金沢|高松|松山|高知|長崎|大分|宮崎|青森|秋田|山形|福島|盛岡|水戸|宇都宮|前橋|甲府|長野|富山|福井|岐阜|大津|奈良|和歌山|鳥取|松江|山口|徳島|高知|佐賀|長野|富山|石川)$')
    orgs = extract_authority_orgs(ja)
    lines, ng = [], False
    if not orgs:
        return False, ['  権威属性の固有名: 抽出0件']
    for ln, name in orgs:
        hit = name in sources_text
        if not hit:
            core = re.sub(_ORG_TAIL + r'$', '', name)
            ok_core = (bool(core) and len(core) >= 3
                       and (not label or core not in label)
                       and not _PLACE.match(core))
            hit = ok_core and core in sources_text
        if hit:
            lines.append('  L%-3d %s : 出典に出現' % (ln, name))
        else:
            ng = True
            lines.append('  L%-3d %s : ×出典に不在(要一次照合・定型流し込みの疑い)' % (ln, name))
    return ng, lines


# --- 2026-08-02・133諏訪湖: 権威属性の『役割』共起照合(WARN専用) ---
# checkは団体名が出典に在るかしか見ないため、実在する団体に誤った役割を割り当てた
# 誤り(『諏訪市観光協会が協力している』=公式に不在の役割)を構造的に素通りさせた。
# 真偽は判定せず、記事が与えた役割語が出典で同じ団体と共起するかだけを見る。
ROLE_WORDS = ['主催', '共催', '後援', '主管', '協力', '協賛', '運営']

_ROLE_RE = re.compile('(' + '|'.join(ROLE_WORDS) + ')')

def authority_pairs(line):
    """役割語を起点に近接だけを見る(2026-08-02 v2)。v1は行内に役割語があると
       _ORGを行全体へ当てたため『広島県広島市』『愛川町』など平文の地名を拾い
       偽陽性47.8%になった。また『主催は諏訪市観光協会』のように役割が前置される
       列挙形を後方探索だけで解こうとして誤ペアリングしていた。
       採る形は2つに限定する: 『主催：X』『主催はX』(後置)と『Xが主催』(前置)。"""
    pairs, seen = [], set()
    for m in _ROLE_RE.finditer(line):
        role = m.group(1)
        name = None
        a = re.match(r'^[\s：:＝=はがのも、・\-]{0,3}(' + _ORG.pattern + ')',
                     line[m.end(): m.end() + 40])
        if a:
            name = a.group(1)
        else:
            before = line[max(0, m.start() - 40): m.start()]
            bm = list(_ORG.finditer(before))
            if bm and len(before) - bm[-1].end() <= 2:
                name = bm[-1].group(0)
        if not name:
            continue
        name = _trim_particles(name.lstrip('・-* 　'))
        if plausible_org(name) and (role, name) not in seen:
            seen.add((role, name))
            pairs.append((role, name))
    return pairs

def check_roles(ja, sources_text, window=80, skip_names=(), label=""):
    """記事が与えた役割語が、出典本文中の同じ団体名の近傍に現れるかを見る(WARN専用)。
       checkは団体名の存在しか見ないため、実在団体への誤った役割の割り当て
       (133諏訪湖『諏訪市観光協会が協力している』)を素通りさせた。真偽は判定しない。"""
    lines, warn = [], False
    if not sources_text:
        return False, ['  役割共起: 出典本文なしでスキップ']
    core_label = re.sub(r'(まつり|祭り|祭|大会|フェスティバル)$', '', label or '')
    seen = set()
    for i, line in enumerate(ja.split('\n'), 1):
        for role, name in authority_pairs(line):
            if name in skip_names or (name, role) in seen:
                continue
            seen.add((name, role))
            j = line.find(name)
            if j >= 0 and re.match(r'[^）]{0,10}内[）\)]', line[j + len(name): j + len(name) + 12]):
                lines.append('  L%-3d %s : 所在表記のため対象外' % (i, name))
                continue
            if role in ('主催', '運営') and name.endswith(('実行委員会', '委員会')) \
               and core_label and core_label[:3] in name:
                lines.append('  L%-3d %s = %s : 同義反復のためINFO' % (i, name, role))
                continue
            if name not in sources_text:
                lines.append('  L%-3d %s = %s : 名称不在(check側の担当)' % (i, name, role))
                continue
            ok = False
            for m2 in re.finditer(re.escape(name), sources_text):
                s0, s1 = max(0, m2.start() - window), min(len(sources_text), m2.end() + window)
                if role in sources_text[s0:s1]:
                    ok = True
                    break
            if ok:
                lines.append('  L%-3d %s = %s : 出典で共起' % (i, name, role))
            else:
                warn = True
                lines.append('  L%-3d %s = %s : ▲出典で役割が共起せず(要一次照合)' % (i, name, role))
    return warn, (lines or ['  役割共起: 対象なし'])
