# Слишком глубокое наследование
class Vehicle; end
class Car < Vehicle; end
class ElectricCar < Car; end
class LuxuryElectricCar < ElectricCar; end

# Композиция
class Vehicle
  attr_reader :engine, :features

  def initialize(engine:, features: [])
    @engine = engine
    @features = features
  end
end

electric_engine = ElectricEngine.new(battery_capacity: 100)
luxury_features = [LeatherSeats.new, PremiumSoundSystem.new]

car = Vehicle.new(engine: electric_engine, features: luxury_features)
