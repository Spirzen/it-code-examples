class DynamicAttributes
  def self.attribute(name, default = nil)
    define_method(name) do
      instance_variable_get("@#{name}") || default
    end
    
    define_method("#{name}=") do |value|
      instance_variable_set("@#{name}", value)
    end
  end
end

class Product < DynamicAttributes
  attribute :name, "Безымянный продукт"
  attribute :price, 0
  attribute :in_stock, true
end

product = Product.new
puts product.name      # Безымянный продукт
puts product.price     # 0
puts product.in_stock  # true

product.name = "Книга"
product.price = 500
product.in_stock = false

puts product.name      # Книга
puts product.price     # 500
puts product.in_stock  # false

# Создание методов на лету
class Calculator
  [:add, :subtract, :multiply, :divide].each do |operation|
    define_method(operation) do |a, b|
      case operation
      when :add then a + b
      when :subtract then a - b
      when :multiply then a * b
      when :divide then a.to_f / b
      end
    end
  end
end

calc = Calculator.new
puts calc.add(5, 3)       # 8
puts calc.subtract(10, 4) # 6
puts calc.multiply(6, 7)  # 42
puts calc.divide(10, 2)   # 5.0
