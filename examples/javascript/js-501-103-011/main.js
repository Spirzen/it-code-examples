const http = require('http');
const https = require('https');
const { URL } = require('url');

function parseAndCheckUrl(targetUrl) {
    return new Promise((resolve, reject) => {
        let parsedUrl;

        try {
            parsedUrl = new URL(targetUrl);
        } catch (e) {
            reject(new Error('Некорректный формат URL'));
            return;
        }

        const protocol = parsedUrl.protocol === 'https:' ? https : http;
        const options = {
            hostname: parsedUrl.hostname,
            port: parsedUrl.port || (parsedUrl.protocol === 'https:' ? 443 : 80),
            path: parsedUrl.pathname,
            method: 'HEAD', // Используем HEAD для экономии ресурсов
            timeout: 5000
        };

        const req = protocol.request(options, (res) => {
            resolve({
                url: targetUrl,
                status: res.statusCode,
                headers: res.headers,
                valid: res.statusCode >= 200 && res.statusCode < 400
            });
        });

        req.on('error', (e) => {
            resolve({
                url: targetUrl,
                status: null,
                error: e.message,
                valid: false
            });
        });

        req.on('timeout', () => {
            req.destroy();
            resolve({
                url: targetUrl,
                status: null,
                error: 'Таймаут запроса',
                valid: false
            });
        });

        req.end();
    });
}

async function main() {
    const testUrls = [
        'https://example.com',
        'http://invalid-domain-xyz.com',
        'not-a-url'
    ];

    for (const url of testUrls) {
        try {
            const result = await parseAndCheckUrl(url);
            console.log(`URL: ${result.url}`);
            console.log(`Статус: ${result.status || 'Ошибка'}`);
            console.log(`Доступен: ${result.valid ? 'Да' : 'Нет'}`);
            if (result.error) console.log(`Ошибка: ${result.error}`);
            console.log('---');
        } catch (err) {
            console.log(`Ошибка парсинга для ${url}: ${err.message}`);
        }
    }
}

// main();
