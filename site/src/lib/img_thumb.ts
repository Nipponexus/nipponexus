// Commons 画像をサムネイル幅つき URL にする独立モジュール。DB の値は原寸のまま保つ。
export function thumbUrl(url: string | null, width = 400): string | null {
  if (!url) return url;
  if (!url.includes('Special:FilePath/')) return url;
  if (url.includes('?')) return url;
  return url + '?width=' + width;
}
export function withThumb<T extends { image_url: string | null }>(rows: T[], width = 400): T[] {
  return rows.map((r) => (r.image_url ? { ...r, image_url: thumbUrl(r.image_url, width) } : r));
}
