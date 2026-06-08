class Animal
  def initialize(name)
    @name = name
  end
  
  def speak
    "Some sound"
  end
  
  def info
    "I am #{@name}"
  end
end

class Dog < Animal
  def speak
    "Woof!"
  end
  
  def fetch
    "Fetching the ball!"
  end
end

class Cat < Animal
  def speak
    "Meow!"
  end
  
  def purr
    "Purrrring..."
  end
end

dog = Dog.new("Рекс")
cat = Cat.new("Мурка")

puts dog.speak    # Woof!
puts cat.speak    # Meow!
puts dog.info     # I am Рекс
puts cat.info     # I am Мурка
puts dog.fetch    # Fetching the ball!
puts cat.purr     # Purrrring...
