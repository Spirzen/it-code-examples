const displayNames = new Intl.DisplayNames("ru", { type: "language" });

console.log(displayNames.of("en"));   // "английский"
console.log(displayNames.of("de"));   // "немецкий"
console.log(displayNames.of("fr"));   // "французский"
console.log(displayNames.of("zh"));   // "китайский"

// Названия регионов
const regionNames = new Intl.DisplayNames("ru", { type: "region" });
console.log(regionNames.of("US"));    // "США"
console.log(regionNames.of("DE"));    // "Германия"
console.log(regionNames.of("CN"));    // "Китай"
console.log(regionNames.of("RU"));    // "Россия"

// Названия скриптов
const scriptNames = new Intl.DisplayNames("ru", { type: "script" });
console.log(scriptNames.of("Latn"));  // "латиница"
console.log(scriptNames.of("Cyrl"));  // "кириллица"
