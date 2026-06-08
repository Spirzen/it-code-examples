--!strict
-- В обработчике монеты (сервер)

local function grantCoinOnce(player: Player, coinId: string, amount: number)
    local tags = player:FindFirstChild("CoinTags") :: Folder?
    if not tags then
        tags = Instance.new("Folder")
        tags.Name = "CoinTags"
        tags.Parent = player
    end
    if tags:FindFirstChild(coinId) then
        return
    end
    local tag = Instance.new("BoolValue")
    tag.Name = coinId
    tag.Parent = tags

    DataModule.increment(player, "Coins", amount)
    local ls = player:FindFirstChild("leaderstats")
    local coins = ls and ls:FindFirstChild("Coins") :: IntValue?
    if coins then
        coins.Value = DataModule.get(player).Coins
    end
end
