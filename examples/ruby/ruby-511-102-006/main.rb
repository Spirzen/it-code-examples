class Product
  def initialize(name, price)
    @name = name
    @price = price
  end
  
  # Геттеры
  def name
    @name
  end
  
  def price
    @price
  end
  
  # Сеттеры
  def name=(new_name)
    @name = new_name
  end
  
  def price=(new_price)
    @price = new_price if new_price >= 0
  end
end

product = Product.new("Книга", 500)
puts product.name    # Книга
puts product.price   # 500

product.name = "Новая книга"
product.price = 600
puts product.name    # Новая книга
puts product.price   # 600
