import Database from 'better-sqlite3';
import path from 'path';

const DB_PATH = path.resolve(process.cwd(), '../data/sqlite/nipponexus.db');

export interface Festival {
  qid: string;
  label_ja: string;
  label_en: string;
  description_ja: string | null;
  description_en: string | null;
  location_label_ja: string | null;
  location_label_en: string | null;
  prefecture: string | null;
  region: string | null;
  latitude: number | null;
  longitude: number | null;
  inception_year: number | null;
  start_month: number | null;
  season: string | null;
  image_url: string | null;
  wikipedia_ja: string | null;
  wikipedia_en: string | null;
  manual_content_ja: string | null;
  manual_content_en: string | null;
  slug_ja: string | null;
  slug_en: string | null;
  status: string;
}

export function getDraftedFestivals(locale: 'ja' | 'en'): Festival[] {
  const db = new Database(DB_PATH, { readonly: true });
  const slugCol = locale === 'ja' ? 'slug_ja' : 'slug_en';
  const stmt = db.prepare(`
    SELECT * FROM festivals
    WHERE status IN ('drafted', 'published')
      AND ${slugCol} IS NOT NULL
    ORDER BY priority_score DESC
  `);
  const rows = stmt.all() as Festival[];
  db.close();
  return rows;
}

export function getFestivalBySlug(slug: string, locale: 'ja' | 'en'): Festival | null {
  const db = new Database(DB_PATH, { readonly: true });
  const slugCol = locale === 'ja' ? 'slug_ja' : 'slug_en';
  const stmt = db.prepare(`SELECT * FROM festivals WHERE ${slugCol} = ?`);
  const row = stmt.get(slug) as Festival | undefined;
  db.close();
  return row || null;
}
