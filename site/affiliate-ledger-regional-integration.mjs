import { readFile, writeFile } from 'node:fs/promises';
import { applyAffiliateLedger as applyLegacy } from './affiliate-ledger-chichibu-integration.mjs';
import { renderRegionalAffiliate } from './affiliate-region-render.mjs';

const readJson = async name => JSON.parse(await readFile(new URL(name, import.meta.url), 'utf8'));
const oldPaths = new Set(['/chichibu-night-festival/', '/chichibu-kawase-matsuri/']);
const pathPattern = /^\/[a-z0-9]+(?:-[a-z0-9]+)*\/$/;

export default {
  name: 'nx4-affiliate-regional-ledger',
  hooks: {
    'astro:build:done': async ({ dir }) => {
      const state = await readJson('./affiliate-ledger.json');
      const links = new Map(Object.entries(await readJson('./affiliate-region-links.json')));
      const approved = new Map(state.approvedPages.map(p => [p.path, p]));
      const scheduled = new Set(state.scheduledPaths);
      if (state.version !== 1 || approved.size !== state.approvedPages.length
          || scheduled.size !== state.scheduledPaths.length) {
        throw new Error('Affiliate: invalid or duplicate ledger entries');
      }
      const changes = [];
      for (const path of scheduled) {
        if (oldPaths.has(path)) continue;
        const placement = approved.get(path);
        if (!pathPattern.test(path) || placement?.locale !== 'ja') {
          throw new Error('Affiliate: ineligible regional path');
        }
        const file = new URL(`${path.slice(1)}index.html`, dir);
        const html = await readFile(file, 'utf8');
        const after = renderRegionalAffiliate({ pathname: path, locale: 'ja', html, placement, links });
        if (after === html || (after.match(/data-nx-affiliate\s*=/gi) || []).length !== 1) {
          throw new Error(`Affiliate: expected one regional ad for ${path}`);
        }
        changes.push({ file, after });
      }
      const oldCount = await applyLegacy({
        dir, state: { ...state, scheduledPaths: state.scheduledPaths.filter(p => oldPaths.has(p)) },
      });
      for (const { file, after } of changes) await writeFile(file, after, 'utf8');
      console.log(`[nx4-affiliate-ledger] legacy=${oldCount} regional=${changes.length}`);
    },
  },
};
