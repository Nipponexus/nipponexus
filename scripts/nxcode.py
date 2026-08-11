# -*- coding: utf-8 -*-
# nxcode.py  CODECHK_v1 2026-08-12
# 00-A3が使用を義務づける count_code / assert_once / dup_defs の実体。
# 生のgrep/countはコメントと文字列リテラルを拾って偽陽性を出すため、tokenize/astで判定する。
# replace_func は2026-08-10のpro_verify_loop破損事故(文字列一致replaceが別箇所を書換)への恒久対策。
import io, ast, token, tokenize, pathlib, collections
def _code_text(src):
    """コメントと文字列リテラルを除いたコードのみのテキストを返す。"""
    out = []
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type in (token.COMMENT, token.STRING): continue
        if tok.type in (token.NEWLINE, token.NL, token.INDENT, token.DEDENT): continue
        out.append(tok.string)
    return ' '.join(out)
def count_code(path, needle):
    """コード部分だけを対象にneedleの出現数を数える。
    needleも同じトークナイザに通す(nxenchk.check 等のドット名が空振りするため)。"""
    hay = _code_text(pathlib.Path(path).read_text(encoding='utf-8'))
    try:
        pat = _code_text(needle)
    except Exception:
        pat = needle
    return hay.count(pat) if pat else 0
def assert_once(path, needle):
    n = count_code(path, needle)
    assert n == 1, 'count_code(%s, %r) = %d (expected 1)' % (path, needle, n)
    return True
def dup_defs(path):
    """同名で複数定義されている関数/クラスを返す。二重挿入事故の検出用。"""
    tree = ast.parse(pathlib.Path(path).read_text(encoding='utf-8'))
    names = [n.name for n in ast.walk(tree)
             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
    return {k: v for k, v in collections.Counter(names).items() if v > 1}
def replace_func(path, name, new_src):
    """astで対象関数のlineno/end_linenoを取り関数まるごと差し替える。
    対象以外の全関数が1文字も変化していないことを検査し、変化があればValueError。"""
    p = pathlib.Path(path); src = p.read_text(encoding='utf-8')
    segs = lambda s: {n.name: ast.get_source_segment(s, n) for n in ast.parse(s).body
                      if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
    before = segs(src)
    nodes = [n for n in ast.parse(src).body
             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name]
    if len(nodes) != 1: raise ValueError('%s は %d 個' % (name, len(nodes)))
    n = nodes[0]; L = src.split('\n')
    out = '\n'.join(L[:n.lineno-1] + new_src.split('\n') + L[n.end_lineno:])
    after = segs(out)
    diff = [k for k in before if k != name and before[k] != after.get(k)]
    if diff: raise ValueError('巻き添え変更: %s' % diff)
    if set(before) != set(after): raise ValueError('関数集合が変化')
    ast.parse(out)
    return out
# 自己テスト(import時)。目視回帰に頼らない。
_S = 'x = "def foo():"  # def foo():\ndef foo():\n    return 1\ndef bar():\n    return foo()\n'
import tempfile, os as _os
_f = tempfile.NamedTemporaryFile('w', suffix='.py', delete=False, encoding='utf-8'); _f.write(_S); _f.close()
assert count_code(_f.name, 'def foo') == 1, 'FX1 コメント/文字列を拾った'
assert dup_defs(_f.name) == {}, 'FX2'
assert 'def foo():\n    return 2' in replace_func(_f.name, 'foo', 'def foo():\n    return 2'), 'FX3'
try:
    replace_func(_f.name, 'baz', 'def baz(): pass'); raise SystemExit('FX4 不在関数を通した')
except ValueError: pass
_os.unlink(_f.name)
if __name__ == '__main__': print('[OK] nxcode self-test 4/4')
