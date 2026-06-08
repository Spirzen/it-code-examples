-- Сервер — валидация цены и выдача Tool
ShopPurchase.OnServerEvent:Connect(function(player, itemId: string)
    local PRICE = { SpeedCoil = 50 }
    local price = PRICE[itemId]
    if not price then
        return
    end
    local data = DataModule.get(player)
    if data.Coins < price then
        return
    end
    DataModule.increment(player, "Coins", -price)
    -- выдать Tool из ServerStorage в Backpack
    DataModule.save(player)
    pushStats(player) -- ваша функция обновления GUI
end)
