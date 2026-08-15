import { marked } from 'marked';

// 裸URLの自動リンクが全角括弧・句読点を URL に飲み込む問題を打ち消す。
// marked の出力後に、アンカー文字列が URL そのものである要素だけを対象に終端を切り直す。
const CUT = /[（）。、「」『』…\u3000]/;

function trimUrl(raw: string): [string, string] {
  let keep = raw;
  const m = keep.match(CUT);
  let rest = '';
  if (m && m.index !== undefined) { rest = keep.slice(m.index); keep = keep.slice(0, m.index); }
  while (keep.length > 1 && /[)\].,;:!?]$/.test(keep)) {
    const last = keep[keep.length - 1];
    if (last === ')' && (keep.split('(').length - 1) >= (keep.split(')').length - 1)) break;
    if (last === ']' && (keep.split('[').length - 1) >= (keep.split(']').length - 1)) break;
    rest = last + rest; keep = keep.slice(0, -1);
  }
  return [keep, rest];
}

export function mdToHtml(src: string | null | undefined): string {
  const html = marked.parse(src ?? '') as string;
  return html.replace(
    /<a href="(https?:\/\/[^"]+)"([^>]*)>(https?:\/\/[^<]*)<\/a>/g,
    (full, _href, attrs, text) => {
      const [keep, rest] = trimUrl(text);
      if (!rest) return full;
      return '<a href="' + encodeURI(keep) + '"' + attrs + '>' + keep + '</a>' + rest;
    }
  );
}
