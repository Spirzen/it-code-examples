let animal = {
    walk() {
        console.log("Животное идёт");
    }
};

let rabbit = {
    __proto__: animal,
    walk() {
        console.log("Кролик скачет");
        // Можно вызвать родительский метод
        animal.walk(); // или this.__proto__.walk()
    }
};

rabbit.walk(); 
// "Кролик скачет"
// "Животное идёт"
