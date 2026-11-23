import base from './astro.config.mjs';
import { readFile, realpath, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { renderAffiliatePilot } from './affiliate-pilot.mjs';

const marker = 'data-nx-affiliate="chichibu-rakuten"';

export const affiliatePilot = {
  name: 'nx-affiliate-pilot',
  hooks: {
    async 'astro:build:done'({ dir, logger }) {
      const root = await realpath(fileURLToPath(dir));
      const page = resolve(root, 'chichibu-night-festival/index.html');
      if (await realpath(page) !== page) throw new Error('Unexpected output path');

      const before = await readFile(page, 'utf8');
      if (!/<html\b[^>]*\blang=["']ja["']/i.test(before)) {
        throw new Error('Unexpected output language');
      }
      const after = renderAffiliatePilot({
        pathname: '/chichibu-night-festival/', locale: 'ja', contentHtml: before,
      });
      if (after.split(marker).length !== 2 ||
          after.replace(/\n<aside data-nx-affiliate="chichibu-rakuten">[\s\S]*?<\/aside>\n/, '') !== before) {
        throw new Error('Unexpected HTML difference');
      }
      await writeFile(page, after, 'utf8');
      logger.info('NX affiliate pilot: 1 page');
    },
  },
};

export default {
  ...base,
  integrations: [...(base.integrations ?? []), affiliatePilot],
};
