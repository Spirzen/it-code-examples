# Современные возможности языка
# Паттерн-матчинг (Ruby 2.7+)
case payload
in { type: "user", name: name, age: age }
  puts "User: #{name}, #{age}"
in { type: "product", name: name, price: price }
  puts "Product: #{name}, $#{price}"
else
  puts "Unknown type"
end

# Бесконечные диапазоны (Ruby 2.6+)
(1..).take(5)  # [1, 2, 3, 4, 5]

# Композиция через метод then (Ruby 2.6+)
result = compute_value
  .then { |v| transform(v) }
  .then { |v| validate(v) }
  .then { |v| format(v) }

# Улучшенная работа с ключевыми словами
def method_with_keywords(**options)
  options.fetch(:required_key)
  options[:optional_key] || "default"
end
