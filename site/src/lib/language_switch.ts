import { getDraftedFestivals } from './festivals';

type Locale = 'ja' | 'en';
type SlugRow = { qid: string; slug_ja: string | null; slug_en: string | null };

const normalize = (pathname: string) => `/${pathname.split('/').filter(Boolean).join('/')}${pathname.split('/').filter(Boolean).length ? '/' : ''}`;
const articlePath = (slug: string, locale: Locale) => `/${locale === 'en' ? 'en/' : ''}${slug}/`;

// Match only routes actually emitted by the two getStaticPaths functions and
// concrete Astro pages. Never infer an English article slug from a Japanese one.
export function createLanguageSwitch(ja: SlugRow[], en: SlugRow[], staticPaths: string[]) {
  const counterparts = new Map<string, string>();
  const pages = new Set(staticPaths.map(normalize));
  const english = new Map(en.map(row => [row.qid, row]));
  for (const row of ja) {
    const other = english.get(row.qid);
    if (row.slug_ja && other?.slug_en) {
      const a = articlePath(row.slug_ja, 'ja');
      const b = articlePath(other.slug_en, 'en');
      counterparts.set(a, b);
      counterparts.set(b, a);
    }
  }
  for (const page of pages) {
    if (page.startsWith('/en/')) continue;
    const other = page === '/' ? '/en/' : `/en${page}`;
    if (pages.has(other)) {
      counterparts.set(page, other);
      counterparts.set(other, page);
    }
  }
  return (pathname: string, locale: Locale) => {
    const match = counterparts.get(normalize(pathname));
    const isJa = locale === 'ja';
    const fallback = !match;
    return {
      href: match ?? (isJa ? '/en/' : '/'),
      label: fallback ? (isJa ? 'English (home)' : '日本語（ホーム）') : (isJa ? 'English' : '日本語'),
      headerLabel: fallback ? (isJa ? 'English (home)' : '日本語（ホーム）') : (isJa ? 'EN' : '日本語'),
      fallback,
    };
  };
}

const staticPaths = Object.keys(import.meta.glob('../pages/**/*.astro'))
  .filter(file => !file.includes('['))
  .map(file => file.replace('../pages', '').replace(/\.astro$/, '').replace(/\/index$/, '') || '/');

export const getLanguageSwitch = createLanguageSwitch(
  getDraftedFestivals('ja'), getDraftedFestivals('en'), staticPaths,
);
