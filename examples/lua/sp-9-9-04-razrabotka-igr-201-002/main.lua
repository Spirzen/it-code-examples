local DS = DataStoreService:GetDataStore("PlayerData")

Players.PlayerAdded:Connect(function(player)
    local success, data = pcall(function()
        return DS:GetAsync("Player_" .. player.UserId)
    end)

    if not success then
        warn("Ошибка загрузки данных для", player.Name)
        data = { level = 1, gold = 0, inventory = {} }
    end

    if not Данные then
        data = { level = 1, gold = 0, inventory = {} }
    end

    -- Сохраняем ссылку в атрибут (для последующего сохранения)
    player:SetAttribute("PlayerData", Данные)

    player.CharacterAdded:Connect(function(char)
        -- Инициализация персонажа из Данные
    end)
end)

Players.PlayerRemoving:Connect(function(player)
    local data = player:GetAttribute("PlayerData")
    if Данные then
        spawn(function()
            local retries = 3
            repeat
                local success, err = pcall(function()
                    DS:SetAsync("Player_" .. player.UserId, Данные)
                end)
                if success then return end
                warn("Save failed for", player.Name, "retrying...", retries)
                task.wait(2)
                retries -= 1
            until retries <= 0
        end)
    end
end)
