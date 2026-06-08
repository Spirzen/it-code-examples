function readFileUtf8(path: string): Promise<string> {
  return new Promise((resolve, reject) => {
    // псевдокод Node callback API
    fakeRead(path, (err: Error | null, data?: string) => {
      if (err) reject(err);
      else resolve(data ?? "");
    });
  });
}

declare function fakeRead(
  path: string,
  cb: (err: Error | null, data?: string) => void,
): void;
