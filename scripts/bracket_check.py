# -*- coding: utf-8 -*-
"""還元(2026-08-02・135マウント・フジ): 出典装飾の残存を形式非依存で検出する。
   strip_bare_citations(113相模川)は中身がドメイン様の裸ブラケットのみを対象とするため、
   [出典名ラベル]形式が素通りし本文に残った(JA6/EN6)。形式を列挙して追う方針を捨て、
   strip後にブラケットが残っていること自体をNGとする。脚注[^1]と数字[1]は除外。
   偽陽性=底上げ済みdrafted全走査で実測する(設計上ゼロを維持できる前提の検査)。"""
import re

_BRACKET = re.compile(r'\[[^\]\[\n]{1,60}\]')
_FOOTNOTE = re.compile(r'^\[\^')
_NUMERIC = re.compile(r'^\[[\s\d,\-\u2013]*\]$')

def find(text):
    out = []
    t = text or ''
    for m in _BRACKET.finditer(t):
        s = m.group(0)
        if _FOOTNOTE.match(s) or _NUMERIC.match(s):
            continue
        out.append((t.count('\n', 0, m.start()) + 1, s))
    return out

def check(ja, en):
    """戻り値 (ng: bool, hits: [(side, line, snippet)])"""
    hits = []
    for side, txt in (('JA', ja), ('EN', en)):
        for ln, s in find(txt):
            hits.append((side, ln, s))
    return (len(hits) > 0, hits)


_URL = re.compile(r'https?://[^\s)\]"\u3000]+')
_PAREN_URL = re.compile(r'[（(]\s*https?://[^)）\s]+\s*[)）]')

def check_urls(ja, en):
    """還元(2026-08-02・勝山左義長): ブラケットを持たない出典残骸は形状で追えない。
       strip_bare_citationsが[ラベル](URL)の[ラベル]だけを消すと(URL)が孤児として残り、
       bracket_checkの射程外になる。本文にURLを置かないのはC-1の方針なので、
       『本文中のURL出現数がゼロ』という不変条件で検査する(形状に依存しない)。"""
    hits = []
    for side, txt in (('JA', ja or ''), ('EN', en or '')):
        for m in _URL.finditer(txt):
            hits.append((side, txt.count('\n', 0, m.start()) + 1, txt[max(0, m.start() - 40): m.end() + 5]))
    return (len(hits) > 0, hits)




_LABEL_URL = re.compile(r'(公式サイト|公式ウェブサイト|公式ポータル|公式情報源|公式HP|特設サイト|観光協会|実行委員会|Official Website|official website)')


def residual_urls(ja, en):
    """残ったURLを『ラベル付き(容認)』と『それ以外(要確認)』に分けて返す。"""
    out = []
    for side, txt in (('JA', ja or ''), ('EN', en or '')):
        for m in _URL.finditer(txt):
            head = txt[max(0, m.start() - 60): m.start()]
            out.append((side, txt.count('\n', 0, m.start()) + 1, bool(_LABEL_URL.search(head)), head[-40:] + m.group(0)[:40]))
    return out


_CITE_PAREN = re.compile(r'[ \t]?[（(]\s*https?://(?:[^)）\s]|\n){1,200}?\s*[)）\]］]')
_EMPTY_PAREN = re.compile(r'[（(][ \t]*[)）]')

def strip_citation_urls(text):
    """還元(2026-08-03): 空白の全域正規化はマークダウンの字下げを壊す(住吉の御田植で
       4スペース字下げの入れ子リストが1スペースになり入れ子が解けた)。除去は括弧付き出典URLの
       spanのみとし、直前の空白1個をパターンに含めて二重空白の発生源を断つ。本文の空白には触れない。"""
    t = _CITE_PAREN.sub('', text or '')
    return _EMPTY_PAREN.sub('', t)
