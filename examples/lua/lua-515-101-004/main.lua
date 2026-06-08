-- глобальная функция (избегать)
function global_helper()
  -- реализация
end

-- локальная функция (предпочтительно)
local function calculate_score(kills, assists, deaths)
  return kills * 10 + assists * 5 - deaths * 3
end

-- метод таблицы
local Player = {}
function Player:take_damage(amount)
  self.health = self.health - amount
  if self.health <= 0 then
    self:die()
  end
end
