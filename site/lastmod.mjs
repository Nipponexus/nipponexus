import path from 'node:path';
import { fileURLToPath } from 'node:url';
import Database from 'better-sqlite3';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const DB_PATH = path.resolve(HERE, '../data/sqlite/nipponexus.db');
export const BUILD_ISO = new Date().toISOString();

function toIso(v) {
  if (!v) return null;
  const s = String(v).trim();
  let d;
  if (/^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}/.test(s)) {
    const tz = /[Zz]$|[+-]\d{2}:?\d{2}$/.test(s) ? '' : '+09:00';
    d = new Date(s.replace(' ', 'T') + tz);
  } else if (/^\d{4}-\d{2}-\d{2}$/.test(s)) {
    d = new Date(s + 'T00:00:00+09:00');
  } else {
    d = new Date(s);
  }
  return isNaN(d.getTime()) ? null : d.toISOString();
}

function buildMap() {
  const m = new Map();
  let db;
  try {
    db = new Database(DB_PATH, { readonly: true });
  } catch (e) {
    console.warn('[lastmod] DB open failed, fallback to build time:', e.message);
    return m;
  }
  try {
    const rows = db.prepare(
      "SELECT slug_ja, slug_en, updated_at FROM festivals WHERE status IN ('drafted','published')"
    ).all();
    for (const r of rows) {
      const iso = toIso(r.updated_at);
      if (!iso) continue;
      if (r.slug_ja) m.set('/' + String(r.slug_ja).replace(/^\/+|\/+$/g, '') + '/', iso);
      if (r.slug_en) m.set('/en/' + String(r.slug_en).replace(/^en\//, '').replace(/^\/+|\/+$/g, '') + '/', iso);
    }
  } catch (e) {
    console.warn('[lastmod] query failed:', e.message);
  } finally {
    try { db.close(); } catch (e) {}
  }
  return m;
}

const MAP = buildMap();
console.log('[lastmod] entries=' + MAP.size + ' build=' + BUILD_ISO);

export function lastmodFor(url) {
  let p;
  try { p = new URL(url).pathname; } catch (e) { p = String(url); }
  if (!p.endsWith('/')) p += '/';
  return MAP.get(p) || BUILD_ISO;
}
