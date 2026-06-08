/**
 * Извлекает тяжёлые листинги из docs/encyclopedia/3-data-markup/3-11-analiz-dannyh
 * (it-knowledge-base) в examples/ и заменяет на ExternalCodeEmbed.
 *
 * Usage:
 *   node scripts/migrate-data-analysis-examples-from-kb.mjs [--dry-run] [--min-lines=15] [--only=424.md]
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CODE_ROOT = path.join(__dirname, '..');
const KB_ROOT = path.join(CODE_ROOT, '..', 'it-knowledge-base');
const KB_DIR = path.join(KB_ROOT, 'docs', 'encyclopedia', '3-data-markup', '3-11-analiz-dannyh');
const EXAMPLES_ROOT = path.join(CODE_ROOT, 'examples');
const MANIFEST_PATH = path.join(__dirname, 'data-analysis-examples-manifest.json');
const ENCYCLOPEDIA_BASE = '/encyclopedia/3-data-markup/3-11-analiz-dannyh';

const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const ONLY = args.find((a) => a.startsWith('--only='))?.slice('--only='.length);
const MIN_LINES = Number(args.find((a) => a.startsWith('--min-lines='))?.slice('--min-lines='.length) ?? 15);

const SKIP_FILES = new Set(['intro.md', '998.md', '999.md']);

const SKIP_FENCE_LANGS = new Set(['text', 'plain', 'mermaid', 'scratch', 'regex', '']);

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
  csharp: 'csharp',
  cs: 'csharp',
  java: 'java',
  cpp: 'cpp',
  c: 'cpp',
  html: 'html',
  css: 'css',
  yaml: 'yaml',
  yml: 'yaml',
  sql: 'sql',
  plpgsql: 'sql',
  tsql: 'sql',
  mysql: 'sql',
  psql: 'bash',
  cql: 'sql',
  cypher: 'javascript',
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
  groovy: 'groovy',
  php: 'php',
  pascal: 'pascal',
  latex: 'latex',
  tex: 'latex',
  lua: 'lua',
  luau: 'lua',
  dart: 'dart',
  flutter: 'dart',
  vue: 'vue',
  svelte: 'svelte',
  nginx: 'nginx',
  promql: 'promql',
  mcfunction: 'mcfunction',
  cmd: 'batch',
  batch: 'batch',
  r: 'r',
  http: 'http',
  dax: 'dax',
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
  csharp: 'cs',
  cs: 'cs',
  java: 'java',
  cpp: 'cpp',
  c: 'c',
  html: 'html',
  css: 'css',
  yaml: 'yaml',
  yml: 'yml',
  sql: 'sql',
  plpgsql: 'sql',
  tsql: 'sql',
  mysql: 'sql',
  psql: 'sh',
  cql: 'cql',
  cypher: 'cypher',
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
  groovy: 'groovy',
  php: 'php',
  pascal: 'pas',
  latex: 'tex',
  tex: 'tex',
  lua: 'lua',
  luau: 'lua',
  dart: 'dart',
  flutter: 'dart',
  vue: 'vue',
  svelte: 'svelte',
  nginx: 'conf',
  promql: 'promql',
  mcfunction: 'mcfunction',
  cmd: 'cmd',
  batch: 'cmd',
  r: 'r',
  http: 'http',
  dax: 'dax',
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
  let last = {level: 2, title: 'intro', anchor: 'intro'};
  let spanAnchor = '';

  const lines = before.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const span = line.match(/<span id="([^"]+)"/);
    if (span) spanAnchor = span[1];
    const h = line.match(/^(#{2,4})\s+(.+)$/);
    if (h) {
      last = {
        level: h[1].length,
        title: h[2].trim(),
        anchor: spanAnchor || slugify(h[2]),
      };
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

function extractBlocks(body) {
  const blocks = [];
  const re = /```(\w*)\r?\n([\s\S]*?)```/g;
  let m;
  while ((m = re.exec(body))) {
    const fenceLang = m[1];
    const code = m[2].replace(/\r\n/g, '\n');
    const lineCount = code.split('\n').length;
    const folderLang = mapLang(fenceLang);
    if (!folderLang || lineCount < MIN_LINES) continue;

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

function articleId(filename) {
  return filename.replace(/\.md$/, '');
}

function buildDocUrl(article) {
  return `https://spirzen.ru${ENCYCLOPEDIA_BASE}/${article}`;
}

function groupBlocks(blocks) {
  const groups = new Map();
  for (const block of blocks) {
    const key = `${block.section.level}:${block.section.anchor}:${block.section.title}`;
    const list = groups.get(key) ?? {section: block.section, blocks: []};
    list.blocks.push(block);
    groups.set(key, list);
  }
  return [...groups.values()];
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

function processArticle(filePath) {
  const filename = path.basename(filePath);
  if (SKIP_FILES.has(filename)) return null;

  const raw = fs.readFileSync(filePath, 'utf8');
  const normalized = raw.replace(/\r\n/g, '\n');
  const {meta, body} = parseFrontmatter(normalized);
  const blocks = extractBlocks(body);
  if (!blocks.length) return null;

  const art = articleId(filename);
  const docUrl = buildDocUrl(art);
  const seriesId = `da-${art}`;
  const seriesTitle = meta.title ?? `Анализ данных ${art}`;
  const groups = groupBlocks(blocks);

  const manifestEntries = [];
  const replacements = [];
  let seriesOrder = 0;

  for (const group of groups) {
    seriesOrder += 1;
    const slugName = `da-${art}-${String(seriesOrder).padStart(3, '0')}`;
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
        tags: ['data-analysis', 'encyclopedia', art],
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
      `[dry-run] update ${filename}: ${replacements.length} embed(s), ${blocks.length} block(s)`,
    );
  }

  return manifestEntries;
}

function main() {
  if (!fs.existsSync(KB_DIR)) {
    throw new Error(`KB data-analysis dir not found: ${KB_DIR}`);
  }

  const files = fs
    .readdirSync(KB_DIR)
    .filter((f) => f.endsWith('.md'))
    .filter((f) => !SKIP_FILES.has(f))
    .filter((f) => !ONLY || f === ONLY || f === `${ONLY}.md`);

  const manifest = {
    generatedAt: new Date().toISOString(),
    minLines: MIN_LINES,
    encyclopediaPath: ENCYCLOPEDIA_BASE,
    articles: {},
  };

  let totalExamples = 0;
  let totalBlocks = 0;

  for (const file of files) {
    const full = path.join(KB_DIR, file);
    const entries = processArticle(full);
    if (!entries?.length) continue;
    manifest.articles[articleId(file)] = entries;
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
