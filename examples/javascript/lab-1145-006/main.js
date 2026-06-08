// === fetch: GET ===
const res = await fetch(url);
if (!res.ok) throw new Error(res.status);
const data = await res.json();

// === fetch: POST JSON ===
await fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ key: 'value' }),
});

// === axios: GET / POST ===
import axios from 'axios';
const { data } = await axios.get(url, { params: { q: 1 } });
await axios.post(url, { key: 'value' });

// === axios: клиент ===
const api = axios.create({ baseURL: '/api', timeout: 10000 });
