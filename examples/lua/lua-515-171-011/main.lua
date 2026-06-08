local Animal = {}
Animal.__index = Animal

function Animal:new(name)
    local animal = setmetatable({}, {__index = self})
    animal.name = name
    animal.age = 0
    return animal
end

function Animal:speak()
    print(self.name .. " издает звук")
end

-- Создание дочернего класса
local Dog = setmetatable({}, { __index = Animal })
Dog.__index = Dog

function Dog:new(name, breed)
    local dog = Animal.new(Animal, name)
    setmetatable(dog, self)
    dog.breed = breed
    return dog
end

function Dog:speak()
    print(self.name .. " лает: Гав!")
end

-- Использование
local myDog = Dog:new("Рекс", "Лабрадор")
myDog:speak() -- Выведет: Рекс лает: Гав!
print(myDog.age) -- 0 (наследовано от Animal)
