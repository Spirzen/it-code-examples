function validateInput(input) {
    if (!input) {
        return "Поле не может быть пустым";
    }
    
    const number = Number(input);
    if (isNaN(number)) {
        return "Введите число";
    }
    
    if (number <= 0) {
        return "Число должно быть положительным";
    }
    
    return "Валидация пройдена";
}

console.log(validateInput("")); // "Поле не может быть пустым"
console.log(validateInput("abc")); // "Введите число"
console.log(validateInput("-5")); // "Число должно быть положительным"
console.log(validateInput("10")); // "Валидация пройдена"
