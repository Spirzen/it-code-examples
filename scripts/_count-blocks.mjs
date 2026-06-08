import fs from 'node:fs';
import path from 'node:path';

const dir = process.argv[2];
const min = Number(process.argv[3] ?? 15);
const skip = new Set(['text', 'mermaid', 'plain', '']);

for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.md'))) {
  const body = fs.readFileSync(path.join(dir, f), 'utf8').replace(/\r\n/g, '\n');
  const re = /```(\w*)\r?\n([\s\S]*?)```/g;
  let m;
  let n = 0;
  let nMin = 0;
  while ((m = re.exec(body))) {
    if (skip.has(m[1])) continue;
    n++;
    if (m[2].split('\n').length >= min) nMin++;
  }
  if (nMin) console.log(`${f}: ${n} blocks, ${nMin} >= ${min}`);
}
