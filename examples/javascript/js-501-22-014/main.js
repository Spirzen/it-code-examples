const person = {};
let _age = 0;

Object.defineProperty(person, 'age', {
    get() {
        return _age;
    },
    set(value) {
        if (value >= 0 && value <= 120) {
            _age = value;
        }
    },
    enumerable: true,
    configurable: true
});

person.age = 25;
console.log(person.age); // 25
person.age = 200; // Не сработает
console.log(person.age); // 25
