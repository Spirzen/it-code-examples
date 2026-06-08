local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local MarketplaceService = game:GetService("MarketplaceService")

local player = Players.LocalPlayer
local BuyEvent = ReplicatedStorage.RemoteEvents.BuyItem
local BalanceEvent = ReplicatedStorage.RemoteEvents.RequestBalance

-- Получаем элементы GUI (предполагаем, что они уже созданы в дизайнере)
local balanceLabel = script.Parent:WaitForChild("BalanceLabel")
local swordButton = script.Parent:WaitForChild("SwordButton")
local coinsButton = script.Parent:WaitForChild("CoinsButton")

-- Запрашиваем баланс при открытии
BalanceEvent:FireServer()
BalanceEvent.OnClientEvent:Connect(function(action, Данные)
    if action == "Response" or action == "Update" then
        balanceLabel.Text = "Монет: " .. (data.Balance or 0)
    end
end)

-- Покупка меча за монеты
swordButton.MouseButton1Click:Connect(function()
    local txId = "tx_" .. tick() .. "_" .. math.random(1000, 9999)
    BuyEvent:FireServer("Sword_Fire", txId)
end)

-- Покупка монет за Robux
coinsButton.MouseButton1Click:Connect(function()
    -- Получаем ID продукта по имени (из серверного маппинга)
    local success, mapping = pcall(function()
        return ReplicatedStorage:WaitForChild("DevProductMapping"):GetAttribute("Products")
    end)

    if success and mapping and mapping.prod_coins_1k then
        MarketplaceService:PromptPurchase(player, mapping.prod_coins_1k)
    else
        warn("Developer product not configured")
    end
end)

-- Обработка ответа от сервера
BuyEvent.OnClientEvent:Connect(function(status, Данные)
    if status == "Success" then
        print("Успешно куплено:", data.ItemId)
        -- Можно показать эффект, звук, обновить инвентарь
    elseif status == "Failed" then
        if data.Reason == "InsufficientFunds" then
            warn("Недостаточно монет")
        else
            warn("Покупка не удалась")
        end
    end
end)
