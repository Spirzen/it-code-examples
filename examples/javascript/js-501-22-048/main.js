const product = {
    name: "Ноутбук",
    price: 50000,
    costPrice: 30000, // Себестоимость (не показываем)
    discount: 0.1,
    inStock: true
};

// Исключение полей из сериализации
const jsonString = JSON.stringify(product, ["name", "price", "discount", "inStock"]);
console.log(jsonString);
// '{"name":"Ноутбук","price":50000,"discount":0.1,"inStock":true}'

// Преобразование значений
const formatted = JSON.stringify(product, (key, value) => {
    if (key === "price") {
        return value + " ₽";
    }
    if (key === "discount") {
        return (value * 100) + "%";
    }
    return value;
});

console.log(formatted);
// '{"name":"Ноутбук","price":"50000 ₽","costPrice":30000,"discount":"10%","inStock":true}'
