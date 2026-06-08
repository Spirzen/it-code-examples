class Unit
  attr_accessor :name, :intel, :agility, :strength, :health, :mana, :level

  def initialize
    @name = "Имя"
    @intel = 10
    @agility = 10
    @strength = 10
    @health = 100
    @mana = 50
    @level = 1
  end

  def damage
    (@intel + @agility + @strength) + (@level * 2)
  end

  def attack(target)
    puts "#{@name} атакует #{target.name} и наносит #{damage} единиц урона."
    target.health -= damage
    puts "#{target.name} теперь имеет #{target.health} здоровья."
  end
end

warrior = Unit.new
warrior.name = "Воин"
warrior.intel = 5
warrior.agility = 15
warrior.strength = 30

mage = Unit.new
mage.name = "Маг"
mage.intel = 35
mage.agility = 10
mage.strength = 5

warrior.attack(mage)
mage.attack(warrior)
