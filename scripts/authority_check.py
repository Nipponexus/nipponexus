# -*- coding: utf-8 -*-
"""authority_check: 権威属性フィールドの固有名を出典本文と共起照合する(還元U)。
真偽は判定しない。『その団体名が出典に一度も出ないか』だけを決定論で見る。
対象は主催/共催/後援/問い合わせ/正式名称/文化財指定名に限定(多義語の暴発防止)。"""
import re

FIELDS_JA = ['主催','共催','後援','主管','問い合わせ','問合せ','正式名称','指定名称']
FIELDS_EN = ['Organizer','Co-organizer','Sponsor','Contact','Official name']
_ORG_TAIL = r'(?:実行委員会|委員会|協会|振興会|保存会|商工会議所|観光協会|振興協会|奉賛会|組合|連合会|神社|寺|市役所|市|町|村)'
_ORG = re.compile(r'[一般社団法人|公益財団法人|財団法人|社団法人]*[ぁ-んァ-ヴ一-龥ー]{2,20}' + _ORG_TAIL)

def extract_authority_orgs(ja):
    out = []
    for i, line in enumerate(ja.split('\n'), 1):
        if not any(f in line for f in FIELDS_JA):
            continue
        for m in _ORG.finditer(line):
            name = m.group(0).lstrip('・-* 　')
            if len(name) >= 3:
                out.append((i, name))
    seen, uniq = set(), []
    for ln, n in out:
        if n not in seen:
            seen.add(n); uniq.append((ln, n))
    return uniq

def check(ja, sources_text):
    """sources_text = citesの出典本文を連結した文字列。戻り値 (ng, lines)"""
    orgs = extract_authority_orgs(ja)
    lines, ng = [], False
    if not orgs:
        return False, ['  権威属性の固有名: 抽出0件']
    for ln, name in orgs:
        hit = name in sources_text
        if not hit:
            core = re.sub(_ORG_TAIL + r'$', '', name)
            hit = bool(core) and len(core) >= 3 and core in sources_text
        if hit:
            lines.append('  L%-3d %s : 出典に出現' % (ln, name))
        else:
            ng = True
            lines.append('  L%-3d %s : ×出典に不在(要一次照合・定型流し込みの疑い)' % (ln, name))
    return ng, lines
