import { readFile, writeFile } from 'node:fs/promises';
import { renderAffiliatePilot } from './affiliate-pilot.mjs';

export default {
  name: 'nx4-chichibu-affiliate',
  hooks: {
    'astro:build:done': async ({ dir }) => {
      const file = new URL('chichibu-night-festival/index.html', dir);
      const before = await readFile(file, 'utf8');
      if (!/<html\b[^>]*\blang=["']ja["']/i.test(before)) {
        throw new Error('Affiliate: target HTML is not Japanese');
      }
      const after = renderAffiliatePilot({
        pathname: '/chichibu-night-festival/',
        locale: 'ja',
        contentHtml: before,
      });
      if (after.split('data-nx-affiliate="chichibu-rakuten"').length !== 2) {
        throw new Error('Affiliate: expected one disclosure block');
      }
      await writeFile(file, after, 'utf8');
    },
  },
};
