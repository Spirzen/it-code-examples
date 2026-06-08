--[[
  Модуль векторной математики для двумерного пространства.
  
  Примеры:
    local v1 = Vector2.new(3, 4)
    local v2 = Vector2.new(1, 2)
    local sum = v1:add(v2)        -- Vector2(4, 6)
    local length = v1:length()    -- 5.0
    local normalized = v1:normalize()  -- Vector2(0.6, 0.8)
]]
local Vector2 = {}
Vector2.__index = Vector2

function Vector2.new(x, y)
  return setmetatable({ x = x or 0, y = y or 0 }, Vector2)
end

-- ... реализация методов
