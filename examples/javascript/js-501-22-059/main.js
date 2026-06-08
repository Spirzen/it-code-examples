const obj = { name: "Тест", value: 42 };

// Получение свойства
console.log(Reflect.get(obj, "name")); // "Тест"

// Установка свойства
Reflect.set(obj, "value", 100);
console.log(obj.value); // 100

// Проверка наличия свойства
console.log(Reflect.has(obj, "name")); // true
console.log(Reflect.has(obj, "missing")); // false

// Удаление свойства
Reflect.deleteProperty(obj, "value");
console.log("value" in obj); // false

// Применение функции
function sum(a, b) {
    return a + b;
}

console.log(Reflect.apply(sum, null, [5, 3])); // 8

// Создание экземпляра
class Person {
    constructor(name) {
        this.name = name;
    }
}

const person = Reflect.construct(Person, ["Алексей"]);
console.log(person.name); // "Алексей"
