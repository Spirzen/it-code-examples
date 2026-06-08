// Используется с Promise.any()
const promises = [
    Promise.reject(new Error("Ошибка 1")),
    Promise.reject(new Error("Ошибка 2")),
    Promise.reject(new Error("Ошибка 3"))
];

Promise.any(promises)
    .then(result => console.log(result))
    .catch(error => {
        console.log(error.name); // "AggregateError"
        console.log(error.errors.length); // 3
        error.errors.forEach((err, index) => {
            console.log(`Ошибка ${index + 1}: ${err.message}`);
        });
    });

// Создание своего AggregateError
const errors = [
    new TypeError("Тип 1"),
    new RangeError("Диапазон 1"),
    new Error("Обычная ошибка")
];

const aggregate = new AggregateError(errors, "Несколько ошибок произошло");
console.log(aggregate.message); // "Несколько ошибок произошло"
console.log(aggregate.errors.length); // 3
