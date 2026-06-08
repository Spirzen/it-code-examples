try {
    null.someMethod(); // null не имеет методов
} catch (error) {
    console.log(error.name); // "TypeError"
}

try {
    const num = 42;
    num(); // Число не является функцией
} catch (error) {
    console.log(error.name); // "TypeError"
}

// Создание своей ошибки типа
function divide(a, b) {
    if (typeof a !== "number" || typeof b !== "number") {
        throw new TypeError("Оба аргумента должны быть числами");
    }
    if (b === 0) {
        throw new TypeError("Деление на ноль запрещено");
    }
    return a / b;
}

try {
    divide("10", 2);
} catch (error) {
    console.log(error.message); // "Оба аргумента должны быть числами"
}
