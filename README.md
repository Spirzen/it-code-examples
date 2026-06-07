# IT Code Examples

**Каталог примеров кода для [Вселенной IT](https://spirzen.ru/)**

| | |
|---|---|
| Публичный сайт | [code.spirzen.ru](https://code.spirzen.ru/) |
| Энциклопедия | [spirzen.ru](https://spirzen.ru/) |
| Репозиторий энциклопедии | [it-knowledge-base](https://github.com/spirzen/it-knowledge-base) |

Длинные листинги и мультифайловые практикумы живут здесь; в статьях — текст и встроенный просмотрщик через iframe. Отдельный репозиторий даёт второй лимит GitHub Pages и не раздувает билд Docusaurus.

---

## Возможности

- **Каталог** с поиском и фильтром по языку
- **Практикумы (серии)** — несколько связанных примеров с навигацией шаг 1…N
- **Версии и diff** — сравнение папок `v1/`, `v2/` из `meta.json`
- **Мультифайловые примеры** — вкладки, «Копировать все»
- **Копирование** и **полноэкранный просмотр** кода
- **Светлая / тёмная тема** — синхрон с Docusaurus (`localStorage.theme`, `postMessage`)
- **Embed** для iframe в энциклопедии

Подробности для агентов и авторов — в [AGENTS.md](AGENTS.md).

---

## Стек

| Область | Технология |
|---------|------------|
| Сборка | [Astro 5](https://astro.build/) (статический output) |
| Подсветка | [Shiki](https://shiki.style/) на этапе сборки (light + dark) |
| Runtime JS | Вкладки, поиск, тема, копирование, fullscreen, resize iframe |
| Node.js | ≥ 20 |
| Деплой | GitHub Actions → GitHub Pages |

---

## Быстрый старт

**Windows:** `start.bat` — проверит Node.js, при необходимости `npm install`, запустит dev на порту 4321.

```bash
git clone https://github.com/spirzen/it-code-examples.git
cd it-code-examples
npm install
npm run dev
```

Откройте [http://localhost:4321/](http://localhost:4321/).

```bash
npm run build    # dist/
npm run preview  # проверка сборки
```

---

## Структура репозитория

```
it-code-examples/
├── examples/                    # единственный источник контента
│   └── <язык>/
│       └── <slug>/
│           ├── meta.json
│           ├── *.ext            # исходники
│           ├── v1/, v2/         # опционально: версии для diff
│           └── …
├── src/
│   ├── lib/
│   │   ├── examples.ts          # сканер, серии, поиск
│   │   ├── diff.ts              # построчный diff
│   │   └── languages.ts
│   ├── components/
│   │   ├── CodeBlock.astro
│   │   ├── FileTabs.astro
│   │   ├── ExampleViewer.astro  # версии + diff
│   │   ├── DiffViewer.astro
│   │   └── SeriesNav.astro
│   ├── layouts/
│   │   ├── BaseLayout.astro
│   │   └── EmbedLayout.astro
│   └── pages/
│       ├── index.astro          # главная
│       ├── series/[id].astro    # страница серии
│       └── e/
│           ├── [...slug].astro
│           └── embed/[...slug].astro
├── public/
│   ├── styles/                  # global.css, embed.css
│   └── scripts/                 # theme, catalog-search, code-toolbar, …
├── .cursor/rules/               # правила для Cursor
├── AGENTS.md                    # бриф для агентов
└── astro.config.mjs
```

Новый пример = папка в `examples/` — правки в `src/pages` не нужны.

---

## Добавление примера

1. Создайте `examples/<язык>/<slug>/` (slug: kebab-case, латиница).
2. Положите файлы с кодом.
3. Заполните `meta.json`:

```json
{
  "title": "Python — Hello World",
  "description": "Краткое описание для каталога.",
  "tags": ["beginner"],
  "order": 1,
  "encyclopediaUrl": "https://spirzen.ru/encyclopedia/…/статья"
}
```

### Дополнительные поля `meta.json`

| Поле | Описание |
|------|----------|
| `series` | ID серии (латиница, kebab-case), одинаковый у всех шагов |
| `seriesOrder` | Порядок шага в серии (1, 2, 3…) |
| `seriesTitle` | Человекочитаемое название серии (на любом шаге) |
| `versions` | `[{ "label": "v1", "dir": "v1" }, …]` — папки с версиями для diff |

Папки из `versions[].dir` **не** попадают в основной список файлов — только во вкладки версий и diff.

4. Проверьте: `/e/<язык>/<slug>/`, `/e/embed/<язык>/<slug>/`, при серии — `/series/<series-id>/`.

Языки — `LANGUAGE_CATALOG` в `src/lib/languages.ts`.

**Когда выносить сюда:** листинг > ~30 строк, несколько файлов, практикумы, часто обновляемые конфиги. Короткие фрагменты (3–15 строк) можно оставить в markdown энциклопедии.

---

## URL и пути (важно)

### Канонические адреса на code.spirzen.ru

Продакшен — **custom domain в корне сайта**, без префикса репозитория:

| Назначение | Канонический путь | Пример |
|------------|-------------------|--------|
| Главная | `/` | https://code.spirzen.ru/ |
| Серия | `/series/<id>/` | `/series/python-basics-practicum/` |
| Полная страница | `/e/<язык>/<slug>/` | `/e/bash/backup-dir/` |
| Embed (iframe) | `/e/embed/<язык>/<slug>/` | `/e/embed/python/hello-world/` |
| Тема в embed | `?theme=light` \| `?theme=dark` | `…?theme=dark` |

**В новых ссылках, embed и документации всегда используйте канонические пути** — без `/it-code-examples/` в начале.

### Переменные сборки (Astro `site` + `base`)

Задают все абсолютные пути к CSS, JS и canonical. Для **code.spirzen.ru** обязательно:

```bash
IT_CODE_EXAMPLES_SITE=https://code.spirzen.ru
IT_CODE_EXAMPLES_BASE=/
```

| Среда | `SITE` | `BASE` | Где задаётся |
|-------|--------|--------|--------------|
| **Прод (домен)** | `https://code.spirzen.ru` | `/` | `deploy.yml`, `deploy.bat` |
| Локальная разработка | `http://localhost:4321` | `/` | по умолчанию в `astro.config.mjs` |
| Project Pages (устар.) | `https://spirzen.github.io` | `/it-code-examples/` | только если **нет** custom domain |

Неверный `BASE` на проде → **нет CSS** (`/it-code-examples/styles/…` 404) и **404 страниц** (`/it-code-examples/e/…`).

### Как пути попадают в HTML

- В коде — только через `sitePath('…')` из `src/lib/site.ts` (читает `import.meta.env.BASE_URL`).
- **Не хардкодить** `/it-code-examples/` в компонентах и страницах.
- После `npm run build` скрипт `scripts/postbuild.mjs`:
  1. проверяет, что в `index.html` нет `/it-code-examples/styles/` при prod-env;
  2. зеркалирует весь `dist/` в `dist/it-code-examples/` — для старых закладок и Project Pages;
  3. `public/404.html` редиректит `/it-code-examples/…` → `/…`, если файла ещё нет.

### Устаревшие варианты (совместимость)

| Вариант | Поведение |
|---------|-----------|
| `/it-code-examples/e/…` | Зеркало postbuild или редирект `404.html` |
| `?embed=1` на полной странице | Редирект на `/e/embed/…` (`embed-mode.js`) |

### Чеклист перед деплоем

```bash
# Windows PowerShell
$env:IT_CODE_EXAMPLES_SITE="https://code.spirzen.ru"
$env:IT_CODE_EXAMPLES_BASE="/"
npm run build
```

1. В выводе postbuild: `OK: канонические пути с BASE=/`.
2. В `dist/index.html`: `href="/styles/global.css"`, **не** `/it-code-examples/styles/`.
3. Есть `dist/it-code-examples/e/…` (legacy-зеркало).
4. Push → GitHub Actions; в Pages: custom domain `code.spirzen.ru`, **Enforce HTTPS**.

Подробнее для агентов: [AGENTS.md §5–6](AGENTS.md).

---

## Встраивание в энциклопедию

В [it-knowledge-base](https://github.com/spirzen/it-knowledge-base) — компонент `ExternalCodeEmbed`:

```jsx
import ExternalCodeEmbed from '@site/src/components/ExternalCodeEmbed';

<ExternalCodeEmbed example="python/hello-world" title="Python — Hello World" />
```

Компонент:

- рендерит iframe на `/e/embed/<slug>/`;
- подстраивает высоту по `postMessage` (`it-code-embed-height`);
- передаёт тему (`?theme=` + `postMessage` `it-code-theme`);
- показывает ссылку на полную страницу.

Локально: энциклопедия `localhost:3000`, каталог `localhost:4321`. URL каталога — `customFields.codeExamplesUrl` в Docusaurus или `.env` (`IT_CODE_EXAMPLES_URL`).

### Контракт iframe

| Сообщение | Направление | Назначение |
|-----------|-------------|------------|
| `it-code-embed-height` | iframe → parent | `{ height: number }` |
| `it-code-theme` | parent → iframe | `{ theme: 'light' \| 'dark' }` |

CSP `frame-ancestors`: `spirzen.ru`, localhost:3000. Parent проверяет `event.origin` — `CODE_EXAMPLES_TRUSTED_ORIGINS` в it-knowledge-base.

---

## Деплой

### GitHub Actions (рекомендуется)

1. Репозиторий: [github.com/Spirzen/it-code-examples](https://github.com/Spirzen/it-code-examples).
2. **Settings → Pages → Source:** GitHub Actions.
3. Push в `main` / `master` → [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).
4. Custom domain: `code.spirzen.ru` (CNAME в `public/CNAME`).

Переменные сборки в workflow (не менять для custom domain):

```bash
IT_CODE_EXAMPLES_SITE=https://code.spirzen.ru
IT_CODE_EXAMPLES_BASE=/
```

**Не возвращать** `BASE=/it-code-examples/` после подключения домена `code.spirzen.ru`.

### Альтернатива: `deploy.bat`

Локальная сборка и push в `gh-pages` — только если Pages настроен на ветку `gh-pages`, не Actions. В `deploy.bat` те же `SITE` и `BASE`, что в таблице выше.

---

## Лицензия

| Часть | Лицензия |
|-------|----------|
| Код сайта (Astro, скрипты, стили) | [MIT](LICENSE) |
| Тексты в `meta.json` и примеры кода | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |

---

## Контакт

**Тагиров Тимур Владиславович** — [об авторе](https://spirzen.ru/about/author).
