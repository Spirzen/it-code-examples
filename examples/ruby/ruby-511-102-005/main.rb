class TemperatureSensor
  def initialize(initial_temperature)
    @temperature = initial_temperature
    @calibration_factor = 1.0
    @last_reading_time = nil
  end
  
  def read_temperature
    @last_reading_time = Time.now
    @temperature * @calibration_factor
  end
  
  def calibrate(factor)
    @calibration_factor = factor
  end
end

sensor = TemperatureSensor.new(25.5)
puts sensor.read_temperature  # 25.5
sensor.calibrate(1.05)
puts sensor.read_temperature  # 26.775
