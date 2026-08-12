import { prefEn } from './i18n_geo';
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
  image_author: string | null;
  image_license: string | null;
  image_credit_url: string | null;
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
  const regionOrder = ['hokkaido', 'tohoku', 'kanto', 'chubu', 'kinki', 'chugoku', 'shikoku', 'kyushu', 'okinawa'];
  const regionLabels: Record<string, { ja: string; en: string }> = {
    hokkaido: { ja: '北海道', en: 'Hokkaido' },
    tohoku: { ja: '東北', en: 'Tohoku' },
    kanto: { ja: '関東', en: 'Kanto' },
    chubu: { ja: '中部', en: 'Chubu' },
    kinki: { ja: '近畿', en: 'Kinki' },
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
  const prefectureOrder = [
    '北海道',
    '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県',
    '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県',
    '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県',
    '三重県', '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県',
    '鳥取県', '島根県', '岡山県', '広島県', '山口県',
    '徳島県', '香川県', '愛媛県', '高知県',
    '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県',
  ];
  const idx = (k: string) => {
    const i = prefectureOrder.indexOf(k);
    return i === -1 ? prefectureOrder.length : i;  // 配列外は末尾
  };
  return [...map.entries()]
    .sort((a, b) => idx(a[0]) - idx(b[0]))
    .map(([k, v]) => ({ key: locale === 'en' ? prefEn(k).toLowerCase().replace(/\s+/g, '-') : k, label: locale === 'en' ? prefEn(k) : k, festivals: v }));
}

/**
 * 同じ都道府県の他の祭りを取得（内部リンク用）。
 * drafted/published かつ該当localeのslugありのみ。自分自身(excludeQid)を除外。
 */
export function getRelatedByPrefecture(
  prefecture: string | null,
  excludeQid: string,
  locale: 'ja' | 'en',
  limit = 6
): Festival[] {
  if (!prefecture) return [];
  const db = open();
  const slugCol = locale === 'ja' ? 'slug_ja' : 'slug_en';
  const stmt = db.prepare(`
    SELECT * FROM festivals
    WHERE prefecture = ?
      AND status IN ('drafted', 'published')
      AND ${slugCol} IS NOT NULL
      AND qid != ?
    ORDER BY priority_score DESC, qid
    LIMIT ?
  `);
  const rows = stmt.all(prefecture, excludeQid, limit) as Festival[];
  db.close();
  return rows;
}

/**
 * 同じ季節の他の祭りを取得（内部リンク用）。
 * drafted/published かつ該当localeのslugありのみ。自分自身(excludeQid)を除外。
 */
export function getRelatedBySeason(
  season: string | null,
  excludeQid: string,
  locale: 'ja' | 'en',
  limit = 6
): Festival[] {
  if (!season) return [];
  const db = open();
  const slugCol = locale === 'ja' ? 'slug_ja' : 'slug_en';
  const stmt = db.prepare(`
    SELECT * FROM festivals
    WHERE season = ?
      AND status IN ('drafted', 'published')
      AND ${slugCol} IS NOT NULL
      AND qid != ?
    ORDER BY priority_score DESC, qid
    LIMIT ?
  `);
  const rows = stmt.all(season, excludeQid, limit) as Festival[];
  db.close();
  return rows;
}

export interface EventEnd {
  qid: string; end_year: number | null; kind: string | null;
  successor_qid: string | null; successor_label: string | null;
}

export function getEventEnd(qid: string): EventEnd | null {
  const db = open();
  try {
    const t = db.prepare(
      "SELECT name FROM sqlite_master WHERE type='table' AND name='event_end'"
    ).get();
    if (!t) return null;
    const row = db.prepare('SELECT * FROM event_end WHERE qid = ?').get(qid) as EventEnd | undefined;
    return row ?? null;
  } catch { return null; } finally { db.close(); }
}
