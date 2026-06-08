local Flyable = {}
Flyable.fly = function(self)
    print(self.name .. " летит")
end

local Swimmable = {}
Swimmable.swim = function(self)
    print(self.name .. " плавает")
end

local Duck = {}
setmetatable(Duck, {__index = Flyable})
-- Добавление второго уровня наследования через ручное копирование или использование таблиц
for k, v in pairs(Swimmable) do
    Duck[k] = v
end

local duck = Duck:new("Утка")
duck:flew() -- Утка летит
duck:swim() -- Утка плавает
