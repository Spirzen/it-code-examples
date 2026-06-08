local DataStoreService = game:GetService("DataStoreService")

-- Используем изолированное имя, чтобы не конфликтовать с другими играми
local STORE_NAME = "EconomyData_v2"
local RETRY_DELAY = 3
local MAX_RETRIES = 3

local DataStoreAdapter = {}

-- Загрузка данных игрока
function DataStoreAdapter.LoadAsync(player)
    local userId = player.UserId
    local success, data = pcall(function()
        return DataStoreService:GetDataStore(STORE_NAME):GetAsync("Player_" .. userId)
    end)

    if not success then
        warn("DataStore load failed for", player.Name, "-", Данные)
        return nil
    end

    -- Если данных нет — создаём шаблон
    if not Данные then
        data = {
            Coins = 0,
            Inventory = {},
            PurchaseHistory = {}
        }
    end

    return Данные
end

-- Сохранение с повторными попытками
function DataStoreAdapter.SaveAsync(player, Данные)
    local userId = player.UserId
    local key = "Player_" .. userId

    for i = 1, MAX_RETRIES do
        local success, err = pcall(function()
            DataStoreService:GetDataStore(STORE_NAME):SetAsync(key, Данные)
        end)

        if success then
            return true
        elseif i == MAX_RETRIES then
            warn("DataStore save failed after retries for", player.Name, "-", err)
            return false
        else
            task.wait(RETRY_DELAY)
        end
    end
end

return DataStoreAdapter
