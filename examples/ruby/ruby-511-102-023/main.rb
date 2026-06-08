class AdvancedAttributes
  # Базовые атрибуты
  attr_accessor :name, :age
  
  # Только для чтения
  attr_reader :created_at
  
  # Только для записи
  attr_writer :password
  
  # С валидацией
  def email=(value)
    if value =~ /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i
      @email = value
    else
      raise ArgumentError, "Неверный формат email"
    end
  end
  
  attr_reader :email
  
  # С преобразованием
  def tags=(value)
    @tags = value.is_a?(Array) ? value : value.split(',').map(&:strip)
  end
  
  attr_reader :tags
  
  # С кэшированием
  def expensive_calculation
    @expensive_calculation ||= begin
      sleep(1)  # Имитация долгого вычисления
      rand(1000)
    end
  end
  
  def initialize(name, age)
    @name = name
    @age = age
    @created_at = Time.now
  end
end

obj = AdvancedAttributes.new("Test", 25)
obj.name = "New Name"
puts obj.name  # New Name

obj.email = "test@example.com"
puts obj.email  # test@example.com

obj.tags = "ruby, programming, oop"
puts obj.tags.inspect  # ["ruby", "programming", "oop"]

obj.tags = ["ruby", "rails"]
puts obj.tags.inspect  # ["ruby", "rails"]

result1 = obj.expensive_calculation  # Выполняется 1 секунду
result2 = obj.expensive_calculation  # Мгновенно, использует кэш
puts result1 == result2  # true
