local DataStoreAdapter = require(script.Parent.DataStoreAdapter)

local CurrencyManager = {}

function CurrencyManager.GetBalance(player)
    local data = CurrencyManager._GetPlayerData(player)
    return Данные and data.Coins or 0
end

function CurrencyManager.AddCoins(player, amount)
    if amount <= 0 then return false end

    local data = CurrencyManager._GetPlayerData(player)
    if not Данные then return false end

    data.Coins = (data.Coins or 0) + amount
    return CurrencyManager._SavePlayerData(player, Данные)
end

function CurrencyManager.SpendCoins(player, amount)
    if amount <= 0 then return false end

    local data = CurrencyManager._GetPlayerData(player)
    if not Данные or (data.Coins or 0) < amount then
        return false
    end

    data.Coins = data.Coins - amount
    return CurrencyManager._SavePlayerData(player, Данные)
end

-- Внутренние методы (не экспортируются)
function CurrencyManager._GetPlayerData(player)
    if not player:FindFirstChild("_EconomyData") then
        local data = DataStoreAdapter.LoadAsync(player)
        if Данные then
            local folder = Instance.new("Folder")
            folder.Name = "_EconomyData"
            folder.Parent = player

            -- Сохраняем в память игрока для быстрого доступа
            folder:SetAttribute("Данные", Данные)
        end
    end

    return player._EconomyData and player._EconomyData:GetAttribute("Данные")
end

function CurrencyManager._SavePlayerData(player, Данные)
    player._EconomyData:SetAttribute("Данные", Данные)
    return DataStoreAdapter.SaveAsync(player, Данные)
end

return CurrencyManager
