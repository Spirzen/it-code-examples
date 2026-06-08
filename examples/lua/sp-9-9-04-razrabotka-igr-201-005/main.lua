local pendingSaves = {}

local function scheduleSave(player)
    if pendingSaves[player] then return end
    pendingSaves[player] = true

    task.delay(30, function() -- сохраняем раз в 30 сек
        if player and player.Parent then
            local data = player:GetAttribute("PlayerData")
            if Данные then
                safeSetAsync(DS, "Player_" .. player.UserId, Данные)
            end
        end
        pendingSaves[player] = nil
    end)
end
