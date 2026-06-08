local Mammal = setmetatable({}, { __index = Animal })
Mammal.__index = Mammal

function Mammal:new(name)
    local mammal = Animal.new(Animal, name)
    setmetatable(mammal, self)
    mammal.hasHair = true
    return mammal
end

function Mammal:nurse()
    print(self.name .. " кормит детёнышей молоком")
end

local Cat = setmetatable({}, { __index = Mammal })
Cat.__index = Cat

function Cat:new(name)
    local cat = Mammal:new(name)
    setmetatable(cat, self)
    cat.meow = true
    return cat
end

function Cat:speak()
    print(self.name .. " мяукает: Мяу!")
end

local myCat = Cat:new("Барсик")
myCat:speak() -- Мяукает: Мяу!
myCat:nurse() -- Барсик кормит детенышей молоком
print(myCat.hasHair) -- true
print(myCat.age) -- 0
