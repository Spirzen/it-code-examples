// Прототип пользователя
let userPrototype = {
    isAdmin: false,
    sayHello() {
        console.log(`Привет, я ${this.name}`);
    }
};

// Конкретные пользователи
let admin = {
    name: "Антон",
    isAdmin: true,  // переопределяем
    __proto__: userPrototype
};

let guest = {
    name: "Гость",
    __proto__: userPrototype
};

admin.sayHello(); // "Привет, я Антон"
guest.sayHello(); // "Привет, я Гость"

console.log(admin.isAdmin); // true (своё)
console.log(guest.isAdmin); // false (из прототипа)
