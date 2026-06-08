const http = require('http');

function sendPostRequest(url, data) {
    return new Promise((resolve, reject) => {
        const postData = JSON.stringify(data);
        
        const options = {
            hostname: new URL(url).hostname,
            port: new URL(url).port || 80,
            path: new URL(url).pathname,
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': Buffer.byteLength(postData)
            }
        };

        const req = http.request(options, (res) => {
            let body = '';

            res.on('data', chunk => {
                body += chunk;
            });

            res.on('end', () => {
                resolve({ statusCode: res.statusCode, body });
            });
        });

        req.on('error', (error) => {
            reject(error);
        });

        req.write(postData);
        req.end();
    });
}

async function main() {
    const payload = { username: 'user1', action: 'login' };
    try {
        const result = await sendPostRequest('http://localhost:3000/api/login', payload);
        console.log('Статус ответа:', result.statusCode);
        console.log('Тело ответа:', result.body);
    } catch (error) {
        console.error('Ошибка отправки:', error.message);
    }
}

// main();
