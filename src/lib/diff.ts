export type DiffLineType = 'same' | 'add' | 'remove';

export type DiffLine = {
  type: DiffLineType;
  oldLine: number | null;
  newLine: number | null;
  content: string;
};

/** Простой построчный diff (LCS) без внешних зависимостей. */
export function diffLines(oldText: string, newText: string): DiffLine[] {
  const oldLines = oldText.replace(/\r\n/g, '\n').split('\n');
  const newLines = newText.replace(/\r\n/g, '\n').split('\n');
  const n = oldLines.length;
  const m = newLines.length;

  const dp: number[][] = Array.from({length: n + 1}, () => Array(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      dp[i][j] =
        oldLines[i] === newLines[j]
          ? dp[i + 1][j + 1] + 1
          : Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }

  const out: DiffLine[] = [];
  let i = 0;
  let j = 0;
  while (i < n && j < m) {
    if (oldLines[i] === newLines[j]) {
      out.push({
        type: 'same',
        oldLine: i + 1,
        newLine: j + 1,
        content: oldLines[i],
      });
      i++;
      j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1]) {
      out.push({
        type: 'remove',
        oldLine: i + 1,
        newLine: null,
        content: oldLines[i],
      });
      i++;
    } else {
      out.push({
        type: 'add',
        oldLine: null,
        newLine: j + 1,
        content: newLines[j],
      });
      j++;
    }
  }
  while (i < n) {
    out.push({
      type: 'remove',
      oldLine: i + 1,
      newLine: null,
      content: oldLines[i],
    });
    i++;
  }
  while (j < m) {
    out.push({
      type: 'add',
      oldLine: null,
      newLine: j + 1,
      content: newLines[j],
    });
    j++;
  }
  return out;
}

export function hasDiffChanges(lines: DiffLine[]): boolean {
  return lines.some((l) => l.type !== 'same');
}
