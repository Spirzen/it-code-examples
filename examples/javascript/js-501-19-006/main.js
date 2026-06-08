const user = {
    name: "Timur",
    age: 31,
    
    // Метод, использующий this
    describe() {
        return `${this.name}, ${this.age} лет`;
    },
    
    // Стрелочная функция внутри объекта (см. раздел 4)
    describeArrow: () => {
        // this здесь НЕ относится к object user, а наследуется из внешней области
        return `Стрелка: ${this}`; 
    }
};

// Вызов метода через точку
console.log(user.describe()); // "Timur, 31 лет"
// Внутри describe(), this === user

// Неправильный вызов (потеря контекста)
const getUserDesc = user.describe;
// Если вызвать отдельно, this станет undefined (в strict mode) или глобальным объектом (в non-strict)
console.log(getUserDesc()); // В strict mode: TypeError: Cannot read properties of undefined (reading 'name')
