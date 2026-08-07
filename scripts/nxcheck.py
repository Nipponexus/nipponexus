# -*- coding: utf-8 -*-
"""コード上の存在確認(2026-08-06新設)。

★背景: 存在確認を生の str.count / grep で行い、自分がパッチのコメントへ書いた識別子を
  拾って『二重適用の疑い』『旧経路が残存』の誤検知を2連続で出した。さらに追記型パッチの
  冪等化を既存ファイルへの文字列手術で入れようとして二重挿入の穴を自ら作った。
  原因は個々の不注意でなく『既存ファイルを文字列手術し、文字列カウントで検証する』方法
  そのもの。→新規機能は独立モジュールとして新規作成し、検証はトークン解析に固定する。
★使い方: 存在確認は count_code / assert_once を必ず経由する。生countは使わない。
"""
import io, os, re, glob, tokenize


def _blank(s):
    return ''.join(' ' if ch != '\n' else '\n' for ch in s)


def code_only(path):
    """コメントと文字列リテラルを空白化したソースを返す(行番号は保存)。"""
    src = open(os.path.expanduser(path), encoding='utf-8').read()
    lines = src.splitlines(True)
    for t in tokenize.generate_tokens(io.StringIO(src).readline):
        if t.type not in (tokenize.COMMENT, tokenize.STRING):
            continue
        (sr, sc), (er, ec) = t.start, t.end
        if sr == er:
            l = lines[sr-1]; lines[sr-1] = l[:sc] + _blank(l[sc:ec]) + l[ec:]
        else:
            l = lines[sr-1]; lines[sr-1] = l[:sc] + _blank(l[sc:])
            for r in range(sr, er-1):
                lines[r] = _blank(lines[r])
            l = lines[er-1]; lines[er-1] = _blank(l[:ec]) + l[ec:]
    return ''.join(lines)


def count_code(path, marker):
    """コード実体での出現数。コメント/文字列は数えない。"""
    return code_only(path).count(marker)


def where(path, marker):
    """出現行を [(行番号, 行)] で返す(重複の所在を目で確認するため)。"""
    return [(i, l.rstrip()) for i, l in enumerate(code_only(path).split('\n'), 1)
            if marker in l]


def assert_once(path, marker):
    n = count_code(path, marker)
    assert n == 1, '%s: %r が %d 件 %s' % (os.path.basename(path), marker, n,
                                          where(path, marker))
    return True


def defs(path):
    """トップレベル定義名と行番号。重複定義(静かに後勝ちする事故)の検出用。"""
    out = {}
    for i, l in enumerate(code_only(path).split('\n'), 1):
        if l.startswith('def ') or l.startswith('class '):
            out.setdefault(l.split('(')[0].split(':')[0].strip(), []).append(i)
    return out


def dup_defs(path):
    return {k: v for k, v in defs(path).items() if len(v) > 1}


def dup_defs_real(path):
    """真に上書きされている重複定義だけを返す(2026-08-07新設)。

    ★背景: pro_verify(3定義)/as_defects(2定義)は `_raw_x = x` で前定義を別名へ退避してから
      再定義する手書きデコレータであり、全層が生きている。dup_defs はこれを毎回誤検知する。
      退避行が定義の間に無いものだけを『静かに後勝ちして消えた定義』として報告する。
    """
    src = code_only(path).split('\n')
    out = {}
    for name, lines in dup_defs(path).items():
        bare = name.split()[-1]   # defs() のキーは 'def foo' 形式
        lost = []
        for a, b in zip(lines, lines[1:]):
            between = '\n'.join(src[a-1:b-1])
            if not re.search(r'^\s*\w+\s*=\s*%s\s*$' % re.escape(bare), between, re.M):
                lost.append(a)
        if lost:
            out[name] = {'all': lines, 'overwritten': lost}
    return out


def scan_dups(dirpath='~/nipponexus/scripts'):
    """ディレクトリ一括。run_full の前段や自己診断から呼ぶ。"""
    hits = {}
    for f in sorted(glob.glob(os.path.join(os.path.expanduser(dirpath), '*.py'))):
        if '_backup' in f or '_tmp' in f:
            continue
        try:
            d = dup_defs_real(f)
        except Exception as e:
            hits[os.path.basename(f)] = {'ERROR': str(e)}
            continue
        if d:
            hits[os.path.basename(f)] = d
    return hits
