import {defineConfig} from 'astro/config';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/** Прод: code.spirzen.ru или user.github.io/it-code-examples */
const site = process.env.IT_CODE_EXAMPLES_SITE ?? 'http://localhost:4321';
const base = process.env.IT_CODE_EXAMPLES_BASE ?? '/';

export default defineConfig({
  site,
  base,
  output: 'static',
  vite: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'),
      },
    },
  },
  markdown: {
    syntaxHighlight: {
      type: 'shiki',
      excludeLangs: ['mermaid'],
    },
    shikiConfig: {
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
      wrap: true,
      langAlias: {
        xaml: 'xml',
        cs: 'csharp',
        js: 'javascript',
        ts: 'typescript',
        ps1: 'powershell',
        sh: 'bash',
        yml: 'yaml',
      },
    },
  },
});
