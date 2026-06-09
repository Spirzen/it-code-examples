local Animal = {}

function Animal:new(name)
    local obj = setmetatable({name = name}, {__index = self})
    return obj
end

function Animal:eat()
    print(self.name .. " ест")
end

local Cat = {}
setmetatable(Cat, {__index = Animal})

function Cat:new(name)
    return Animal.new(self, name)
end

function Cat:speak()
    print("Мяу!")
end

local Dog = {}
setmetatable(Dog, {__index = Animal})

function Dog:new(name)
    return Animal.new(self, name)
end

function Dog:speak()
    print("Гав!")
end

local cat = Cat:new("Мурка")
local dog = Dog:new("Шарик")
cat:eat()
cat:speak()
dog:eat()
dog:speak()
