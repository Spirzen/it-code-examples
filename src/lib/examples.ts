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

export type SearchIndexEntry = {
  slug: string;
  title: string;
  description: string;
  tags: string[];
  language: string;
  series?: string;
  seriesTitle?: string;
  fileNames: string[];
};

export type SeriesGroup = {
  id: string;
  title: string;
  examples: ExampleEntry[];
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
      const files = listFiles(dir, dir, versionDirs);
      const versions = loadVersions(dir, meta);
      if (files.length === 0 && versions.length === 0) {
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
        files,
        versions,
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

export function groupBySeries(examples: ExampleEntry[]): SeriesGroup[] {
  const map = new Map<string, ExampleEntry[]>();
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

export function getSeriesNeighbors(example: ExampleEntry, examples: ExampleEntry[]) {
  if (!example.series) {
    return {prev: undefined, next: undefined, series: undefined};
  }
  const series = groupBySeries(examples).find((g) => g.id === example.series);
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

export function buildSearchIndex(examples: ExampleEntry[]): SearchIndexEntry[] {
  return examples.map((ex) => ({
    slug: ex.slug,
    title: ex.title,
    description: ex.description,
    tags: ex.tags,
    language: ex.language,
    series: ex.series,
    seriesTitle: ex.seriesTitle,
    fileNames: ex.files.map((f) => f.relativePath),
  }));
}
