local InventorySystem = {}

function InventorySystem.UnlockItem(player, itemId)
    local data = require(script.Parent.CurrencyManager)._GetPlayerData(player)
    if not Данные then return false end

    if not data.Inventory then data.Inventory = {} end
    data.Inventory[itemId] = data.Inventory[itemId] or {}
    data.Inventory[itemId].Unlocked = true

    return require(script.Parent.CurrencyManager)._SavePlayerData(player, Данные)
end

function InventorySystem.IsItemUnlocked(player, itemId)
    local data = require(script.Parent.CurrencyManager)._GetPlayerData(player)
    return Данные and data.Inventory and data.Inventory[itemId] and data.Inventory[itemId].Unlocked
end

return InventorySystem
