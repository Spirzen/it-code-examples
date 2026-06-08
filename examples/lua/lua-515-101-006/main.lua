local Class = {}
Class.__index = Class

function Class.new(initial_value)
  local self = setmetatable({}, Class)
  self.value = initial_value or 0
  return self
end

function Class:increment(amount)
  self.value = self.value + (amount or 1)
  return self.value
end

function Class:get_value()
  return self.value
end

-- использование
local instance = Class.new(10)
instance:increment(5)
print(instance:get_value())  -- 15
