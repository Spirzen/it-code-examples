class Unit {
    var name: String = "Имя"
    var intel: Int = 10
    var agility: Int = 10
    var strength: Int = 10
    var health: Int = 100
    var mana: Int = 50
    var level: Int = 1

    var damage: Int {
        (intel + agility + strength) + (level * 2)
    }

    func attack(target: Unit) {
        print("\(name) атакует \(target.name) и наносит \(damage) единиц урона.")
        target.health -= damage
        print("\(target.name) теперь имеет \(target.health) здоровья.")
    }
}

let warrior = Unit()
warrior.name = "Воин"
warrior.intel = 5
warrior.agility = 15
warrior.strength = 30

let mage = Unit()
mage.name = "Маг"
mage.intel = 35
mage.agility = 10
mage.strength = 5

warrior.attack(target: mage)
mage.attack(target: warrior)
