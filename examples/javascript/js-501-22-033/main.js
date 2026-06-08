// Создание ошибки
const error = new Error("Произошла ошибка");
console.log(error.message); // "Произошла ошибка"
console.log(error.name); // "Error"
console.log(error.stack); // Стек вызовов

// Генерация ошибки
throw new Error("Что-то пошло не так");

// Обработка ошибки
try {
    throw new Error("Ошибка в блоке try");
} catch (error) {
    console.log(error.message); // "Ошибка в блоке try"
    console.log(error.name); // "Error"
}
