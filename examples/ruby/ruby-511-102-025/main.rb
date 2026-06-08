# Ruby 1.8
"hello".each_byte { |b| puts b }  # Работает с байтами

# Ruby 1.9+
"hello".each_char { |c| puts c }  # Работает с символами

# Новые возможности в более поздних версиях
# Ruby 2.0+ - ключевые слова в методах
def create_user(name:, email:, age: 18)
  { name: name, email: email, age: age }
end

# Ruby 2.1+ - required keyword arguments
def create_user(name:, email:)
  { name: name, email: email }
end

# Ruby 2.7+ - numbered parameters
[1, 2, 3].map { _1 * 2 }  # [2, 4, 6]

# Ruby 3.0+ - правый аргумент оператора присваивания
1 => x
puts x  # 1
