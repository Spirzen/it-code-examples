// Примеры возникновения RangeError
try {
    const arr = new Array(-1); // Отрицательная длина
} catch (error) {
    console.log(error.name); // "RangeError"
}

try {
    (123.456).toFixed(1000); // Слишком много знаков
} catch (error) {
    console.log(error.name); // "RangeError"
}

// Создание своей ошибки диапазона
function setAge(age) {
    if (age < 0 || age > 150) {
        throw new RangeError("Возраст должен быть от 0 до 150");
    }
    return age;
}

try {
    setAge(200);
} catch (error) {
    console.log(error.message); // "Возраст должен быть от 0 до 150"
}
