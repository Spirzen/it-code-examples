const res = await fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    title: 'hello',
    body: 'text',
    userId: 1,
  }),
});

if (!res.ok) {
  throw new Error(`HTTP ${res.status}`);
}

const created = await res.json();
console.log('Новый id:', created.id);
