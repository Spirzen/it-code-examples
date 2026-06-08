local Janitor = require(ReplicatedStorage.Janitor)

local janitor = Janitor.new()

-- Подключение события
janitor:Add(player.CharacterAdded:Connect(function(char)
    -- ...
end))

-- Отложенное удаление
janitor:Add(function()
    print("Очистка завершена")
end)

-- Привязка к объекту
script:WaitForChild("Janitor", 5)
if script.Janitor then
    script.Janitor:Destroy()
end
script.Janitor = janitor
