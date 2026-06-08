local Vec2 = { x = 0, y = 0 }

function Vec2:new(x, y)
  local obj = { x = x or 0, y = y or 0 }
  setmetatable(obj, self)
  self.__index = self
  return obj
end

function Vec2:__add(other)
  return Vec2:new(self.x + other.x, self.y + other.y)
end

local a = Vec2:new(1, 2)
local b = Vec2:new(3, 4)
local c = a + b
print(c.x, c.y)  -- 4 6
