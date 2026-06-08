try {
    console.log(nonExistentVariable);
} catch (error) {
    console.log(error.name); // "ReferenceError"
}

// Создание своей ошибки ссылки
function accessProperty(obj, prop) {
    if (!(prop in obj)) {
        throw new ReferenceError(`Свойство "${prop}" не существует`);
    }
    return obj[prop];
}

const user = { name: "Иван" };
try {
    accessProperty(user, "age");
} catch (error) {
    console.log(error.message); // "Свойство "age" не существует"
}
