import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dist = path.join(__dirname, '..', 'dist');
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

// Дублируем статику под /it-code-examples/ для старых HTML и кэша браузера.
const legacyRoot = path.join(dist, 'it-code-examples');
for (const dir of ['styles', 'scripts']) {
  const src = path.join(dist, dir);
  if (fs.existsSync(src)) {
    copyDir(src, path.join(legacyRoot, dir));
    console.log(`[postbuild] legacy mirror: /it-code-examples/${dir}/`);
  }
}

const indexPath = path.join(dist, 'index.html');
if (fs.existsSync(indexPath)) {
  const html = fs.readFileSync(indexPath, 'utf8');
  const site = process.env.IT_CODE_EXAMPLES_SITE ?? '';
  if (site.includes('code.spirzen.ru') && legacyBase === '/') {
    if (html.includes('/it-code-examples/styles/')) {
      console.error(
        '[postbuild] ОШИБКА: сборка для code.spirzen.ru содержит /it-code-examples/ в путях CSS.',
      );
      console.error('Задайте IT_CODE_EXAMPLES_BASE=/ при build.');
      process.exit(1);
    }
    console.log('[postbuild] OK: пути статики с BASE=/');
  }
}
