class Person
  def greet
    "Привет!"
  end
end

person = Person.new
puts person.greet  # Привет!

# Добавление метода в класс во время выполнения
class Person
  def farewell
    "До свидания!"
  end
end

puts person.farewell  # До свидания!

# Изменение существующего метода
class Person
  def greet
    "Здравствуйте!"
  end
end

puts person.greet  # Здравствуйте!

# Добавление метода к конкретному объекту
def person.special_greet
  "Особое приветствие!"
end

puts person.special_greet  # Особое приветствие!
# Person.new.special_greet  # Ошибка — метод не существует для других объектов

# Удаление метода
class Person
  undef_method :farewell
end

# person.farewell  # Ошибка — метод удален
