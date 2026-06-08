const http = require('http');

function fetchData(url) {
    return new Promise((resolve, reject) => {
        const request = http.get(url, (res) => {
            let data = '';

            res.on('data', chunk => {
                data += chunk;
            });

            res.on('end', () => {
                try {
                    const parsedData = JSON.parse(data);
                    resolve(parsedData);
                } catch (e) {
                    resolve(data);
                }
            });
        });

        request.on('error', (error) => {
            reject(error);
        });
    });
}

async function main() {
    try {
        const response = await fetchData('http://localhost:3000/api/data');
        console.log('Полученные данные:', response);
    } catch (error) {
        console.error('Ошибка при получении данных:', error.message);
    }
}

// main();
