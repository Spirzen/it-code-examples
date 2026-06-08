// Обычная функция как конструктор
function Jedi(name) {
    this.name = name;
    this.sayName = function() {
        console.log(this.name);
    };
}

const luke = new Jedi("Люк");
luke.sayName(); // "Люк"

// Стрелочная функция не может быть конструктором
const Sith = (name) => {
    this.name = name; // this указывает не туда
};

// Это вызовет ошибку
// const vader = new Sith("Вейдер");
