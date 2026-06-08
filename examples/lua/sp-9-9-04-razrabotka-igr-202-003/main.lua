local MarketplaceService = game:GetService("MarketplaceService")
local DataStoreService = game:GetService("DataStoreService")

MarketplaceService.PromptPurchaseFinished:Connect(function(player, productId, purchased)
    if not purchased then return end

    local productMap = {
        [123456789] = "Coins_1000", -- ID продукта → внутренний ID товара
        [987654321] = "Skin_Warrior_Red"
    }

    local internalId = productMap[productId]
    if not internalId then
        warn("Unknown product ID:", productId)
        return
    end

    local transactionId = "robux_" .. productId .. "_" .. os.time()
    if isTransactionProcessed(player.UserId, transactionId) then return end

    local playerData = getPlayerData(player)
    local catalog = require(game.ReplicatedStorage.Catalog.Items)
    local item = catalog[internalId]

    if item and commitPurchase(player, playerData, item, transactionId) then
        -- Успешно
    else
        -- Логирование ошибки — без уведомления игрока (во избежание спама)
    end
end)
