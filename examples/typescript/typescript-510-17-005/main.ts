async function withRetry<T>(
  task: () => Promise<T>,
  retries = 2,
): Promise<T> {
  let lastError: unknown;

  for (let attempt = 0; attempt <= retries; attempt += 1) {
    try {
      return await task();
    } catch (error: unknown) {
      lastError = error;
    }
  }

  throw new Error(toMessage(lastError));
}

// Использование
const user = await withRetry(() => loadUser("u-1"), 3);
