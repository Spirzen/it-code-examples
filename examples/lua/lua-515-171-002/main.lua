local Rectangle = {}

Rectangle.width = 0
Rectangle.height = 0

function Rectangle:new(w, h)
    local instance = setmetatable({}, {__index = self})
    instance.width = w or 0
    instance.height = h or 0
    return instance
end

function Rectangle:getArea()
    return self.width * self.height
end

-- Использование конструктора
local rect1 = Rectangle:new(10, 5)
print(rect1:getArea()) -- Выведет: 50

local rect2 = Rectangle:new() -- Использует значения по умолчанию
print(rect2:getArea()) -- Выведет: 0
