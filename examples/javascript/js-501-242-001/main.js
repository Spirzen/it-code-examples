function readConfig(path) {
  let raw;
  try {
    raw = fs.readFileSync(path, 'utf8');
    return JSON.parse(raw);
  } catch (e) {
    if (e instanceof SyntaxError) {
      throw new Error(`Некорректный JSON в ${path}`, { cause: e });
    }
    throw e;
  } finally {
    // освобождение ресурсов, если появятся (дескрипторы, временные файлы)
  }
}
