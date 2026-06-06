# IT Code Examples

**Лёгкий каталог примеров кода для [Вселенной IT](https://spirzen.ru/)**

Публичный сайт: [code.spirzen.ru](https://code.spirzen.ru/)  
Энциклопедия: [spirzen.ru](https://spirzen.ru/) · репозиторий: [it-knowledge-base](https://github.com/spirzen/it-knowledge-base)

Длинные листинги и мультифайловые практикумы живут здесь; в статьях энциклопедии остаётся текст и встроенный просмотрщик через iframe. Отдельный репозиторий даёт второй лимит GitHub Pages и не раздувает билд Docusaurus.

---

## Стек

| Область | Технология |
|---------|------------|
| Сборка | [Astro 5](https://astro.build/) (статический output) |
| Подсветка | [Shiki](https://shiki.style/) на этапе сборки |
| Runtime JS | Только вкладки файлов, копирование, resize iframe |
| Node.js | ≥ 20 |
| Деплой | GitHub Actions → GitHub Pages |

---

## Быстрый старт

```bash
git clone https://github.com/spirzen/it-code-examples.git
cd it-code-examples
npm install
npm run dev
```

Откройте [http://localhost:4321/](http://localhost:4321/) — каталог примеров.

```bash
npm run build    # dist/
npm run preview  # проверка сборки
```

---

## Структура репозитория

```
it-code-examples/
├── examples/              # контент: единственный источник примеров
│   └── <язык>/
│       └── <slug>/
│           ├── meta.json
│           └── исходники…
├── src/
│   ├── lib/               # сканер examples/, языки Shiki
│   ├── components/        # CodeBlock, FileTabs
│   ├── layouts/           # BaseLayout, EmbedLayout
│   └── pages/
│       ├── index.astro    # каталог /
│       └── e/
│           ├── [...slug].astro       # полная страница примера
│           └── embed/[...slug].astro # только код (для iframe)
├── public/
│   ├── CNAME              # code.spirzen.ru
│   ├── styles/
│   └── scripts/           # embed-resize, code-copy
├── astro.config.mjs
└── package.json
```

Новый пример = папка в `examples/` — правки в `src/pages` не нужны.

---

## Добавление примера

1. Создайте `examples/<язык>/<slug>/` (slug в kebab-case, латиница).
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

| Поле | Описание |
|------|----------|
| `title` | Заголовок страницы |
| `description` | Подзаголовок и SEO |
| `tags` | Бейджи в каталоге |
| `order` | Сортировка внутри языка (меньше — выше) |
| `encyclopediaUrl` | Ссылка «статья в энциклопедии» |

4. Проверьте локально: `/e/<язык>/<slug>/` и `/e/embed/<язык>/<slug>/`.

Поддерживаемые языки — `LANGUAGE_CATALOG` в `src/lib/languages.ts`.

**Когда выносить сюда:** листинг > ~30 строк, несколько файлов, часто обновляемые конфиги. Короткие фрагменты (3–15 строк) можно оставить в markdown энциклопедии.

---

## URL

| Назначение | Путь |
|------------|------|
| Каталог | `/` |
| Полная страница | `/e/<язык>/<slug>/` |
| Embed (iframe) | `/e/embed/<язык>/<slug>/` |

Пример: [code.spirzen.ru/e/embed/python/hello-world/](https://code.spirzen.ru/e/embed/python/hello-world/)

Устаревший `?embed=1` на полной странице редиректит на `/e/embed/…`.

---

## Встраивание в энциклопедию

В [it-knowledge-base](https://github.com/spirzen/it-knowledge-base) используется компонент `ExternalCodeEmbed`:

```jsx
import ExternalCodeEmbed from '@site/src/components/ExternalCodeEmbed';

<ExternalCodeEmbed example="python/hello-world" title="Python — Hello World" />
```

Компонент рендерит iframe, подстраивает высоту по `postMessage` (`it-code-embed-height`) и показывает ссылку на полную страницу примера.

Локально: энциклопедия `localhost:3000`, каталог `localhost:4321`. Если порт занят — в энциклопедии задайте `IT_CODE_EXAMPLES_URL` (см. `.env.example`).

### Контракт iframe

- Embed-страница шлёт `{ type: 'it-code-embed-height', height: number }` в parent.
- CSP `frame-ancestors` разрешает только `spirzen.ru` и localhost при разработке.
- Parent проверяет `event.origin` (см. `CODE_EXAMPLES_TRUSTED_ORIGINS` в it-knowledge-base).

---

## Деплой

Push в ветку `main` запускает [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml):

1. `npm ci` → `npm run build`
2. Артефакт `dist/` → GitHub Pages
3. Домен: `code.spirzen.ru` (файл `public/CNAME`)

Переменные сборки (уже в workflow):

```bash
IT_CODE_EXAMPLES_SITE=https://code.spirzen.ru
IT_CODE_EXAMPLES_BASE=/
```

Для project pages (`user.github.io/repo-name`): `IT_CODE_EXAMPLES_BASE=/it-code-examples/`.

---

## Лицензия

| Часть | Лицензия |
|-------|----------|
| Код сайта (Astro, скрипты, стили) | [MIT](LICENSE) |
| Тексты в `meta.json` и примеры кода | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) (как у [Вселенной IT](https://spirzen.ru/about/license)) |

---

## Контакт

**Тагиров Тимур Владиславович** — автор и методист.  
[Об авторе](https://spirzen.ru/about/author) на сайте энциклопедии.
