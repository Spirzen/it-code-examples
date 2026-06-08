local Animal = {}
Animal.__index = Animal

function Animal.new(name)
  local self = setmetatable({}, Animal)
  self.name = name
  return self
end

function Animal:speak()
  return "..."
end

local Dog = setmetatable({}, { __index = Animal })
Dog.__index = Dog

function Dog.new(name, breed)
  local self = Animal.new(name)
  return setmetatable(self, Dog)
end

function Dog:speak()
  return "Woof!"
end

local my_dog = Dog.new("Rex", "Shepherd")
print(my_dog:speak())  -- Woof!
print(my_dog.name)     -- Rex
