import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dist = path.join(__dirname, '..', 'dist');
const legacyPrefix = 'it-code-examples';
const legacyBase = process.env.IT_CODE_EXAMPLES_BASE ?? '/';

function copyDir(src, dest) {
  fs.mkdirSync(dest, {recursive: true});
  for (const entry of fs.readdirSync(src, {withFileTypes: true})) {
    const from = path.join(src, entry.name);
    const to = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDir(from, to);
    } else {
      fs.copyFileSync(from, to);
    }
  }
}

if (!fs.existsSync(dist)) {
  console.error('[postbuild] dist/ не найден — сначала astro build');
  process.exit(1);
}

// Зеркало всего сайта под /it-code-examples/ — старые ссылки Project Pages и кэш.
const legacyRoot = path.join(dist, legacyPrefix);
for (const entry of fs.readdirSync(dist, {withFileTypes: true})) {
  if (entry.name === legacyPrefix) {
    continue;
  }
  const from = path.join(dist, entry.name);
  const to = path.join(legacyRoot, entry.name);
  if (entry.isDirectory()) {
    copyDir(from, to);
  } else {
    fs.mkdirSync(legacyRoot, {recursive: true});
    fs.copyFileSync(from, to);
  }
}
console.log(`[postbuild] legacy mirror: /${legacyPrefix}/ (полная копия dist)`);

const indexPath = path.join(dist, 'index.html');
if (fs.existsSync(indexPath)) {
  const html = fs.readFileSync(indexPath, 'utf8');
  const site = process.env.IT_CODE_EXAMPLES_SITE ?? '';
  if (site.includes('code.spirzen.ru') && legacyBase === '/') {
    if (html.includes(`/${legacyPrefix}/styles/`)) {
      console.error(
        `[postbuild] ОШИБКА: сборка для code.spirzen.ru содержит /${legacyPrefix}/ в путях CSS.`,
      );
      console.error('Задайте IT_CODE_EXAMPLES_BASE=/ при build.');
      process.exit(1);
    }
    console.log('[postbuild] OK: канонические пути с BASE=/');
  }
}
