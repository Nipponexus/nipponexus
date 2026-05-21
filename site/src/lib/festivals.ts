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
  priority_score: number;
}

function open() {
  return new Database(DB_PATH, { readonly: true });
}

export function getDraftedFestivals(locale: 'ja' | 'en'): Festival[] {
  const db = open();
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
  const db = open();
  const slugCol = locale === 'ja' ? 'slug_ja' : 'slug_en';
  const stmt = db.prepare(`SELECT * FROM festivals WHERE ${slugCol} = ?`);
  const row = stmt.get(slug) as Festival | undefined;
  db.close();
  return row || null;
}

/**
 * 全祭り取得（索引ページ用・status問わず・ラベルあるもののみ）
 * 公開済みでないものはリンクなしで表示する。
 */
export function getAllFestivalsForIndex(locale: 'ja' | 'en'): Festival[] {
  const db = open();
  const labelCol = locale === 'ja' ? 'label_ja' : 'label_en';
  const stmt = db.prepare(`
    SELECT * FROM festivals
    WHERE ${labelCol} IS NOT NULL AND ${labelCol} != ''
    ORDER BY priority_score DESC, qid
  `);
  const rows = stmt.all() as Festival[];
  db.close();
  return rows;
}

export interface GroupedFestivals {
  key: string;
  label: string;
  festivals: Festival[];
}

export function groupByRegion(festivals: Festival[], locale: 'ja' | 'en'): GroupedFestivals[] {
  const regionOrder = ['hokkaido', 'tohoku', 'kanto', 'chubu', 'kansai', 'chugoku', 'shikoku', 'kyushu', 'okinawa'];
  const regionLabels: Record<string, { ja: string; en: string }> = {
    hokkaido: { ja: '北海道', en: 'Hokkaido' },
    tohoku: { ja: '東北', en: 'Tohoku' },
    kanto: { ja: '関東', en: 'Kanto' },
    chubu: { ja: '中部', en: 'Chubu' },
    kansai: { ja: '関西', en: 'Kansai' },
    chugoku: { ja: '中国', en: 'Chugoku' },
    shikoku: { ja: '四国', en: 'Shikoku' },
    kyushu: { ja: '九州', en: 'Kyushu' },
    okinawa: { ja: '沖縄', en: 'Okinawa' },
    unknown: { ja: 'その他', en: 'Others' },
  };
  const map = new Map<string, Festival[]>();
  for (const f of festivals) {
    if (!f.region) continue;  // 地域未確定は除外
    const k = f.region;
    if (!map.has(k)) map.set(k, []);
    map.get(k)!.push(f);
  }
  return regionOrder
    .filter(k => map.has(k))
    .map(k => ({ key: k, label: regionLabels[k][locale], festivals: map.get(k)! }));
}

export function groupBySeason(festivals: Festival[], locale: 'ja' | 'en'): GroupedFestivals[] {
  const seasonOrder = ['spring', 'summer', 'autumn', 'winter'];
  const seasonLabels: Record<string, { ja: string; en: string }> = {
    spring: { ja: '春', en: 'Spring' },
    summer: { ja: '夏', en: 'Summer' },
    autumn: { ja: '秋', en: 'Autumn' },
    winter: { ja: '冬', en: 'Winter' },
    unknown: { ja: '通年・不明', en: 'Year-round / Unknown' },
  };
  const map = new Map<string, Festival[]>();
  for (const f of festivals) {
    if (!f.season) continue;  // 季節未確定は除外
    const k = f.season;
    if (!map.has(k)) map.set(k, []);
    map.get(k)!.push(f);
  }
  return seasonOrder
    .filter(k => map.has(k))
    .map(k => ({ key: k, label: seasonLabels[k][locale], festivals: map.get(k)! }));
}

export function groupByPrefecture(festivals: Festival[], locale: 'ja' | 'en'): GroupedFestivals[] {
  const map = new Map<string, Festival[]>();
  for (const f of festivals) {
    if (!f.prefecture) continue;  // 都道府県未確定は除外
    const k = f.prefecture;
    if (!map.has(k)) map.set(k, []);
    map.get(k)!.push(f);
  }
  return [...map.entries()]
    .sort((a, b) => b[1].length - a[1].length)
    .map(([k, v]) => ({ key: k, label: k, festivals: v }));
}
