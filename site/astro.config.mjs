import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://nipponexus.com',
  i18n: {
    defaultLocale: 'ja',
    locales: ['ja', 'en'],
    routing: { prefixDefaultLocale: false },
  },
});
