-- Server
local CollectionService = game:GetService("CollectionService")

-- Где-то при инициализации:
CollectionService:AddTag(door1, "Door")
CollectionService:AddTag(door2, "Door")

-- Глобальный обработчик
CollectionService.InstanceAdded:Connect(function(tag, obj)
    if tag == "Door" then
        local proximity = Instance.new("ProximityPrompt")
        proximity.ActionText = "Открыть"
        proximity.Parent = obj
        -- ... настройка
    end
end)
