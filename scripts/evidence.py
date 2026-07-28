"""還元P(2026-07-28・117伊勢えび祭): 『非検出を不在の証拠にしない』を戒めでなくゲートにする。
117でClaudeは公式頁の本文抽出に年表が無いことを根拠に『DeepSeekの捏造』と誤診した(実際は
crawlerが年表テーブルを落としただけ)。同型が同日4系統(crawler本文抽出/Pro抜粋2割/生文字列
カウントEN0/エスケープ\\')。→不在主張は単一経路では成立させない。"""
import re

def absent(term, sources, min_sources=2):
    """termが『存在しない』と主張する前に必ず通す。sources={経路名:実出力}。
       経路が min_sources 未満、または どれか1経路でも検出したら AssertionError。"""
    if not isinstance(sources, dict) or len(sources) < min_sources:
        raise AssertionError(
            f"[不在主張NG] '{term}': 経路{len(sources) if isinstance(sources,dict) else 0}件では"
            f"不在を主張できない(最低{min_sources}経路の実出力が要る)")
    hits = {}
    for name, text in sources.items():
        t = (text or "")
        n = t.count(term)
        if n:
            m = re.search(re.escape(term), t)
            hits[name] = repr(t[max(0, m.start()-60):m.end()+60])
        print(f"  [経路] {name}: {n}件 (len={len(t)})")
    if hits:
        raise AssertionError(
            f"[不在主張は誤り] '{term}' は次の経路に実在:\n" +
            "\n".join(f"    {k}: {v}" for k, v in hits.items()))
    print(f"  [OK] '{term}' は{len(sources)}経路とも非検出=不在と扱ってよい")
    return True
