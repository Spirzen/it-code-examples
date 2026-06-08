let animal = {
    sound: "Какой-то звук",
    makeSound() {
        console.log(this.sound);
    }
};

let rabbit = {
    sound: "Пи-пи",
    __proto__: animal
};

rabbit.makeSound(); // "Пи-пи" (своё свойство sound)

// А теперь переопределим метод makeSound
rabbit.makeSound = function() {
    console.log("Топот кролика и писк: " + this.sound);
};

rabbit.makeSound(); // "Топот кролика и писк: Пи-пи"
animal.makeSound(); // "Какой-то звук" (оригинал не тронут)
