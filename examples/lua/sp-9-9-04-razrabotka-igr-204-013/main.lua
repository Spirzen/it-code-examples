--!strict
local DataStoreService = game:GetService("DataStoreService")
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local PurchaseHistory = DataStoreService:GetDataStore("PurchaseHistory_v1")

MarketplaceService.ProcessReceipt = function(receiptInfo)
    local player = Players:GetPlayerByUserId(receiptInfo.PlayerId)
    if not player then
        return Enum.ProductPurchaseDecision.NotProcessedYet
    end
    local purchaseId = receiptInfo.PurchaseId
    local ok, already = pcall(function()
        return PurchaseHistory:GetAsync(tostring(purchaseId))
    end)
    if ok and already then
        return Enum.ProductPurchaseDecision.PurchaseGranted
    end
    -- выдача награды по receiptInfo.ProductId
    DataModule.increment(player, "Coins", 500)
    pcall(function()
        PurchaseHistory:SetAsync(tostring(purchaseId), true)
    end)
    DataModule.save(player)
    return Enum.ProductPurchaseDecision.PurchaseGranted
end
