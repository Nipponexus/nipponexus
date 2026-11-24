const ARTICLE_PATH = /^\/[a-z0-9]+(?:-[a-z0-9]+)*\/$/;

export function selectAffiliateAdditions({ pages, approvedRegions, alreadyPublished }) {
  const eligible = new Map();
  const published = new Set(alreadyPublished);

  for (const page of pages) {
    if (page.locale !== 'ja' || !ARTICLE_PATH.test(page.path)
        || !approvedRegions.has(page.regionId) || published.has(page.path)) {
      continue;
    }
    const previous = eligible.get(page.path);
    if (previous && previous.regionId !== page.regionId) {
      throw new Error(`Conflicting region assignments: ${page.path}`);
    }
    eligible.set(page.path, { path: page.path, regionId: page.regionId });
  }

  return [...eligible.keys()].sort().slice(0, 20).map(path => eligible.get(path));
}
