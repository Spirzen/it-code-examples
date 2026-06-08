/**
 * Извлекает тяжёлые листинги из разделов 7-project энциклопедии
 * (it-knowledge-base) в examples/ и заменяет на ExternalCodeEmbed.
 *
 * Обрабатывает подразделы:
 *   7-01-obschee-o-biznese, 7-02-komanda-i-upravlenie, 7-03-metodologiya-i-zhiznennyy-tsikl-po,
 *   7-04-analitika, 7-05-testirovanie, 7-06-proektirovanie-i-arhitektura, 7-07-intellektualnye-prava, 7-08-tehnicheskoe-pismo,
 *   7-09-bazy-znaniy-i-zadachniki, 7-10-kultura-koda, 7-11-legasi-kod, 7-12-konstruirovanie-po,
 *   7-13-ekonomika-proizvodstva-po, 7-14-scrum, 7-15-vnedrenie-erp-sistem, 7-16-itsm-i-it-uslugi
 *
 * Короткие фрагменты, mermaid и text остаются в статье (min-lines по умолчанию 15).
 *
 * Usage:
 *   node scripts/migrate-project-7-examples-from-kb.mjs [--dry-run] [--min-lines=15] [--subdir=7-04-analitika] [--only=7-08-tehnicheskoe-pismo/20.md]
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CODE_ROOT = path.join(__dirname, '..');
const KB_ROOT = path.join(CODE_ROOT, '..', 'it-knowledge-base');
const KB_BASE = path.join(KB_ROOT, 'docs', 'encyclopedia', '7-project');
const EXAMPLES_ROOT = path.join(CODE_ROOT, 'examples');
const MANIFEST_PATH = path.join(__dirname, 'project-7-examples-manifest.json');
const ENCYCLOPEDIA_BASE = '/encyclopedia/7-project';

const KB_SUBDIRS = [
  '7-01-obschee-o-biznese',
  '7-02-komanda-i-upravlenie',
  '7-03-metodologiya-i-zhiznennyy-tsikl-po',
  '7-04-analitika',
  '7-05-testirovanie',
  '7-06-proektirovanie-i-arhitektura',
  '7-07-intellektualnye-prava',
  '7-08-tehnicheskoe-pismo',
  '7-09-bazy-znaniy-i-zadachniki',
  '7-10-kultura-koda',
  '7-11-legasi-kod',
  '7-12-konstruirovanie-po',
  '7-13-ekonomika-proizvodstva-po',
  '7-14-scrum',
  '7-15-vnedrenie-erp-sistem',
  '7-16-itsm-i-it-uslugi',
];

const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const ONLY = args.find((a) => a.startsWith('--only='))?.slice('--only='.length);
const SUBDIR = args.find((a) => a.startsWith('--subdir='))?.slice('--subdir='.length);
const MIN_LINES = Number(args.find((a) => a.startsWith('--min-lines='))?.slice('--min-lines='.length) ?? 15);

const SKIP_FILES = new Set(['intro.md', '998.md', '999.md', '1001.md']);

const SKIP_FENCE_LANGS = new Set([
  'text',
  'plain',
  'plaintext',
  'mermaid',
  'scratch',
  'regex',
  'txt',
  'markdown',
  'prompt',
  'env',
  '',
]);

const FENCE_TO_FOLDER = {
  python: 'python',
  py: 'python',
  bash: 'bash',
  sh: 'bash',
  shell: 'bash',
  javascript: 'javascript',
  js: 'javascript',
  jsx: 'javascript',
  ts: 'typescript',
  typescript: 'typescript',
  tsx: 'typescript',
  csharp: 'csharp',
  cs: 'csharp',
  java: 'java',
  cpp: 'cpp',
  'c++': 'cpp',
  c: 'cpp',
  html: 'html',
  css: 'css',
  yaml: 'yaml',
  yml: 'yaml',
  sql: 'sql',
  plpgsql: 'sql',
  tsql: 'sql',
  mysql: 'sql',
  dockerfile: 'dockerfile',
  xml: 'xml',
  xaml: 'xml',
  json: 'json',
  powershell: 'powershell',
  ps1: 'powershell',
  go: 'go',
  rust: 'rust',
  ruby: 'ruby',
  kotlin: 'kotlin',
  swift: 'swift',
  groovy: 'groovy',
  php: 'php',
  dart: 'dart',
  flutter: 'dart',
  vue: 'vue',
  svelte: 'svelte',
  properties: 'text',
  iss: 'text',
  mdx: 'text',
  cmd: 'batch',
  batch: 'batch',
  gitignore: 'text',
  gitattributes: 'text',
  ini: 'text',
  nginx: 'nginx',
  graphql: 'javascript',
  diff: 'text',
  toml: 'text',
  kv: 'text',
  pseudocode: 'text',
  bsl: 'text',
  '1c': 'text',
};

const FENCE_TO_EXT = {
  python: 'py',
  py: 'py',
  bash: 'sh',
  sh: 'sh',
  shell: 'sh',
  javascript: 'js',
  js: 'js',
  jsx: 'jsx',
  ts: 'ts',
  typescript: 'ts',
  tsx: 'tsx',
  csharp: 'cs',
  cs: 'cs',
  java: 'java',
  cpp: 'cpp',
  'c++': 'cpp',
  c: 'c',
  html: 'html',
  css: 'css',
  yaml: 'yaml',
  yml: 'yml',
  sql: 'sql',
  plpgsql: 'sql',
  tsql: 'sql',
  mysql: 'sql',
  dockerfile: 'dockerfile',
  xml: 'xml',
  xaml: 'xaml',
  json: 'json',
  powershell: 'ps1',
  ps1: 'ps1',
  go: 'go',
  rust: 'rs',
  ruby: 'rb',
  kotlin: 'kt',
  swift: 'swift',
  groovy: 'groovy',
  php: 'php',
  dart: 'dart',
  flutter: 'dart',
  vue: 'vue',
  svelte: 'svelte',
  properties: 'properties',
  iss: 'iss',
  mdx: 'mdx',
  cmd: 'cmd',
  batch: 'cmd',
  gitignore: 'gitignore',
  gitattributes: 'gitattributes',
  ini: 'ini',
  nginx: 'conf',
  graphql: 'graphql',
  diff: 'diff',
  toml: 'toml',
  kv: 'txt',
  pseudocode: 'pseudo',
  bsl: 'bsl',
  '1c': 'bsl',
};

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/<[^>]+>/g, '')
    .replace(/[`"'«»]/g, '')
    .replace(/[^a-z0-9а-яё]+/gi, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 48);
}

function parseFrontmatter(raw) {
  if (!raw.startsWith('---\n')) return {meta: {}, body: raw};
  const end = raw.indexOf('\n---\n', 4);
  if (end < 0) return {meta: {}, body: raw};
  const fm = raw.slice(4, end);
  const body = raw.slice(end + 5);
  const meta = {};
  for (const line of fm.split('\n')) {
    const m = line.match(/^([a-zA-Z_]+):\s*"?(.+?)"?\s*$/);
    if (m) meta[m[1]] = m[2].replace(/^"|"$/g, '');
  }
  return {meta, body};
}

function findSectionKey(body, blockStart) {
  const before = body.slice(0, blockStart);
  let lastH2 = {level: 2, title: 'intro', anchor: 'intro'};
  let last = {level: 2, title: 'intro', anchor: 'intro', h2: lastH2};
  let spanAnchor = '';

  const lines = before.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const span = line.match(/<span id="([^"]+)"/);
    if (span) spanAnchor = span[1];
    const h = line.match(/^(#{2,4})\s+(.+)$/);
    if (h) {
      const level = h[1].length;
      const title = h[2].trim();
      const anchor = spanAnchor || slugify(h[2]);
      if (level === 2) {
        lastH2 = {level, title, anchor};
      }
      last = {level, title, anchor, h2: lastH2};
      spanAnchor = '';
    }
  }

  return last;
}

function mapLang(fenceLang) {
  const key = (fenceLang || '').toLowerCase();
  if (SKIP_FENCE_LANGS.has(key)) return null;
  return FENCE_TO_FOLDER[key] ?? 'text';
}

function extractAllCodeBlocks(body) {
  const blocks = [];
  const re = /```(\w*)\r?\n([\s\S]*?)```/g;
  let m;
  while ((m = re.exec(body))) {
    const fenceLang = m[1];
    const code = m[2].replace(/\r\n/g, '\n');
    const lineCount = code.split('\n').length;
    const folderLang = mapLang(fenceLang);
    if (!folderLang) continue;

    const section = findSectionKey(body, m.index);
    blocks.push({
      full: m[0],
      start: m.index,
      end: m.index + m[0].length,
      fenceLang,
      folderLang,
      code,
      lineCount,
      section,
    });
  }
  return blocks;
}

function selectMigratableGroups(allBlocks) {
  return allBlocks
    .filter((b) => b.lineCount >= MIN_LINES)
    .map((block) => ({section: block.section, blocks: [block]}));
}

function articleKey(relativePath) {
  return relativePath.replace(/\.md$/, '').replace(/[\\/]/g, '-');
}

function buildDocUrl(relativePath) {
  const slug = relativePath.replace(/\.md$/, '').replace(/\\/g, '/');
  return `https://spirzen.ru${ENCYCLOPEDIA_BASE}/${slug}`;
}

function primaryLang(blocks) {
  const counts = new Map();
  for (const b of blocks) {
    counts.set(b.folderLang, (counts.get(b.folderLang) ?? 0) + 1);
  }
  return [...counts.entries()].sort((a, b) => b[1] - a[1])[0][0];
}

function writeExampleDir({slug, language, files, meta}) {
  const dir = path.join(EXAMPLES_ROOT, language, slug.split('/').pop());
  if (DRY_RUN) {
    console.log(`[dry-run] example ${language}/${slug.split('/').pop()} (${files.length} file(s))`);
    return;
  }
  fs.mkdirSync(dir, {recursive: true});
  for (const file of files) {
    fs.writeFileSync(path.join(dir, file.name), file.content, 'utf8');
  }
  fs.writeFileSync(path.join(dir, 'meta.json'), `${JSON.stringify(meta, null, 2)}\n`, 'utf8');
}

function buildEmbedTag(slug, title, minHeight) {
  const safeTitle = title.replace(/"/g, '&quot;');
  const minPart = minHeight ? ` minHeight={${minHeight}}` : '';
  return `<ExternalCodeEmbed example="${slug}" title="${safeTitle}"${minPart} />`;
}

function ensureCodeImport(content) {
  if (content.includes('import ExternalCodeEmbed')) return content;
  const fmEnd = content.indexOf('---', content.indexOf('---') + 3);
  const insertAt = fmEnd >= 0 ? fmEnd + 3 : 0;
  return (
    content.slice(0, insertAt) +
    "\n\nimport ExternalCodeEmbed from '@site/src/components/ExternalCodeEmbed';\n" +
    content.slice(insertAt)
  );
}

function estimateMinHeight(lineCount) {
  return Math.min(720, Math.max(160, 48 + lineCount * 18));
}

function processArticle(filePath, relativePath) {
  const filename = path.basename(filePath);
  if (SKIP_FILES.has(filename)) return null;

  const raw = fs.readFileSync(filePath, 'utf8');
  const normalized = raw.replace(/\r\n/g, '\n');
  const {meta, body} = parseFrontmatter(normalized);
  const allBlocks = extractAllCodeBlocks(body);
  const groups = selectMigratableGroups(allBlocks);
  if (!groups.length) return null;

  const art = articleKey(relativePath);
  const docUrl = buildDocUrl(relativePath);
  const seriesId = `project-7-${art}`;
  const seriesTitle = meta.title ?? `Проект ${art}`;

  const manifestEntries = [];
  const replacements = [];
  let seriesOrder = 0;

  for (const group of groups) {
    seriesOrder += 1;
    const slugName = `project-7-${art}-${String(seriesOrder).padStart(3, '0')}`;
    const language = primaryLang(group.blocks);
    const exampleSlug = `${language}/${slugName}`;

    const files = group.blocks.map((block, idx) => {
      const ext = FENCE_TO_EXT[block.fenceLang.toLowerCase()] ?? 'txt';
      const name =
        group.blocks.length === 1
          ? `main.${ext}`
          : `part-${String(idx + 1).padStart(2, '0')}.${ext}`;
      return {name, content: block.code};
    });

    const totalLines = group.blocks.reduce((n, b) => n + b.lineCount, 0);
    const title =
      group.section.title.replace(/^#+\s*/, '').replace(/\{#.+\}/, '').trim() ||
      `Пример ${seriesOrder}`;

    writeExampleDir({
      slug: exampleSlug,
      language,
      files,
      meta: {
        title: `${seriesTitle} — ${title}`,
        description: `Фрагмент из «${seriesTitle}»: ${title}.`,
        tags: ['project', 'encyclopedia', art],
        order: seriesOrder,
        series: seriesId,
        seriesOrder,
        seriesTitle,
        encyclopediaUrl: docUrl,
      },
    });

    const embed = buildEmbedTag(exampleSlug, title, estimateMinHeight(totalLines));
    manifestEntries.push({
      article: art,
      slug: exampleSlug,
      title,
      section: group.section.anchor,
      blocks: group.blocks.length,
      lines: totalLines,
    });

    replacements.push({
      blocks: group.blocks,
      embed,
    });
  }

  let outBody = body;
  for (const rep of replacements.sort((a, b) => b.blocks[0].start - a.blocks[0].start)) {
    const first = rep.blocks[0];
    const last = rep.blocks[rep.blocks.length - 1];
    outBody = `${outBody.slice(0, first.start)}\n\n${rep.embed}\n\n${outBody.slice(last.end)}`;
  }

  const fmMatch = normalized.match(/^---\n([\s\S]*?)\n---\n/);
  let outDoc = fmMatch ? `---\n${fmMatch[1]}\n---\n${outBody}` : outBody;
  outDoc = ensureCodeImport(outDoc);

  if (!DRY_RUN) {
    fs.writeFileSync(filePath, outDoc.replace(/\n/g, '\r\n'), 'utf8');
  } else {
    console.log(
      `[dry-run] update ${relativePath}: ${replacements.length} embed(s), ${replacements.reduce((n, r) => n + r.blocks.length, 0)} block(s)`,
    );
  }

  return manifestEntries;
}

function loadExistingManifest() {
  if (!fs.existsSync(MANIFEST_PATH)) return null;
  return JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
}

function collectMarkdownFiles() {
  const entries = [];
  const subdirs = SUBDIR ? [SUBDIR] : KB_SUBDIRS;
  for (const subdir of subdirs) {
    const dir = path.join(KB_BASE, subdir);
    if (!fs.existsSync(dir)) {
      console.warn(`Skip missing dir: ${subdir}`);
      continue;
    }
    entries.push(...collectMarkdownFilesInDir(dir, subdir));
  }
  return entries;
}

function collectMarkdownFilesInDir(dir, subdirPrefix, baseDir = dir) {
  const entries = [];
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      entries.push(...collectMarkdownFilesInDir(full, subdirPrefix, baseDir));
      continue;
    }
    if (!name.endsWith('.md')) continue;
    const relativePath = path.relative(path.join(KB_BASE), full).replace(/\\/g, '/');
    entries.push({full, relativePath});
  }
  return entries;
}

function matchesOnly(relativePath) {
  if (!ONLY) return true;
  const normalized = ONLY.replace(/\\/g, '/');
  return (
    relativePath === normalized ||
    relativePath === `${normalized}.md` ||
    path.basename(relativePath) === normalized ||
    path.basename(relativePath) === `${normalized}.md`
  );
}

function main() {
  if (!fs.existsSync(KB_BASE)) {
    throw new Error(`KB 7-project dir not found: ${KB_BASE}`);
  }

  const files = collectMarkdownFiles()
    .filter(({relativePath}) => !SKIP_FILES.has(path.basename(relativePath)))
    .filter(({relativePath}) => matchesOnly(relativePath));

  const existingManifest = loadExistingManifest();
  const manifest = {
    generatedAt: new Date().toISOString(),
    minLines: MIN_LINES,
    encyclopediaPath: ENCYCLOPEDIA_BASE,
    subdirs: KB_SUBDIRS,
    articles: {...(existingManifest?.articles ?? {})},
  };

  let totalExamples = 0;
  let totalBlocks = 0;

  for (const {full, relativePath} of files) {
    const entries = processArticle(full, relativePath);
    if (!entries?.length) continue;
    manifest.articles[articleKey(relativePath)] = entries;
    totalExamples += entries.length;
    totalBlocks += entries.reduce((n, e) => n + e.blocks, 0);
  }

  if (!DRY_RUN) {
    fs.writeFileSync(MANIFEST_PATH, `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');
  }

  console.log(
    `Done. ${totalExamples} example(s) from ${totalBlocks} block(s) across ${Object.keys(manifest.articles).length} article(s)${DRY_RUN ? ' (dry-run)' : ''}.`,
  );
  if (!DRY_RUN) console.log(`Manifest: ${MANIFEST_PATH}`);
}

main();
