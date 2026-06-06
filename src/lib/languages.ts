/** Shiki language id + подпись в каталоге */
export const LANGUAGE_CATALOG = [
  {id: 'html', label: 'HTML'},
  {id: 'css', label: 'CSS'},
  {id: 'javascript', label: 'JavaScript'},
  {id: 'python', label: 'Python'},
  {id: 'xml', label: 'XML / XAML'},
  {id: 'json', label: 'JSON'},
  {id: 'java', label: 'Java'},
  {id: 'csharp', label: 'C#'},
  {id: 'cpp', label: 'C++'},
  {id: 'kotlin', label: 'Kotlin'},
  {id: 'go', label: 'Go'},
  {id: 'yaml', label: 'YAML'},
  {id: 'bash', label: 'Bash'},
  {id: 'powershell', label: 'PowerShell'},
  {id: 'groovy', label: 'Groovy'},
  {id: 'rust', label: 'Rust'},
  {id: 'ruby', label: 'Ruby'},
  {id: 'php', label: 'PHP'},
  {id: 'sql', label: 'SQL'},
  {id: 'dockerfile', label: 'Dockerfile'},
] as const;

const EXT_TO_LANG: Record<string, string> = {
  html: 'html',
  htm: 'html',
  css: 'css',
  js: 'javascript',
  mjs: 'javascript',
  ts: 'typescript',
  py: 'python',
  xml: 'xml',
  xaml: 'xml',
  json: 'json',
  java: 'java',
  cs: 'csharp',
  cpp: 'cpp',
  cc: 'cpp',
  h: 'cpp',
  hpp: 'cpp',
  kt: 'kotlin',
  kts: 'kotlin',
  go: 'go',
  yaml: 'yaml',
  yml: 'yaml',
  sh: 'bash',
  bash: 'bash',
  ps1: 'powershell',
  groovy: 'groovy',
  rs: 'rust',
  rb: 'ruby',
  php: 'php',
  sql: 'sql',
  dockerfile: 'dockerfile',
  md: 'markdown',
};

export function langFromFilename(name: string): string {
  const lower = name.toLowerCase();
  if (lower === 'dockerfile') {
    return 'dockerfile';
  }
  const ext = lower.split('.').pop() ?? lower;
  return EXT_TO_LANG[ext] ?? 'text';
}
