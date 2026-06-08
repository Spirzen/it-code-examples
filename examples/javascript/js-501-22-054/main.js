// Создание промиса
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        const success = true;
        if (success) {
            resolve("Операция завершена успешно");
        } else {
            reject(new Error("Произошла ошибка"));
        }
    }, 1000);
});

// Обработка результата
promise
    .then(result => console.log(result))
    .catch(error => console.error(error.message));

// Цепочка промисов
fetch("https://api.example.com/data")
    .then(response => response.json())
    .then(data => processData(data))
    .then(result => saveResult(result))
    .catch(error => console.error("Ошибка:", error));
