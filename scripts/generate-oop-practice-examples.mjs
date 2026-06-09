/**
 * Генерирует учебные примеры ООП в examples/ и вставляет ExternalCodeEmbed в главы энциклопедии.
 *
 * Usage: node scripts/generate-oop-practice-examples.mjs [--dry-run]
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CODE_ROOT = path.join(__dirname, '..');
const SOURCES_ROOT = path.join(__dirname, 'oop-practice-sources');
const EXAMPLES_ROOT = path.join(CODE_ROOT, 'examples');
const KB_ROOT = path.join(CODE_ROOT, '..', 'it-knowledge-base');
const KB_DOCS = path.join(KB_ROOT, 'docs', 'encyclopedia');

const DRY_RUN = process.argv.includes('--dry-run');

const EXAMPLES = [
  {
    id: 'figure',
    title: 'Класс и объект',
    description: 'Чертёж класса Figure и конкретные объекты — круг и квадрат.',
    minHeight: 300,
  },
  {
    id: 'bank-account',
    title: 'Банковский счёт',
    description: 'Инкапсуляция: скрытое поле баланса и методы deposit/withdraw.',
    minHeight: 480,
  },
  {
    id: 'animal-inheritance',
    title: 'Наследование',
    description: 'Родитель Animal и дочерние Cat и Dog с общим eat() и своим speak().',
    minHeight: 420,
  },
  {
    id: 'smartphone',
    title: 'Смартфон',
    description: 'Состояние объекта: заряд батареи, звонки и подзарядка.',
    minHeight: 480,
  },
  {
    id: 'student',
    title: 'Студент',
    description: 'Список оценок, средний балл и проходной порог.',
    minHeight: 540,
  },
  {
    id: 'shop-cart',
    title: 'Корзина покупок',
    description: 'Взаимодействие Product, Cart и Order при оформлении заказа.',
    minHeight: 600,
  },
  {
    id: 'car',
    title: 'Автомобиль',
    description: 'Пробег, расход топлива и напоминание о техобслуживании.',
    minHeight: 480,
  },
  {
    id: 'user-auth',
    title: 'Пользователь',
    description: 'Скрытый пароль, вход в систему и публикация сообщений.',
    minHeight: 480,
  },
];

const LANG_EXT = {
  python: 'py',
  java: 'java',
  csharp: 'cs',
  cpp: 'cpp',
  php: 'php',
  kotlin: 'kt',
  groovy: 'groovy',
  rust: 'rs',
  swift: 'swift',
  lua: 'lua',
  smalltalk: 'st',
};

const MAIN_FILE = {
  python: 'main.py',
  java: 'main.java',
  csharp: 'main.cs',
  cpp: 'main.cpp',
  php: 'main.php',
  kotlin: 'main.kt',
  groovy: 'main.groovy',
  rust: 'main.rs',
  swift: 'main.swift',
  lua: 'main.lua',
  smalltalk: 'main.st',
};

/** @type {Array<{md: string, lang: string, slugPrefix: string, startNum: number, series: string, seriesTitle: string, encPath: string, tag: string, insertBefore: string}>} */
const CHAPTERS = [
  {
    md: '4-code-dev/4-08-oop/1.md',
    lang: 'python',
    slugPrefix: 'code-408-1',
    startNum: 9,
    series: 'code-408-1-practice',
    seriesTitle: 'ООП на практике',
    encPath: '/encyclopedia/4-code-dev/4-08-oop/1',
    tag: 'oop-practice',
    insertBefore:
      'Так, мы разобрались с ключевыми элементами ООП. Формальное определение парадигмы',
  },
  {
    md: '5-languages/5-02-python/26.md',
    lang: 'python',
    slugPrefix: 'py-502-26',
    startNum: 20,
    series: 'py-502-26-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-02-python/26',
    tag: '26',
    insertBefore: '## Паттерны проектирования',
  },
  {
    md: '5-languages/5-03-java/18.md',
    lang: 'java',
    slugPrefix: 'java-503-18',
    startNum: 32,
    series: 'java-503-18-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-03-java/18',
    tag: '18',
    insertBefore: null,
  },
  {
    md: '5-languages/5-05-csharp/25.md',
    lang: 'csharp',
    slugPrefix: 'csharp-505-25',
    startNum: 21,
    series: 'csharp-505-25-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-05-csharp/25',
    tag: '25',
    insertBefore: null,
  },
  {
    md: '5-languages/5-06-cpp/14.md',
    lang: 'cpp',
    slugPrefix: 'cpp-506-14',
    startNum: 19,
    series: 'cpp-506-14-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-06-cpp/14',
    tag: '14',
    insertBefore: null,
  },
  {
    md: '5-languages/5-07-php/18.md',
    lang: 'php',
    slugPrefix: 'php-507-18',
    startNum: 13,
    series: 'php-507-18-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-07-php/18',
    tag: '18',
    insertBefore: null,
  },
  {
    md: '5-languages/5-08-smalltalk/4.md',
    lang: 'smalltalk',
    slugPrefix: 'smalltalk-508-4',
    startNum: 3,
    series: 'smalltalk-508-4-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-08-smalltalk/4',
    tag: '4',
    insertBefore: null,
  },
  {
    md: '5-languages/5-09-kotlin/15.md',
    lang: 'kotlin',
    slugPrefix: 'kotlin-509-15',
    startNum: 2,
    series: 'kotlin-509-15-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-09-kotlin/15',
    tag: '15',
    insertBefore: null,
  },
  {
    md: '5-languages/5-12-groovy/15.md',
    lang: 'groovy',
    slugPrefix: 'groovy-512-15',
    startNum: 7,
    series: 'groovy-512-15-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-12-groovy/15',
    tag: '15',
    insertBefore: null,
  },
  {
    md: '5-languages/5-13-rust/141.md',
    lang: 'rust',
    slugPrefix: 'rust-513-141',
    startNum: 11,
    series: 'rust-513-141-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-13-rust/141',
    tag: '141',
    insertBefore: null,
  },
  {
    md: '5-languages/5-14-swift/102.md',
    lang: 'swift',
    slugPrefix: 'swift-514-102',
    startNum: 47,
    series: 'swift-514-102-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-14-swift/102',
    tag: '102',
    insertBefore: null,
  },
  {
    md: '5-languages/5-15-lua-i-luau/171.md',
    lang: 'lua',
    slugPrefix: 'lua-515-171',
    startNum: 22,
    series: 'lua-515-171-practice',
    seriesTitle: 'Учебные примеры ООП',
    encPath: '/encyclopedia/5-languages/5-15-lua-i-luau/171',
    tag: '171',
    insertBefore: null,
  },
];

const MARKER = '{/* oop-practice-examples */}';
const END_MARKER = '{/* /oop-practice-examples */}';

function padNum(n) {
  return String(n).padStart(3, '0');
}

function writeFile(filePath, content) {
  if (DRY_RUN) {
    console.log(`[dry-run] write ${filePath}`);
    return;
  }
  fs.mkdirSync(path.dirname(filePath), {recursive: true});
  fs.writeFileSync(filePath, content, 'utf8');
}

function createExample(lang, slug, exampleMeta, chapter, order) {
  const ext = LANG_EXT[lang];
  const srcPath = path.join(SOURCES_ROOT, lang, `${exampleMeta.id}.${ext}`);
  if (!fs.existsSync(srcPath)) {
    throw new Error(`Source not found: ${srcPath}`);
  }
  const code = fs.readFileSync(srcPath, 'utf8');
  const dir = path.join(EXAMPLES_ROOT, lang, slug);
  const meta = {
    title: `${chapter.seriesTitle} — ${exampleMeta.title}`,
    description: exampleMeta.description,
    tags: [lang, 'encyclopedia', 'oop-practice', chapter.tag],
    order,
    series: chapter.series,
    seriesOrder: order,
    seriesTitle: chapter.seriesTitle,
    encyclopediaUrl: `https://spirzen.ru${chapter.encPath}`,
  };
  writeFile(path.join(dir, 'meta.json'), `${JSON.stringify(meta, null, 2)}\n`);
  writeFile(path.join(dir, MAIN_FILE[lang]), code);
  return `${lang}/${slug}`;
}

function buildEmbedBlock(chapter, mappings) {
  const lines = [
    '',
    MARKER,
    '',
    '### Учебные примеры ООП',
    '',
    'Небольшие самодостаточные программы, которые показывают классы, объекты, инкапсуляцию, наследование и взаимодействие нескольких типов на одной предметной области.',
    '',
  ];
  for (let i = 0; i < EXAMPLES.length; i++) {
    const ex = EXAMPLES[i];
    const slug = mappings[i];
    lines.push(`#### ${ex.title}`);
    lines.push('');
    lines.push(ex.description);
    lines.push('');
    lines.push('');
    lines.push(
      `<ExternalCodeEmbed example="${slug}" title="${ex.title}" minHeight={${ex.minHeight}} />`,
    );
    lines.push('');
    lines.push('');
    if (i < EXAMPLES.length - 1) {
      lines.push('---');
      lines.push('');
    }
  }
  lines.push('');
  lines.push(END_MARKER);
  lines.push('');
  return lines.join('\n');
}

function patchMarkdown(chapter, mappings) {
  const mdPath = path.join(KB_DOCS, chapter.md);
  if (!fs.existsSync(mdPath)) {
    throw new Error(`Markdown not found: ${mdPath}`);
  }
  let body = fs.readFileSync(mdPath, 'utf8');
  const block = buildEmbedBlock(chapter, mappings);

  if (body.includes(MARKER)) {
    const start = body.indexOf(MARKER);
    const endMarkerPos = body.indexOf(END_MARKER, start);
    const replaceEnd =
      endMarkerPos > start ? endMarkerPos + END_MARKER.length : body.length;
    body =
      body.slice(0, start) +
      block.trimEnd() +
      body.slice(replaceEnd).replace(/^\n+/, '\n');
  } else if (chapter.insertBefore && body.includes(chapter.insertBefore)) {
    const idx = body.indexOf(chapter.insertBefore);
    body = body.slice(0, idx) + block + body.slice(idx);
  } else {
    body = body.trimEnd() + '\n\n' + block;
  }

  if (DRY_RUN) {
    console.log(`[dry-run] patch ${mdPath}`);
    return;
  }
  fs.writeFileSync(mdPath, body, 'utf8');
  console.log(`patched ${chapter.md}`);
}

function main() {
  for (const chapter of CHAPTERS) {
    const mappings = [];
    for (let i = 0; i < EXAMPLES.length; i++) {
      const num = chapter.startNum + i;
      const slug = `${chapter.slugPrefix}-${padNum(num)}`;
      const embedSlug = createExample(chapter.lang, slug, EXAMPLES[i], chapter, i + 1);
      mappings.push(embedSlug);
      console.log(`created ${embedSlug}`);
    }
    patchMarkdown(chapter, mappings);
  }
  console.log('done');
}

main();
