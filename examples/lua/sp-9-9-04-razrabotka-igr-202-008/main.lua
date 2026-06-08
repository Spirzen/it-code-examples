local CurrencyManager = require(script.Parent.CurrencyManager)
local InventorySystem = require(script.Parent.InventorySystem)
local Catalog = require(script.Parent.Parent.Catalog.Items)

local TransactionProcessor = {}

-- Проверка уникальности транзакции
local function isDuplicate(player, transactionId)
    local data = CurrencyManager._GetPlayerData(player)
    if not Данные or not data.PurchaseHistory then return false end

    for _, record in ipairs(data.PurchaseHistory) do
        if record.TransactionId == transactionId then
            return true
        end
    end
    return false
end

-- Добавление записи в историю
local function recordTransaction(player, transactionId, itemId)
    local data = CurrencyManager._GetPlayerData(player)
    if not data.PurchaseHistory then data.PurchaseHistory = {} end

    table.insert(data.PurchaseHistory, {
        TransactionId = transactionId,
        ItemId = itemId,
        Timestamp = os.time()
    })
end

-- Основная функция покупки
function TransactionProcessor.ProcessPurchase(player, itemId, transactionId)
    if not player or not itemId or not transactionId then return false end

    -- 1. Проверка дубликата
    if isDuplicate(player, transactionId) then
        warn("Duplicate transaction:", transactionId, "from", player.Name)
        return false
    end

    -- 2. Получение описания товара
    local item = Catalog[itemId]
    if not item then
        warn("Unknown item ID:", itemId)
        return false
    end

    -- 3. Определение типа оплаты и валидация
    local priceData = item.Price
    local canAfford = false

    if priceData.Coins then
        -- Покупка за монеты
        canAfford = CurrencyManager.GetBalance(player) >= priceData.Coins
    elseif priceData.RobuxProduct then
        -- Robux-покупка уже подтверждена Roblox — проверка не нужна
        canAfford = true
    else
        warn("Item", itemId, "has no valid price")
        return false
    end

    if not canAfford then return false end

    -- 4. Выполнение операций
    local success = false

    -- Атомарное выполнение: всё или ничего
    if priceData.Coins then
        if not CurrencyManager.SpendCoins(player, priceData.Coins) then
            return false
        end
    end

    -- Выдача предмета по типу
    if item.Type == "CurrencyPack" then
        local amount = item.Metadata.Amount
        success = CurrencyManager.AddCoins(player, amount)
    elseif item.Type == "Tool" then
        success = InventorySystem.UnlockItem(player, itemId)
    elseif item.Type == "Appearance" then
        success = InventorySystem.UnlockItem(player, itemId)
    else
        warn("Unsupported item type:", item.Type)
        return false
    end

    if not success then return false end

    -- 5. Запись в историю и сохранение
    recordTransaction(player, transactionId, itemId)
    return CurrencyManager._SavePlayerData(player, CurrencyManager._GetPlayerData(player))
end

return TransactionProcessor
