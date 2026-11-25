import { readFileSync } from 'node:fs';

function approvedRegionsFor(pages) {
  const links = JSON.parse(readFileSync(
    new URL('./affiliate-region-links.json', import.meta.url), 'utf8'
  ));
  const legacyPaths = new Set(['/chichibu-night-festival/', '/chichibu-kawase-matsuri/']);
  const regions = new Set(['chichibu-nagatoro']);
  for (const page of pages) {
    if (legacyPaths.has(page.path) && page.regionId === 'chichibu-nagatoro') continue;
    const id = page.linkId;
    if (page.locale !== 'ja' || typeof id !== 'string' || !Object.hasOwn(links, id)
        || links[id]?.regionId !== page.regionId) {
      throw new Error('Affiliate: approved page has no matching regional link');
    }
    regions.add(page.regionId);
  }
  return regions;
}

import { selectAffiliateAdditions } from './affiliate-rollout.mjs';

export function planAffiliateDay(state, dateJst) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(dateJst)
      || new Date(dateJst + 'T00:00:00Z').toISOString().slice(0, 10) !== dateJst) {
    throw new Error('Invalid JST date');
  }
  if (state.version !== 1 || !Array.isArray(state.approvedPages)
      || !Array.isArray(state.scheduledPaths)) {
    throw new Error('Invalid affiliate ledger');
  }
  const paths = state.approvedPages.map(page => page.path);
  if (new Set(paths).size !== paths.length
      || new Set(state.scheduledPaths).size !== state.scheduledPaths.length
      || state.scheduledPaths.some(path => !paths.includes(path))) {
    throw new Error('Duplicate or unapproved path in affiliate ledger');
  }
  if (state.lastAdditionDateJst && dateJst < state.lastAdditionDateJst) {
    throw new Error('JST date precedes the last rollout');
  }

  const additions = selectAffiliateAdditions({
    pages: state.approvedPages,
    approvedRegions: approvedRegionsFor(state.approvedPages),
    alreadyPublished: state.scheduledPaths,
  }).map(page => page.path);
  return {
    additions,
    state: additions.length ? {
      ...state,
      lastAdditionDateJst: dateJst,
      scheduledPaths: [...state.scheduledPaths, ...additions],
    } : state,
  };
}
