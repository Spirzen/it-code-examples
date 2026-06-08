// Фабричная функция (без классов и new)
const createWarrior = (name, level) => {
    let health = 100;  // приватная переменная
    
    return {
        name,
        level,
        getHealth: () => health,        // замыкание
        takeDamage: (amount) => { health -= amount; },
        attack: (target) => {
            console.log(`${name} атакует ${target.name}`);
            target.takeDamage(level * 10);
        }
    };
};

const w1 = createWarrior("Артур", 5);
const w2 = createWarrior("Мерлин", 8);
w1.attack(w2);
console.log(w2.getHealth());  // 50 (100 - 50)
