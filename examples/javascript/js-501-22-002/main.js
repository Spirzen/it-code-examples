// Функция-конструктор (старый стиль, до ES6)
function WarriorOld(name, level) {
    this.name = name;
    this.level = level;
}

WarriorOld.prototype.attack = function(target) {
    console.log(`${this.name} атакует!`);
};

// Прототипное наследование
function KnightOld(name, horseName) {
    WarriorOld.call(this, name);   // вызов родительского конструктора
    this.horseName = horseName;
}

KnightOld.prototype = Object.create(WarriorOld.prototype);
KnightOld.prototype.constructor = KnightOld;

const w = new KnightOld("Персиваль", "Ветер");
w.attack();  // "Персиваль атакует!" — метод из прототипа
