const users = [
    { id: 1, name: "Джон" },
    { id: 2, name: "Мария" },
    { id: 3, name: "Алекс" }
];

// Поверхностное копирование массива
const shallowCopy = [...users];
shallowCopy[0].name = "Иван";

console.log(users[0].name); // "Иван" - оригинал изменился

// Глубокое копирование массива
const deepCopy = users.map(user => ({ ...user }));
deepCopy[0].name = "Петр";

console.log(users[0].name); // "Иван" - оригинал не изменился
console.log(deepCopy[0].name); // "Петр"
