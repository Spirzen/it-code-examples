const http = require('http');

const PORT = 3000;

const server = http.createServer((req, res) => {
    console.log(`Запрос: ${req.method} ${req.url}`);

    res.writeHead(200, { 'Content-Type': 'application/json' });

    if (req.url === '/') {
        res.end(JSON.stringify({ message: 'Добро пожаловать на сервер!' }));
    } else if (req.url.startsWith('/api/data')) {
        const responseData = { 
            timestamp: new Date().toISOString(), 
            status: 'active' 
        };
        res.end(JSON.stringify(responseData));
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Ресурс не найден');
    }
});

server.listen(PORT, () => {
    console.log(`Сервер запущен на порту ${PORT}`);
});
