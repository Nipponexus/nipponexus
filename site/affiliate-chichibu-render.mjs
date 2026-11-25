import { renderAffiliatePilot } from './affiliate-pilot.mjs';

const NIGHT = '/chichibu-night-festival/';
const KAWASE = '/chichibu-kawase-matsuri/';
const MARKER = 'data-nx-affiliate="chichibu-rakuten"';
const OLD_LABEL = '広告｜秩父・長瀞の宿を探す（楽天トラベル）';
const HOTEL_LABEL = '広告｜ナチュラルファームシティ農園ホテル（楽天トラベル）';

function kawaseBlock() {
  // 発行済みリンクを再生成せず、既存の広告枠からそのまま引き継ぐ。
  const html = renderAffiliatePilot({
    pathname: NIGHT, locale: 'ja',
    contentHtml: '<h2>開催情報・アクセス</h2><h2>周辺の見どころ</h2>',
  });
  const blocks = [...html.matchAll(/<aside\b[^>]*data-nx-affiliate="chichibu-rakuten"[^>]*>[\s\S]*?<\/aside>/gi)];
  if (blocks.length !== 1 || blocks[0][0].split(OLD_LABEL).length !== 2) {
    throw new Error('Kawase: unexpected affiliate block');
  }
  return blocks[0][0].replace(OLD_LABEL, HOTEL_LABEL);
}

export function renderChichibuAffiliate({ pathname, locale, contentHtml }) {
  if (locale !== 'ja') return contentHtml;
  if (pathname === NIGHT) return renderAffiliatePilot({ pathname, locale, contentHtml });
  if (pathname !== KAWASE) return contentHtml;
  if (contentHtml.includes(MARKER)) throw new Error('Kawase: affiliate already exists');

  const access = [...contentHtml.matchAll(
    /<h2\b[^>]*>\s*開催情報・アクセス\s*<\/h2\s*>/gi
  )];
  if (access.length !== 1) throw new Error('Kawase: access heading not unique');
  const end = access[0].index + access[0][0].length;
  const next = /<h2\b[^>]*>/i.exec(contentHtml.slice(end));
  if (!next) throw new Error('Kawase: next heading missing');
  const at = end + next.index;
  if (!/^<h2\b[^>]*>\s*周辺情報\s*<\/h2\s*>/i.test(contentHtml.slice(at))) {
    throw new Error('Kawase: unexpected next heading');
  }
  return contentHtml.slice(0, at) + '\n' + kawaseBlock() + '\n' + contentHtml.slice(at);
}
