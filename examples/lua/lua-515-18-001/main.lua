Unit = {}

function Unit:new()
    local instance = {
        name = "Имя",
        intel = 10,
        agility = 10,
        strength = 10,
        health = 100,
        mana = 50,
        level = 1
    }
    setmetatable(instance, self)
    self.__index = self
    return instance
end

function Unit:damage()
    return (self.intel + self.agility + self.strength) + (self.level * 2)
end

function Unit:attack(target)
    local dmg = self:damage()
    print(self.name .. " атакует " .. target.name .. " и наносит " .. dmg .. " единиц урона.")
    target.health = target.health - dmg
    print(target.name .. " теперь имеет " .. target.health .. " здоровья.")
end

local warrior = Unit:new()
warrior.name = "Воин"
warrior.intel = 5
warrior.agility = 15
warrior.strength = 30

local mage = Unit:new()
mage.name = "Маг"
mage.intel = 35
mage.agility = 10
mage.strength = 5

warrior:attack(mage)
mage:attack(warrior)
