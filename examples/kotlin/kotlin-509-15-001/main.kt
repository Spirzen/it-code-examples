class Unit {
    var name = "Имя"
    var intel = 10
    var agility = 10
    var strength = 10
    var health = 100
    var mana = 50
    var level = 1

    val damage: Int
        get() = (intel + agility + strength) + (level * 2)

    fun attack(target: Unit) {
        println("$name атакует ${target.name} и наносит $damage единиц урона.")
        target.health -= damage
        println("${target.name} теперь имеет $health здоровья.")
    }
}

fun main() {
    val warrior = Unit()
    warrior.name = "Воин"
    warrior.intel = 5
    warrior.agility = 15
    warrior.strength = 30

    val mage = Unit()
    mage.name = "Маг"
    mage.intel = 35
    mage.agility = 10
    mage.strength = 5

    warrior.attack(mage)
    mage.attack(warrior)
}
