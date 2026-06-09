local Car = {SERVICE_INTERVAL = 15000, FUEL_PER_KM = 0.1}

function Car:new(brand)
    local obj = setmetatable({brand = brand, fuel = 40.0, mileage = 0}, {__index = self})
    return obj
end

function Car:refuel(liters)
    self.fuel = self.fuel + liters
    print(string.format("Заправка: +%.0f л. Топливо: %.1f л", liters, self.fuel))
end

function Car:drive(km)
    local needed = km * self.FUEL_PER_KM
    if needed > self.fuel then
        print("Ошибка: недостаточно топлива")
        return
    end
    self.fuel = self.fuel - needed
    self.mileage = self.mileage + km
    print(string.format("Проехали %d км. Топливо: %.1f л. Пробег: %d км", km, self.fuel, self.mileage))
    if self.mileage >= self.SERVICE_INTERVAL then
        print("⚠️ ВНИМАНИЕ: требуется техобслуживание!")
    end
end

local car = Car:new("Lada")
car:refuel(10)
car:drive(5000)
car:drive(11000)
