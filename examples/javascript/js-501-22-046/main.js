// Преобразование объекта в JSON-строку
const user = {
    name: "Алексей",
    age: 30,
    city: "Москва",
    hobbies: ["чтение", "программирование"]
};

const jsonString = JSON.stringify(user);
console.log(jsonString);
// '{"name":"Алексей","age":30,"city":"Москва","hobbies":["чтение","программирование"]}'

// Преобразование строки в объект
const parsedUser = JSON.parse(jsonString);
console.log(parsedUser.name); // "Алексей"
console.log(parsedUser.hobbies[0]); // "чтение"
