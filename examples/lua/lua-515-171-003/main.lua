local Car = {}

function Car:new(model)
    local instance = setmetatable({}, {__index = self})
    return instance
end

function Car:init(model)
    self.model = model
    self.speed = 0
end

local myCar = Car:new("Toyota")
myCar:init("Toyota") -- Явный вызов инициализации
