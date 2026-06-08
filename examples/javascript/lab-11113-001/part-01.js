const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('ok');
    return;
  }
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Node API в Docker работает\n');
});

// 0.0.0.0 — слушать все интерфейсы; иначе с хоста не достучаться
server.listen(3000, '0.0.0.0', () => {
  console.log('Слушаю http://0.0.0.0:3000');
});
