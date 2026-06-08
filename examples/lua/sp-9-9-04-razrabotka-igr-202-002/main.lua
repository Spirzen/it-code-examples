   local BuyEvent = script.Parent:WaitForChild("BuyItem")

   BuyEvent.OnServerEvent:Connect(function(player, itemId, transactionId)
       if not player or not itemId or not transactionId then return end

       -- Проверка дубликата транзакции
       if isTransactionProcessed(player.UserId, transactionId) then
           warn("Duplicate transaction:", transactionId)
           return
       end

       local catalog = require(game.ReplicatedStorage.Catalog.Items)
       local item = catalog[itemId]
       if not item then return end

       local playerData = getPlayerData(player) -- загрузка из DataStore или кэша
       if not playerData then return end

       -- Валидация: достаточно ли валюты?
       local cost = item.Price.Coins
       if cost and playerData.Coins < cost then
           -- Отправить отказ клиенту
           fireClientEvent(player, "PurchaseFailed", { Reason = "InsufficientFunds" })
           return
       end

       -- Атомарное выполнение
       if commitPurchase(player, playerData, item, transactionId) then
           fireClientEvent(player, "PurchaseSuccess", { ItemId = itemId })
       else
           fireClientEvent(player, "PurchaseFailed", { Reason = "ServerError" })
       end
   end)
