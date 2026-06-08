function Person(name, age) {
    // В данном случае this — это новый пустой объект {}, созданный перед вызовом конструктора
    this.name = name;
    this.age = age;
    this.greet = function() {
        return `Привет, я ${this.name}`;
    };
}

const p1 = new Person("Алексей", 25);
const p2 = new Person("Мария", 28);

console.log(p1.greet()); // "Привет, я Алексей"
console.log(p2.greet()); // "Привет, я Мария"

// Проверка:
console.log(p1 instanceof Person); // true
console.log(p1.constructor === Person); // true
