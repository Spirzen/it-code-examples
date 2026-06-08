const id = Symbol("id");
const name = Symbol("name");

const user = {
    [id]: 12345,
    [name]: "Алексей",
    age: 30
};

console.log(user[id]); // 12345
console.log(user[name]); // "Алексей"
console.log(user.age); // 30

// Символьные свойства не видны в обычных циклах
for (let key in user) {
    console.log(key); // только "age"
}

console.log(Object.keys(user)); // ["age"]
console.log(Object.getOwnPropertyNames(user)); // ["age"]

// Получение символьных ключей
console.log(Object.getOwnPropertySymbols(user)); // [Symbol(id), Symbol(name)]

// Получение всех ключей
const allKeys = [...Object.getOwnPropertyNames(user), ...Object.getOwnPropertySymbols(user)];
console.log(allKeys); // ["age", Symbol(id), Symbol(name)]
