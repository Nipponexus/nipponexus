// Nipponexus affiliate pilot. No network calls or file writes.
const PILOT_PATH = '/chichibu-night-festival/';
const MARKER = 'data-nx-affiliate="chichibu-rakuten"';

const RAKUTEN_HTML = '<a href="https://hb.afl.rakuten.co.jp/hgc/59e243eb.8ca0aa23.59e243ec.b3529479/?pc=https%3A%2F%2Ftravel.rakuten.co.jp%2Fyado%2Fsaitama%2Fchichibu.html&link_type=text&ut=eyJwYWdlIjoidXJsIiwidHlwZSI6InRleHQiLCJjb2wiOjF9" target="_blank" rel="nofollow sponsored noopener" style="word-wrap:break-word;">https://travel.rakuten.co.jp/yado/saitama/chichibu.html</a>';

export function renderAffiliatePilot({ pathname, locale, contentHtml }) {
  if (pathname !== PILOT_PATH || locale !== 'ja') return contentHtml;
  if (typeof contentHtml !== 'string') throw new Error('Missing article HTML');
  if (contentHtml.includes(MARKER)) throw new Error('Duplicate affiliate marker');

  const access = [...contentHtml.matchAll(
    /<h2\b[^>]*>\s*開催情報・アクセス\s*<\/h2\s*>/gi
  )];
  if (access.length !== 1) throw new Error('Access heading not unique');

  const endOfHeading = access[0].index + access[0][0].length;
  const next = /<h2\b[^>]*>\s*周辺の見どころ\s*<\/h2\s*>/i.exec(
    contentHtml.slice(endOfHeading)
  );
  const nextH2 = /<h2\b/i.exec(contentHtml.slice(endOfHeading));
  if (!next || !nextH2 || next.index !== nextH2.index) {
    throw new Error('Unexpected section after access');
  }

  const end = endOfHeading + next.index;
  const ad = '\n<aside ' + MARKER + '><p><strong>' +
    '広告｜秩父・長瀞の宿を探す（楽天トラベル）' +
    '</strong></p><p>' + RAKUTEN_HTML + '</p></aside>\n';
  return contentHtml.slice(0, end) + ad + contentHtml.slice(end);
}
