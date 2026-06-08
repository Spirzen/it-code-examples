// Синхронный обратный вызов
function processData(Данные, callback) {
    const result = data.map(item => item * 2);
    callback(result);
}

processData([1, 2, 3], (result) => {
    console.log(result); // [2, 4, 6]
});

// Асинхронный обратный вызов
function fetchData(url, onSuccess, onError) {
    fetch(url)
        .then(response => response.json())
        .then(data => onSuccess(Данные))
        .catch(error => onError(error));
}

fetchData(
    'https://api.example.com/data',
    (Данные) => console.log('Данные получены:', Данные),
    (error) => console.error('Ошибка:', error)
);
