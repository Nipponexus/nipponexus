# -*- coding: utf-8 -*-
"""ephemeral_src: 固有名が『単年マーカー付き出典にしか出ない』かを見る(還元W)。
日付トークンを含まない単年ネタ(TOTTEI PARK/京町筋/ポケモンコラボ)を捕捉する。
detect_future_ephemeral(本文の日付規則)では原理的に拾えない層を補う。"""
import re
_YEARMARK = re.compile(r'(?:第\s*\d{1,3}\s*回|20\d{2}年|20\d{2}\s*年度|令和\s*\d{1,2}\s*年)')

def check(names, docs):
    """names=本文から拾った固有名リスト, docs=[出典本文,...]。戻り値 (ng, lines)"""
    lines, ng = [], False
    for n in names:
        hit_docs = [d for d in docs if n in d]
        if not hit_docs:
            lines.append('  %-16s : 出典に不在(判定不能)' % n)
            continue
        marked = [d for d in hit_docs if _YEARMARK.search(d)]
        if len(marked) == len(hit_docs):
            ng = True
            lines.append('  %-16s : ×単年候補(出現%d件すべてが単年マーカー付き出典)' % (n, len(hit_docs)))
        else:
            lines.append('  %-16s : 恒常(単年マーカーなし出典に%d件出現)' % (n, len(hit_docs)-len(marked)))
    return ng, lines
