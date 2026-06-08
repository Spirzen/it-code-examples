try {
    eval("function test( { return 1; }"); // Неправильный синтаксис
} catch (error) {
    console.log(error.name); // "SyntaxError"
}

// Создание своей ошибки синтаксиса
function validateJSON(jsonString) {
    try {
        JSON.parse(jsonString);
    } catch (error) {
        if (error instanceof SyntaxError) {
            throw new SyntaxError("Некорректный JSON: " + error.message);
        }
        throw error;
    }
}

try {
    validateJSON("{ name: 'Иван' }"); // Неправильные кавычки
} catch (error) {
    console.log(error.message); // "Некорректный JSON: ..."
}
