-- Создаём RemoteEvents, если их нет
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RemoteEvents = ReplicatedStorage:FindFirstChild("RemoteEvents")
if not RemoteEvents then
    RemoteEvents = Instance.new("Folder")
    RemoteEvents.Name = "RemoteEvents"
    RemoteEvents.Parent = ReplicatedStorage
end

local BuyItem = ReplicatedStorage.RemoteEvents:FindFirstChild("BuyItem")
if not BuyItem then
    BuyItem = Instance.new("RemoteEvent")
    BuyItem.Name = "BuyItem"
    BuyItem.Parent = ReplicatedStorage.RemoteEvents
end

local RequestBalance = ReplicatedStorage.RemoteEvents:FindFirstChild("RequestBalance")
if not RequestBalance then
    RequestBalance = Instance.new("RemoteEvent")
    RequestBalance.Name = "RequestBalance"
    RequestBalance.Parent = ReplicatedStorage.RemoteEvents
end

-- Импорт сервисов
local TransactionProcessor = require(ReplicatedStorage.Services.TransactionProcessor)
local CurrencyManager = require(ReplicatedStorage.Services.CurrencyManager)

-- Обработка покупки
BuyItem.OnServerEvent:Connect(function(player, itemId, transactionId)
    if not player:IsA("Player") then return end

    local success = TransactionProcessor.ProcessPurchase(player, itemId, transactionId)
    if success then
        -- Уведомляем клиента об успехе и отправляем новый баланс
        BuyItem:FireClient(player, "Success", { ItemId = itemId })
        task.delay(0.1, function()
            if player and player.Parent then
                RequestBalance:FireClient(player, "Update", { Balance = CurrencyManager.GetBalance(player) })
            end
        end)
    else
        BuyItem:FireClient(player, "Failed", { Reason = "InvalidRequest" })
    end
end)

-- Запрос баланса
RequestBalance.OnServerEvent:Connect(function(player)
    if player and player:IsA("Player") then
        local balance = CurrencyManager.GetBalance(player)
        RequestBalance:FireClient(player, "Response", { Balance = balance })
    end
end)

-- Поддержка Developer Products
local MarketplaceService = game:GetService("MarketplaceService")

-- Карта: имя продукта → внутренний ID
local PRODUCT_MAP = {
    prod_coins_1k = "Coins_1000"
    -- Добавьте другие по мере регистрации в DevHub
}

MarketplaceService.PromptPurchaseFinished:Connect(function(player, productId, purchased)
    if not purchased or not player:IsA("Player") then return end

    -- Получаем имя продукта по ID (в реальном проекте храните маппинг в ModuleScript)
    local productName = nil
    for name, id in pairs(script.Parent.Parent.DevProductMapping:GetAttribute("Products") or {}) do
        if id == productId then
            productName = name
            break
        end
    end

    if not productName then
        warn("Unknown product ID:", productId)
        return
    end

    local internalId = PRODUCT_MAP[productName]
    if not internalId then
        warn("No internal mapping for product:", productName)
        return
    end

    local transactionId = "robux_" .. productName .. "_" .. os.time()
    TransactionProcessor.ProcessPurchase(player, internalId, transactionId)
end)

-- Необязательно: выдача монет при входе (для теста)
game.Players.PlayerAdded:Connect(function(player)
    task.delay(2, function()
        if player and player.Parent then
            CurrencyManager.AddCoins(player, 100) -- стартовый бонус
        end
    end)
end)
