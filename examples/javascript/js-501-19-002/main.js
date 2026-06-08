function checkError() {
    // Пытаемся обратиться к несуществующей переменной
    try {
        console.log(undefinedVariable); 
    } catch (e) {
        // Ошибка: ReferenceError: undefinedVariable is not defined
        console.error(e.message); 
    }
}

checkError();

// Контекст typeof исключает ошибку для неопределенных идентификаторов
console.log(typeof undefinedVariable); // "undefined" (без ошибки)
