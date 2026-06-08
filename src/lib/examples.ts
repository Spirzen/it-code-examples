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

export type ExampleVersion = {
  label: string;
  dir: string;
  files: ExampleFile[];
};

export type ExampleMeta = {
  title?: string;
  description?: string;
  language?: string;
  tags?: string[];
  encyclopediaUrl?: string;
  order?: number;
  series?: string;
  seriesOrder?: number;
  seriesTitle?: string;
  versions?: {label: string; dir: string}[];
};

export type ExampleEntry = {
  slug: string;
  language: string;
  title: string;
  description: string;
  tags: string[];
  encyclopediaUrl?: string;
  order: number;
  series?: string;
  seriesOrder?: number;
  seriesTitle?: string;
  files: ExampleFile[];
  versions: ExampleVersion[];
  dir: string;
};

/** Лёгкая запись каталога — без содержимого файлов. */
export type CatalogEntry = {
  slug: string;
  language: string;
  title: string;
  description: string;
  tags: string[];
  encyclopediaUrl?: string;
  order: number;
  series?: string;
  seriesOrder?: number;
  seriesTitle?: string;
  fileCount: number;
  versionCount: number;
  /** Относительный путь от EXAMPLES_ROOT для быстрой загрузки примера. */
  dir: string;
};

export type SearchIndexEntry = {
  slug: string;
  title: string;
  description: string;
  tags: string[];
  language: string;
  series?: string;
  seriesTitle?: string;
  fileCount: number;
};

export type SeriesGroup = {
  id: string;
  title: string;
  examples: CatalogEntry[];
};

let catalogCache: CatalogEntry[] | null = null;

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

function listFiles(dir: string, base = dir, skipDirs = new Set<string>()): ExampleFile[] {
  const out: ExampleFile[] = [];
  for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
    if (entry.name === 'meta.json' || entry.name.startsWith('.')) {
      continue;
    }
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (skipDirs.has(entry.name)) {
        continue;
      }
      out.push(...listFiles(full, base, skipDirs));
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

function countCodeFiles(dir: string, skipDirs = new Set<string>()): number {
  let count = 0;
  for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
    if (entry.name === 'meta.json' || entry.name.startsWith('.')) {
      continue;
    }
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (skipDirs.has(entry.name)) {
        continue;
      }
      count += countCodeFiles(full, skipDirs);
      continue;
    }
    count++;
  }
  return count;
}

function loadVersions(dir: string, meta: ExampleMeta): ExampleVersion[] {
  if (!meta.versions?.length) {
    return [];
  }
  return meta.versions
    .map((v) => {
      const versionDir = path.join(dir, v.dir);
      if (!fs.existsSync(versionDir)) {
        return null;
      }
      const files = listFiles(versionDir, versionDir);
      if (files.length === 0) {
        return null;
      }
      return {label: v.label, dir: v.dir, files};
    })
    .filter((v): v is ExampleVersion => v !== null);
}

function sortCatalogEntries(a: CatalogEntry, b: CatalogEntry): number {
  if (a.language !== b.language) {
    return a.language.localeCompare(b.language, 'ru');
  }
  if (a.order !== b.order) {
    return a.order - b.order;
  }
  return a.title.localeCompare(b.title, 'ru');
}

function walkCatalogDirs(root: string, language: string, acc: CatalogEntry[] = []) {
  if (!fs.existsSync(root)) {
    return acc;
  }
  for (const entry of fs.readdirSync(root, {withFileTypes: true})) {
    if (!entry.isDirectory() || entry.name.startsWith('.')) {
      continue;
    }
    const dir = path.join(root, entry.name);
    const metaPath = path.join(dir, 'meta.json');
    const meta = readMeta(dir);
    const versionDirs = new Set((meta.versions ?? []).map((v) => v.dir));
    const hasCode = fs
      .readdirSync(dir)
      .some((f) => f !== 'meta.json' && !f.startsWith('.') && !versionDirs.has(f));
    if (hasCode || fs.existsSync(metaPath)) {
      const fileCount = countCodeFiles(dir, versionDirs);
      const versionCount = meta.versions?.filter((v) => fs.existsSync(path.join(dir, v.dir))).length ?? 0;
      if (fileCount === 0 && versionCount === 0) {
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
        series: meta.series,
        seriesOrder: meta.seriesOrder,
        seriesTitle: meta.seriesTitle,
        fileCount,
        versionCount,
        dir: path.relative(EXAMPLES_ROOT, dir).replace(/\\/g, '/'),
      });
    } else {
      walkCatalogDirs(dir, language, acc);
    }
  }
  return acc;
}

function loadExampleFromDir(dir: string, language: string, folderName: string): ExampleEntry | undefined {
  const meta = readMeta(dir);
  const versionDirs = new Set((meta.versions ?? []).map((v) => v.dir));
  const files = listFiles(dir, dir, versionDirs);
  const versions = loadVersions(dir, meta);
  if (files.length === 0 && versions.length === 0) {
    return undefined;
  }
  return {
    slug: `${language}/${folderName}`,
    language,
    title: meta.title ?? humanizeSlug(folderName),
    description: meta.description ?? '',
    tags: meta.tags ?? [],
    encyclopediaUrl: meta.encyclopediaUrl,
    order: meta.order ?? 999,
    series: meta.series,
    seriesOrder: meta.seriesOrder,
    seriesTitle: meta.seriesTitle,
    files,
    versions,
    dir,
  };
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
    const meta = readMeta(dir);
    const versionDirs = new Set((meta.versions ?? []).map((v) => v.dir));
    const hasCode = fs
      .readdirSync(dir)
      .some((f) => f !== 'meta.json' && !f.startsWith('.') && !versionDirs.has(f));
    if (hasCode || fs.existsSync(metaPath)) {
      const example = loadExampleFromDir(dir, language, entry.name);
      if (example) {
        acc.push(example);
      }
    } else {
      walkExampleDirs(dir, language, acc);
    }
  }
  return acc;
}

/** Каталог без содержимого файлов — для главной, поиска и списков. */
export function loadCatalog(): CatalogEntry[] {
  if (catalogCache) {
    return catalogCache;
  }
  if (!fs.existsSync(EXAMPLES_ROOT)) {
    catalogCache = [];
    return catalogCache;
  }
  const all: CatalogEntry[] = [];
  for (const langDir of fs.readdirSync(EXAMPLES_ROOT, {withFileTypes: true})) {
    if (!langDir.isDirectory() || langDir.name.startsWith('.')) {
      continue;
    }
    walkCatalogDirs(path.join(EXAMPLES_ROOT, langDir.name), langDir.name, all);
  }
  catalogCache = all.sort(sortCatalogEntries);
  return catalogCache;
}

/** Загрузка одного примера с файлами — для страниц /e/… */
export function loadExampleBySlug(slug: string): ExampleEntry | undefined {
  const entry = loadCatalog().find((e) => e.slug === slug);
  if (!entry) {
    return undefined;
  }
  const dir = path.join(EXAMPLES_ROOT, entry.dir);
  const folderName = entry.slug.slice(entry.language.length + 1);
  return loadExampleFromDir(dir, entry.language, folderName);
}

/** @deprecated Используйте loadCatalog / loadExampleBySlug */
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
  return loadExampleBySlug(slug);
}

export function groupByLanguage(examples: CatalogEntry[]) {
  const map = new Map<string, CatalogEntry[]>();
  for (const ex of examples) {
    const list = map.get(ex.language) ?? [];
    list.push(ex);
    map.set(ex.language, list);
  }
  return map;
}

export function groupBySeries(examples: CatalogEntry[]): SeriesGroup[] {
  const map = new Map<string, CatalogEntry[]>();
  for (const ex of examples) {
    if (!ex.series) {
      continue;
    }
    const list = map.get(ex.series) ?? [];
    list.push(ex);
    map.set(ex.series, list);
  }
  const groups: SeriesGroup[] = [];
  for (const [id, items] of map) {
    const sorted = [...items].sort((a, b) => {
      const ao = a.seriesOrder ?? 999;
      const bo = b.seriesOrder ?? 999;
      if (ao !== bo) {
        return ao - bo;
      }
      return a.title.localeCompare(b.title, 'ru');
    });
    groups.push({
      id,
      title: sorted[0]?.seriesTitle ?? humanizeSlug(id),
      examples: sorted,
    });
  }
  return groups.sort((a, b) => a.title.localeCompare(b.title, 'ru'));
}

export function getSeriesNeighbors(example: CatalogEntry | ExampleEntry, catalog: CatalogEntry[]) {
  if (!example.series) {
    return {prev: undefined, next: undefined, series: undefined};
  }
  const series = groupBySeries(catalog).find((g) => g.id === example.series);
  if (!series) {
    return {prev: undefined, next: undefined, series: undefined};
  }
  const idx = series.examples.findIndex((e) => e.slug === example.slug);
  return {
    prev: idx > 0 ? series.examples[idx - 1] : undefined,
    next: idx >= 0 && idx < series.examples.length - 1 ? series.examples[idx + 1] : undefined,
    series,
  };
}

export function buildSearchIndex(examples: CatalogEntry[]): SearchIndexEntry[] {
  return examples.map((ex) => ({
    slug: ex.slug,
    title: ex.title,
    description: ex.description,
    tags: ex.tags,
    language: ex.language,
    series: ex.series,
    seriesTitle: ex.seriesTitle,
    fileCount: ex.fileCount,
  }));
}
