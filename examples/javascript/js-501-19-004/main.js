const user = {
    name: "Timur",
    age: 31
};

// Доступ к существующему свойству
console.log(user.name); // "Timur"

// Доступ к отсутствующему свойству
console.log(user.role); // undefined (НЕ ReferenceError)

// Попытка обратиться к несуществующей переменной (не свойству)
try {
    console.log(role); 
} catch (e) {
    console.error("Ошибка:", e.message); // ReferenceError: role is not defined
}
