local Figure = {}

function Figure:new(name, color)
    local obj = setmetatable({name = name, color = color}, {__index = self})
    return obj
end

function Figure:describe()
    print("Фигура «" .. self.name .. "», цвет: " .. self.color)
end

local Circle = {}
setmetatable(Circle, {__index = Figure})

function Circle:new(color)
    return Figure.new(self, "Круг", color)
end

local Square = {}
setmetatable(Square, {__index = Figure})

function Square:new(color)
    return Figure.new(self, "Квадрат", color)
end

local circle = Circle:new("красный")
local square = Square:new("синий")
circle:describe()
square:describe()
