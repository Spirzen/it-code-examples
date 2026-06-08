local Vehicle = {}
Vehicle.__index = Vehicle

function Vehicle:new(type)
    local vehicle = setmetatable({}, {__index = self})
    vehicle.type = type
    vehicle.fuelLevel = 0
    return vehicle
end

function Vehicle:refuel(amount)
    self.fuelLevel = self.fuelLevel + amount
end

local Car = setmetatable({}, { __index = Vehicle })
Car.__index = Car

function Car:new(model, color)
    local car = Vehicle.new(Vehicle, "Car")
    setmetatable(car, self)
    car.model = model
    car.color = color
    car.wheels = 4
    return car
end

local myCar = Car:new("Tesla Model S", "Red")
print(myCar.type) -- Car
print(myCar.model) -- Tesla Model S
print(myCar.wheels) -- 4
