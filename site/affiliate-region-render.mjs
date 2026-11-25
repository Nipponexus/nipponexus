const idPattern = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const pagePattern = /^\/[a-z0-9]+(?:-[a-z0-9]+)*\/$/;
const escapeHtml = s => s.replace(/[&<>"']/g, c => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
}[c]));

export function renderRegionalAffiliate({ pathname, locale, html, placement, links }) {
  if (locale !== 'ja' || !placement || placement.path !== pathname) return html;
  if (!pagePattern.test(pathname) || placement.locale !== 'ja'
      || !idPattern.test(placement.regionId ?? '') || !idPattern.test(placement.linkId ?? '')) {
    throw new Error('Affiliate: invalid placement');
  }
  // links は確認済みの発行コードだけを保持する。記事台帳にはHTMLを書かない。
  const link = links.get(placement.linkId);
  if (!link || link.regionId !== placement.regionId || !link.label?.trim()
      || typeof link.html !== 'string' || [...link.html.matchAll(/<a\b/gi)].length !== 1
      || /data-nx-affiliate/i.test(link.html)) {
    throw new Error('Affiliate: missing or mismatched approved link');
  }
  if (!/<html\b[^>]*\blang=["']ja["']/i.test(html) || /data-nx-affiliate\s*=/i.test(html)) {
    throw new Error('Affiliate: unexpected language or existing ad');
  }
  const headings = [...html.matchAll(/<h2\b[^>]*>([\s\S]*?)<\/h2\s*>/gi)];
  const access = headings.filter(m => m[1].trim() === '開催情報・アクセス');
  const next = headings[headings.indexOf(access[0]) + 1];
  if (access.length !== 1 || !next || next[1].trim() !== '周辺の見どころ') {
    throw new Error('Affiliate: insertion point changed');
  }
  const ad = `\n<aside data-nx-affiliate="${placement.linkId}"><p><strong>広告｜${escapeHtml(link.label)}</strong></p><p>${link.html}</p></aside>\n`;
  return html.slice(0, next.index) + ad + html.slice(next.index);
}
