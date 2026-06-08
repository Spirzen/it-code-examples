// Создание объектов Boolean
const bool1 = new Boolean(true);
const bool2 = new Boolean(false);
const bool3 = new Boolean("текст"); // любое непустое значение → true

console.log(bool1); // Boolean { true }
console.log(bool2); // Boolean { false }
console.log(bool3); // Boolean { true }

// Приведение к примитиву
console.log(bool1.valueOf()); // true
console.log(bool2.valueOf()); // false

// Автоматическое приведение в условиях
if (bool1) {
    console.log("Истина"); // Выполнится
}

if (bool2) {
    console.log("Истина"); // Не выполнится
}
