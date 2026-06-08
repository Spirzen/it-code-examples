class LivingBeing
  def initialize(name)
    @name = name
  end
  
  def breathe
    "Дышит"
  end
end

class Animal < LivingBeing
  def initialize(name, species)
    super(name)
    @species = species
  end
  
  def move
    "Передвигается"
  end
end

class Mammal < Animal
  def initialize(name, species)
    super(name, species)
  end
  
  def feed_young
    "Кормит детенышей молоком"
  end
end

class Dog < Mammal
  def initialize(name, breed)
    super(name, "Canis lupus familiaris")
    @breed = breed
  end
  
  def bark
    "Гавкает"
  end
  
  def info
    "#{@name} - это собака породы #{@breed}, вид #{@species}"
  end
end

class Cat < Mammal
  def initialize(name, color)
    super(name, "Felis catus")
    @color = color
  end
  
  def meow
    "Мяукает"
  end
  
  def info
    "#{@name} - это кошка цвета #{@color}, вид #{@species}"
  end
end

dog = Dog.new("Бобик", "Овчарка")
cat = Cat.new("Мурка", "Рыжая")

puts dog.info           # Бобик - это собака породы Овчарка, вид Canis lupus familiaris
puts cat.info           # Мурка - это кошка цвета Рыжая, вид Felis catus
puts dog.breathe        # Дышит
puts dog.move           # Передвигается
puts dog.feed_young     # Кормит детенышей молоком
puts dog.bark           # Гавкает
puts cat.meow           # Мяукает
