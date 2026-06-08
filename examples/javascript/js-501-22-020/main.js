class Animal {
    constructor(name) {
        this.name = name;
    }
    
    speak() {
        console.log(`${this.name} издаёт звук`);
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name); // Вызов конструктора родителя
        this.breed = breed;
    }
    
    bark() {
        console.log(`${this.name} лает`);
    }
}

const dog = new Dog("Рекс", "Овчарка");
dog.speak(); // "Рекс издаёт звук"
dog.bark();  // "Рекс лает"
