import {defineConfig} from 'astro/config';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/**
 * Пути задаются env (см. README.md § «URL и пути», AGENTS.md §5).
 *
 * Прод code.spirzen.ru: SITE=https://code.spirzen.ru, BASE=/
 * Локально:            http://localhost:4321, BASE=/ (по умолчанию)
 * Устар. Project Pages: spirzen.github.io + BASE=/it-code-examples/ — не для custom domain
 */
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
        fs: 'fsharp',
        js: 'javascript',
        ts: 'typescript',
        ps1: 'powershell',
        sh: 'bash',
        yml: 'yaml',
        pas: 'pascal',
        tex: 'latex',
        luau: 'lua',
        conf: 'nginx',
        hcl: 'hcl',
        tf: 'hcl',
        promql: 'promql',
        mcfunction: 'mcfunction',
        cmd: 'batch',
        cql: 'sql',
        cypher: 'javascript',
        dax: 'sql',
        http: 'http',
        st: 'smalltalk',
        asm: 'asm',
        nasm: 'asm',
        assembly: 'asm',
        cobol: 'cobol',
        cbl: 'cobol',
        cpy: 'cobol',
        fortran: 'fortran-free-form',
        f90: 'fortran-free-form',
        f95: 'fortran-free-form',
        f: 'fortran-fixed-form',
        lisp: 'lisp',
        cl: 'lisp',
        hs: 'haskell',
        cabal: 'ini',
        scala: 'scala',
        sc: 'scala',
        elixir: 'elixir',
        ex: 'elixir',
        zig: 'zig',
        nim: 'nim',
        julia: 'julia',
        jl: 'julia',
        bsl: 'bsl',
        '1c': 'bsl',
      },
    },
  },
});
