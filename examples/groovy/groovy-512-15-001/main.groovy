class Unit {
    String name = "Имя"
    int intel = 10
    int agility = 10
    int strength = 10
    int health = 100
    int mana = 50
    int level = 1

    int getDamage() {
        (intel + agility + strength) + (level * 2)
    }

    void attack(Unit target) {
        println "${name} атакует ${target.name} и наносит ${damage} единиц урона."
        target.health -= damage
        println "${target.name} теперь имеет ${target.health} здоровья."
    }
}

def warrior = new Unit()
warrior.name = "Воин"
warrior.intel = 5
warrior.agility = 15
warrior.strength = 30

def mage = new Unit()
mage.name = "Маг"
mage.intel = 35
mage.agility = 10
mage.strength = 5

warrior.attack(mage)
mage.attack(warrior)
