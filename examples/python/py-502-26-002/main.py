class Unit:
    def __init__(self):
        self.name = "Имя"
        self.intel = 10
        self.agility = 10
        self.strength = 10
        self.health = 100
        self.mana = 50
        self.level = 1

    @property
    def damage(self):
        return (self.intel + self.agility + self.strength) + (self.level * 2)

    def attack(self, target):
        print(f"{self.name} атакует {target.name} и наносит {self.damage} единиц урона.")
        target.health -= self.damage
        print(f"{target.name} теперь имеет {target.health} здоровья.")


warrior = Unit()
warrior.name = "Воин"
warrior.intel = 5
warrior.agility = 15
warrior.strength = 30

mage = Unit()
mage.name = "Маг"
mage.intel = 35
mage.agility = 10
mage.strength = 5

warrior.attack(mage)
mage.attack(warrior)
