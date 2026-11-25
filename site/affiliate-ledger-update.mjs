import { mkdtempSync, mkdirSync, readFileSync, renameSync, rmdirSync,
         unlinkSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { planAffiliateDay } from './affiliate-regional-daily-plan.mjs';

export function updateLedger(file, dateJst) {
  const lock = `${file}.lock`;
  try {
    mkdirSync(lock, { mode: 0o700 });
  } catch (error) {
    if (error.code === 'EEXIST') throw new Error('台帳がロックされています。変更なし');
    throw error;
  }
  let tempDir, temp;
  try {
    const before = readFileSync(file, 'utf8');
    const result = planAffiliateDay(JSON.parse(before), dateJst);
    if (!result.additions.length) return 0;

    tempDir = mkdtempSync(join(dirname(file), '.affiliate-ledger-'));
    temp = join(tempDir, 'ledger.json');
    const body = JSON.stringify(result.state, null, 2) + '\n';
    writeFileSync(temp, body, { encoding: 'utf8', flag: 'wx' });
    if (readFileSync(temp, 'utf8') !== body || readFileSync(file, 'utf8') !== before) {
      throw new Error('差し替え前の照合に失敗');
    }
    renameSync(temp, file);
    temp = undefined;
    return result.additions.length;
  } finally {
    try {
      if (temp) {
        try { unlinkSync(temp); } catch (error) {
          if (error.code !== 'ENOENT') throw error;
        }
      }
      if (tempDir) rmdirSync(tempDir);
    } finally {
      rmdirSync(lock);
    }
  }
}

if (process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url) {
  const parts = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Tokyo', year: 'numeric', month: '2-digit', day: '2-digit',
  }).formatToParts(new Date());
  const part = type => parts.find(p => p.type === type).value;
  const date = `${part('year')}-${part('month')}-${part('day')}`;
  try {
    const count = updateLedger(fileURLToPath(new URL('./affiliate-ledger.json', import.meta.url)), date);
    console.log(`広告台帳: ${date} JST / 追加 ${count}件`);
  } catch (error) {
    console.error(`広告台帳の更新中断: ${error.message}`);
    process.exitCode = 1;
  }
}
