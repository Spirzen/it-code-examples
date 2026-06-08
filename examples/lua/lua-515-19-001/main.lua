-- файл: math_utils.lua
local M = {}

function M.square(x)
  return x * x
end

function M.cube(x)
  return x * x * x
end

-- Приватная функция (не экспортируется)
local function is_positive(x)
  return x > 0
end

return M
