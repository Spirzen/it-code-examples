class Vehicle
  def initialize(make, model, year)
    @make = make
    @model = model
    @year = year
  end
  
  def info
    "#{@year} #{@make} #{@model}"
  end
  
  def start_engine
    "Двигатель запущен"
  end
end

class Car < Vehicle
  def initialize(make, model, year, doors)
    super(make, model, year)
    @doors = doors
  end
  
  def info
    "#{super}, #{@doors} дверей"
  end
  
  def start_engine
    "#{super}. Автомобиль готов к движению!"
  end
end

class Motorcycle < Vehicle
  def initialize(make, model, year, has_sidecar)
    super(make, model, year)
    @has_sidecar = has_sidecar
  end
  
  def info
    sidecar_info = @has_sidecar ? " с коляской" : ""
    "#{super}#{sidecar_info}"
  end
  
  def start_engine
    "#{super}. Мотоцикл ревет!"
  end
end

car = Car.new("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle.new("Harley", "Sportster", 2019, true)

puts car.info           # 2020 Toyota Camry, 4 дверей
puts motorcycle.info    # 2019 Harley Sportster с коляской
puts car.start_engine   # Двигатель запущен. Автомобиль готов к движению!
puts motorcycle.start_engine # Двигатель запущен. Мотоцикл ревет!
