const number = 1234567.89;

// Форматирование для русской локали
console.log(new Intl.NumberFormat("ru-RU").format(number));
// "1 234 567,89"

// Валюта
console.log(new Intl.NumberFormat("ru-RU", { 
    style: "currency", 
    currency: "RUB" 
}).format(number));
// "1 234 567,89 ₽"

console.log(new Intl.NumberFormat("en-US", { 
    style: "currency", 
    currency: "USD" 
}).format(number));
// "$1,234,567.89"

// Проценты
console.log(new Intl.NumberFormat("ru-RU", { 
    style: "percent" 
}).format(0.42));
// "42 %"

// Научная нотация
console.log(new Intl.NumberFormat("ru-RU", { 
    notation: "scientific" 
}).format(number));
// "1,23456789E6"

// Компактный формат
console.log(new Intl.NumberFormat("ru-RU", { 
    notation: "compact" 
}).format(1234567));
// "1,2 млн"
