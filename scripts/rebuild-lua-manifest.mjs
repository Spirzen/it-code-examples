/**
 * Восстанавливает lua-examples-manifest.json из examples/lua/lua-515-*.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const EXAMPLES_ROOT = path.join(__dirname, '..', 'examples');
const MANIFEST_PATH = path.join(__dirname, 'lua-examples-manifest.json');

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/<[^>]+>/g, '')
    .replace(/[`"'«»]/g, '')
    .replace(/[^a-z0-9а-яё]+/gi, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 48);
}

function lineCount(dir) {
  const preferred = ['main.lua', 'main.cpp', 'main.c', 'main.txt', 'main.sh'];
  for (const name of preferred) {
    const file = path.join(dir, name);
    if (fs.existsSync(file)) {
      return fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n').split('\n').length;
    }
  }
  const first = fs
    .readdirSync(dir)
    .find((f) => /\.(lua|cpp|c|txt|sh|py|js|ts|cs|java|rb|go|rs)$/i.test(f));
  if (!first) return 0;
  return fs.readFileSync(path.join(dir, first), 'utf8').replace(/\r\n/g, '\n').split('\n').length;
}

const articles = {};

for (const lang of fs.readdirSync(EXAMPLES_ROOT)) {
  const langDir = path.join(EXAMPLES_ROOT, lang);
  if (!fs.statSync(langDir).isDirectory()) continue;

  for (const name of fs.readdirSync(langDir).filter((d) => d.startsWith('lua-515-'))) {
    const dir = path.join(langDir, name);
    const meta = JSON.parse(fs.readFileSync(path.join(dir, 'meta.json'), 'utf8'));
    const articleTag = meta.tags?.find((t) => /^\d+$/.test(t));
    if (!articleTag) continue;

    const titlePart = meta.title.includes(' — ') ? meta.title.split(' — ').pop() : meta.title;
    const entry = {
      article: articleTag,
      slug: `${lang}/${name}`,
    title: titlePart.trim(),
    section: slugify(titlePart),
    blocks: 1,
    lines: lineCount(dir),
  };

    if (!articles[articleTag]) articles[articleTag] = [];
    articles[articleTag].push(entry);
  }
}

for (const list of Object.values(articles)) {
  list.sort((a, b) => a.slug.localeCompare(b.slug, 'en'));
}

const manifest = {
  generatedAt: new Date().toISOString(),
  minLines: 15,
  encyclopediaPath: '/encyclopedia/5-languages/5-15-lua-i-luau',
  articles,
};

fs.writeFileSync(MANIFEST_PATH, `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');

const total = Object.values(articles).flat().length;
console.log(`Rebuilt manifest: ${total} example(s) in ${Object.keys(articles).length} article(s).`);
