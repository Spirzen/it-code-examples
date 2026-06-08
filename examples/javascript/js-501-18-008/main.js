const original = {
    name: "Джон",
    address: {
        city: "Москва",
        street: "Тверская"
    }
};

// Способ 1: spread оператор
const copy1 = { ...original };
copy1.name = "Мария";
copy1.address.city = "Санкт-Петербург";

console.log(original.name); // "Джон" - изменилось только имя копии
console.log(original.address.city); // "Санкт-Петербург" - город изменился в обоих

// Способ 2: Object.assign
const copy2 = Object.assign({}, original);
