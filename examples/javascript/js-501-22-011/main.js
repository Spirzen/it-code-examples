let animal = {
    walk() {
        console.log("Animal walks");
    }
};

let rabbit = {
    __proto__: animal
};

// Метод walk всё ещё из прототипа
rabbit.walk(); // "Animal walks"

// Переопределяем только для rabbit
rabbit.walk = function() {
    console.log("Rabbit hops");
};

rabbit.walk(); // "Rabbit hops"
animal.walk(); // "Animal walks" (не изменился)
