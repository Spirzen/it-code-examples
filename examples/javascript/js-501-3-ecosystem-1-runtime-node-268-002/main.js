import http from 'node:http';

const proxy = http.createServer((clientReq, clientRes) => {
  const options = {
    hostname: 'api.example.com',
    port: 80,
    path: clientReq.url,
    method: clientReq.method,
    headers: clientReq.headers,
  };

  const proxyReq = http.request(options, (proxyRes) => {
    clientRes.writeHead(proxyRes.statusCode, proxyRes.headers);
    proxyRes.pipe(clientRes);
  });

  clientReq.pipe(proxyReq);
});
