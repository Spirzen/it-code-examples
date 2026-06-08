function Person(name) {
    this.name = name; // this = новый объект
    console.log(this);
}

const alice = new Person("Alice"); // Person { name: "Alice" }

class Car {
    constructor(model) {
        this.model = model; // this = новый объект Car
    }
}

const tesla = new Car("Tesla"); // Car { model: "Tesla" }
