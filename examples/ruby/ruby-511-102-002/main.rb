class Engine
  def start
    "Двигатель запущен"
  end
end

class Car
  def initialize(engine = Engine.new)
    @engine = engine
  end

  def drive
    "#{@engine.start}. Машина едет"
  end
end

puts Car.new.drive
