import { readFile, writeFile } from 'node:fs/promises';
import { renderChichibuAffiliate } from './affiliate-chichibu-render.mjs';

const ledgerUrl = new URL('./affiliate-ledger.json', import.meta.url);
const pathPattern = /^\/[a-z0-9]+(?:-[a-z0-9]+)*\/$/;
const marker = 'data-nx-affiliate="chichibu-rakuten"';

// 既存パイロットを、確認済みの秩父・長瀞リンクの描画にだけ再利用する。
// 実際の掲載先は台帳とHTMLの言語を照合して別途決める。
function renderChichibu(html, path) {
  return renderChichibuAffiliate({ pathname: path, locale: 'ja', contentHtml: html });
}

export async function applyAffiliateLedger({ dir, state, render = renderChichibu }) {
  if (state.version !== 1 || !Array.isArray(state.approvedPages)
      || !Array.isArray(state.scheduledPaths)) {
    throw new Error('Affiliate: invalid ledger');
  }
  const approved = new Map(state.approvedPages.map(page => [page.path, page]));
  const paths = new Set(state.scheduledPaths);
  if (approved.size !== state.approvedPages.length || paths.size !== state.scheduledPaths.length) {
    throw new Error('Affiliate: duplicate ledger entry');
  }

  const changes = [];
  for (const path of paths) {
    const page = approved.get(path);
    if (typeof path !== 'string' || !pathPattern.test(path)
        || page?.locale !== 'ja' || page.regionId !== 'chichibu-nagatoro') {
      throw new Error('Affiliate: ineligible scheduled page');
    }
    const file = new URL(`${path.slice(1)}index.html`, dir);
    const before = await readFile(file, 'utf8');
    if (!/<html\b[^>]*\blang=["']ja["']/i.test(before) || before.includes(marker)) {
      throw new Error(`Affiliate: unexpected HTML for ${path}`);
    }
    const after = render(before, path);
    if (after === before || after.split(marker).length !== 2) {
      throw new Error(`Affiliate: expected one disclosure block for ${path}`);
    }
    changes.push({ file, after });
  }
  // 全対象が合格するまで、生成済みHTMLには書き込まない。
  for (const { file, after } of changes) await writeFile(file, after, 'utf8');
  return changes.length;
}

export default {
  name: 'nx4-affiliate-ledger',
  hooks: {
    'astro:build:done': async ({ dir }) => {
      const state = JSON.parse(await readFile(ledgerUrl, 'utf8'));
      const count = await applyAffiliateLedger({ dir, state });
      console.log(`[nx4-affiliate-ledger] rendered=${count}`);
    },
  },
};
