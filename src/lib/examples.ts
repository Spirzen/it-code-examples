import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {langFromFilename} from './languages';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
export const EXAMPLES_ROOT = path.join(__dirname, '..', '..', 'examples');

export type ExampleFile = {
  name: string;
  relativePath: string;
  language: string;
  content: string;
};

export type ExampleMeta = {
  title?: string;
  description?: string;
  language?: string;
  tags?: string[];
  encyclopediaUrl?: string;
  order?: number;
};

export type ExampleEntry = {
  slug: string;
  language: string;
  title: string;
  description: string;
  tags: string[];
  encyclopediaUrl?: string;
  order: number;
  files: ExampleFile[];
  dir: string;
};

function readMeta(dir: string): ExampleMeta {
  const metaPath = path.join(dir, 'meta.json');
  if (!fs.existsSync(metaPath)) {
    return {};
  }
  try {
    return JSON.parse(fs.readFileSync(metaPath, 'utf8')) as ExampleMeta;
  } catch {
    return {};
  }
}

function humanizeSlug(part: string): string {
  return part
    .split('-')
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(' ');
}

function listFiles(dir: string, base = dir): ExampleFile[] {
  const out: ExampleFile[] = [];
  for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
    if (entry.name === 'meta.json' || entry.name.startsWith('.')) {
      continue;
    }
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      out.push(...listFiles(full, base));
      continue;
    }
    const content = fs.readFileSync(full, 'utf8');
    out.push({
      name: entry.name,
      relativePath: path.relative(base, full).replace(/\\/g, '/'),
      language: langFromFilename(entry.name),
      content,
    });
  }
  return out.sort((a, b) => a.relativePath.localeCompare(b.relativePath, 'ru'));
}

function walkExampleDirs(root: string, language: string, acc: ExampleEntry[] = []) {
  if (!fs.existsSync(root)) {
    return acc;
  }
  for (const entry of fs.readdirSync(root, {withFileTypes: true})) {
    if (!entry.isDirectory() || entry.name.startsWith('.')) {
      continue;
    }
    const dir = path.join(root, entry.name);
    const metaPath = path.join(dir, 'meta.json');
    const hasCode = fs
      .readdirSync(dir)
      .some((f) => f !== 'meta.json' && !f.startsWith('.'));
    if (hasCode || fs.existsSync(metaPath)) {
      const meta = readMeta(dir);
      const files = listFiles(dir);
      if (files.length === 0) {
        continue;
      }
      const slug = `${language}/${entry.name}`;
      acc.push({
        slug,
        language,
        title: meta.title ?? humanizeSlug(entry.name),
        description: meta.description ?? '',
        tags: meta.tags ?? [],
        encyclopediaUrl: meta.encyclopediaUrl,
        order: meta.order ?? 999,
        files,
        dir,
      });
    } else {
      walkExampleDirs(dir, language, acc);
    }
  }
  return acc;
}

export function loadAllExamples(): ExampleEntry[] {
  if (!fs.existsSync(EXAMPLES_ROOT)) {
    return [];
  }
  const all: ExampleEntry[] = [];
  for (const langDir of fs.readdirSync(EXAMPLES_ROOT, {withFileTypes: true})) {
    if (!langDir.isDirectory() || langDir.name.startsWith('.')) {
      continue;
    }
    walkExampleDirs(path.join(EXAMPLES_ROOT, langDir.name), langDir.name, all);
  }
  return all.sort((a, b) => {
    if (a.language !== b.language) {
      return a.language.localeCompare(b.language, 'ru');
    }
    if (a.order !== b.order) {
      return a.order - b.order;
    }
    return a.title.localeCompare(b.title, 'ru');
  });
}

export function getExampleBySlug(slug: string): ExampleEntry | undefined {
  return loadAllExamples().find((e) => e.slug === slug);
}

export function groupByLanguage(examples: ExampleEntry[]) {
  const map = new Map<string, ExampleEntry[]>();
  for (const ex of examples) {
    const list = map.get(ex.language) ?? [];
    list.push(ex);
    map.set(ex.language, list);
  }
  return map;
}
