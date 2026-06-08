const locale = new Intl.Locale("ru-RU");

console.log(locale.language);   // "ru"
console.log(locale.script);     // undefined
console.log(locale.region);     // "RU"
console.log(locale.baseName);   // "ru-RU"

// Методы
console.log(locale.maximize()); // "ru-Cyrl-RU" (добавлен скрипт)
console.log(locale.minimize()); // "ru" (убран регион)

// Создание с опциями
const localeWithOptions = new Intl.Locale("ru", {
    region: "RU",
    calendar: "gregory",
    hourCycle: "h23"
});

console.log(localeWithOptions.toString()); 
// "ru-RU-u-ca-gregory-hc-h23"
