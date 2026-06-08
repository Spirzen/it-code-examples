class Duck
  def quack
    "Quack!"
  end
  
  def walk
    "Waddle waddle"
  end
  
  def swim
    "Paddle paddle"
  end
end

class Person
  def quack
    "Человек подражает утке: Кря-кря!"
  end
  
  def walk
    "Человек идет"
  end
  
  def swim
    "Человек плавает"
  end
end

class Robot
  def quack
    "Механическое кря-кря"
  end
  
  def walk
    "Робот шагает"
  end
  
  def swim
    "Робот не умеет плавать"
  end
end

def make_it_duck(duck_like)
  puts duck_like.quack
  puts duck_like.walk
  puts duck_like.swim
  puts "---"
end

duck = Duck.new
person = Person.new
robot = Robot.new

make_it_duck(duck)
# Quack!
# Waddle waddle
# Paddle paddle
# ---

make_it_duck(person)
# Человек подражает утке — Кря-кря!
# Человек идет
# Человек плавает
# ---

make_it_duck(robot)
# Механическое кря-кря
# Робот шагает
# Робот не умеет плавать
# ---
