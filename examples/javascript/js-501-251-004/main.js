fetch(url, {
  method: 'GET', // 'POST', 'PUT', …
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data), // для POST/PUT
  mode: 'cors', // 'same-origin', 'no-cors'
  credentials: 'same-origin', // 'include', 'omit'
  cache: 'default', // 'no-store', 'reload', 'force-cache', …
  redirect: 'follow', // 'manual', 'error'
  signal: ac.signal, // AbortSignal для отмены
  integrity: 'sha256-…' // Subresource Integrity
})
.then(res => {
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json(); // .text(), .blob(), .arrayBuffer()
});
