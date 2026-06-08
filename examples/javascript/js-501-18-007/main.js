function processForm(data) {
    const age = Number(data.age) || 18; // Если возраст не указан, используем 18
    const isActive = data.isActive === "true"; // Преобразуем строку в булево
    
    return {
        name: String(data.name).trim(),
        age: age,
        email: String(data.email).toLowerCase(),
        isActive: isActive
    };
}

const formData = {
    name: "  Джон  ",
    age: "25",
    email: "JOHN@EXAMPLE.COM",
    isActive: "true"
};

console.log(processForm(formData));
// { name: "Джон", age: 25, email: "john@example.com", isActive: true }
