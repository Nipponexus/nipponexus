import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { lastmodFor } from './lastmod.mjs';

export default defineConfig({
  site: 'https://nipponexus.com',
  integrations: [sitemap({ serialize(item) { item.lastmod = lastmodFor(item.url); return item; } })],
  i18n: {
    defaultLocale: 'ja',
    locales: ['ja', 'en'],
    routing: { prefixDefaultLocale: false },
  },
});
