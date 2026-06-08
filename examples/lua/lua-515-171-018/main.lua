local Shape = {}

function Shape:new()
    local shape = setmetatable({}, {__index = self})
    return shape
end

function Shape:draw()
    print("Рисуется фигура")
end

local Circle = {}
setmetatable(Circle, {__index = Shape})

function Circle:new(radius)
    local circle = Shape.new(self)
    circle.radius = radius
    return circle
end

function Circle:draw()
    print("Рисуется круг радиусом " .. self.radius)
end

local Square = {}
setmetatable(Square, {__index = Shape})

function Square:new(side)
    local square = Shape.new(self)
    square.side = side
    return square
end

function Square:draw()
    print("Рисуется квадрат со стороной " .. self.side)
end

local shapes = {Circle:new(5), Square:new(10), Shape:new()}

for _, s in ipairs(shapes) do
    s:draw()
end
