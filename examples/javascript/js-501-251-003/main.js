// Вариант 1: try/catch
async function f() {
  try {
    const res = await fetch('/api');
    const data = await res.json();
    return data;
  } catch (e) {
    console.error('Fetch failed', e);
    throw e;
  }
}

// Вариант 2: .catch на уровне вызова
f().catch(e => { … });
