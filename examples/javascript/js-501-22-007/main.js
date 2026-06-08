class Unit {
    constructor() {
        this.name = "Имя";
        this.intel = 10;
        this.agility = 10;
        this.strength = 10;
        this.health = 100;
        this.mana = 50;
        this.level = 1;
    }

    get damage() {
        return (this.intel + this.agility + this.strength) + (this.level * 2);
    }

    attack(target) {
        console.log(`${this.name} атакует ${target.name} и наносит ${this.damage} единиц урона.`);
        target.health -= this.damage;
        console.log(`${target.name} теперь имеет ${target.health} здоровья.`);
    }
}

const warrior = new Unit();
warrior.name = "Воин";
warrior.intel = 5;
warrior.agility = 15;
warrior.strength = 30;

const mage = new Unit();
mage.name = "Маг";
mage.intel = 35;
mage.agility = 10;
mage.strength = 5;

warrior.attack(mage);
mage.attack(warrior);
