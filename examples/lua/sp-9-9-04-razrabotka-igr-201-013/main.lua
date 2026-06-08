-- Script в ServerScriptService (имя не важно)
local MarketplaceService = game:GetService("MarketplaceService")

MarketplaceService.ProcessReceipt = function(receiptInfo)
    local userId = receiptInfo.PlayerId
    local productId = receiptInfo.ProductId
    local purchaseId = receiptInfo.PurchaseId

    -- 1. Валидация: не обработан ли уже?
    local dataStore = DataStoreService:GetDataStore("Purchases")
    local success, alreadyProcessed = pcall(function()
        return dataStore:GetAsync("Purchase_" .. purchaseId)
    end)

    if success and alreadyProcessed then
        return Enum.ProductPurchaseDecision.PurchaseGranted
    end

    -- 2. Выдача товара
    local player = Players:GetPlayerByUserId(userId)
    if player then
        if productId == 987654321 then -- "1000 Gold"
            local data = player:GetAttribute("PlayerData") or {}
            data.gold = (data.gold or 0) + 1000
            player:SetAttribute("PlayerData", Данные)
        end
    else
        -- Игрок оффлайн — сохранить в DataStore для последующей выдачи
        local deferred = dataStore:GetAsync("Deferred_" .. userId) or {}
        table.insert(deferred, { productId = productId, time = tick() })
        dataStore:SetAsync("Deferred_" .. userId, deferred)
    end

    -- 3. Подтверждение обработки
    pcall(function()
        dataStore:SetAsync("Purchase_" .. purchaseId, true)
    end)

    return Enum.ProductPurchaseDecision.PurchaseGranted
end
