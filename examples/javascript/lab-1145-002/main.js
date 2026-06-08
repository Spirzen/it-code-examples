async function fetchWithRetry(url, { attempts = 3, baseMs = 300 } = {}) {
  let lastError;
  for (let i = 0; i < attempts; i++) {
    try {
      const res = await fetch(url);
      if (res.status >= 500) throw new Error(`HTTP ${res.status}`);
      if (!res.ok) throw new Error(`HTTP ${res.status} (no retry)`);
      return await res.json();
    } catch (e) {
      lastError = e;
      if (String(e.message).includes('no retry')) throw e;
      if (i === attempts - 1) break;
      await new Promise((r) => setTimeout(r, baseMs * 2 ** i));
    }
  }
  throw lastError;
}
