class Warrior {
    // Статическое поле
    static count = 0;
    
    // Поле класса (ES2022)
    health = 100;
    
    // Конструктор
    constructor(name, level = 1) {
        this.name = name;      // this — ссылка на экземпляр
        this.level = level;
        Warrior.count++;
    }
    
    // Геттер
    get damage() {
        return this.level * 10 + (this.strength || 0);
    }
    
    // Метод
    attack(target) {
        console.log(`${this.name} атакует ${target.name}`);
        target.health -= this.damage;
    }
    
    // Статический метод
    static getCount() {
        return Warrior.count;
    }
}

// Наследование
class Knight extends Warrior {
    constructor(name, horseName, level) {
        super(name, level);     // вызов конструктора родителя (обязателен!)
        this.horseName = horseName;
    }
    
    // Переопределение метода
    attack(target) {
        console.log(`${this.name} на коне ${this.horseName} атакует!`);
        super.attack(target);   // вызов метода родителя
    }
    
    // Свойство вместо метода
    get shout() {
        return `За ${this.name}!`;
    }
}

// Использование
const w1 = new Warrior("Артур", 5);
const w2 = new Knight("Ланселот", "Скакун", 10);
w1.attack(w2);
console.log(w2.shout);          // "За Ланселот!" (геттер без скобок)
