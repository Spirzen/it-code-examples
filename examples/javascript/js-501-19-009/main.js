function showInfo(city, country) {
    // this здесь — тот объект, который мы передадим вручную
    return `Я живу в ${this.city}, ${this.country}. Город: ${city}, Страна: ${country}`;
}

const traveler = {
    city: "Уфа",
    country: "Россия"
};

// call: передает аргументы списком
console.log(showInfo.call(traveler, "Москва", "США")); 
// Результат: "Я живу в Уфа, Россия. Город: Москва, Страна: США"

// apply: передает аргументы массивом
console.log(showInfo.apply(traveler, ["Казань", "Татарстан"])); 
// Результат: "Я живу в Уфа, Россия. Город: Казань, Страна: Татарстан"

// bind: возвращает новую функцию с предзаданным this
const boundShowInfo = showInfo.bind(traveler);
console.log(boundShowInfo("Башкирия", "РФ")); 
// Результат: "Я живу в Уфа, Россия. Город: Башкирия, Страна: РФ"
