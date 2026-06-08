--!strict
local SHOP = {
    ["Зелье прыгучести"] = { Price = 50 },
}

local function hookShopPart(part: BasePart)
    local nameVal = part:FindFirstChild("ItemName") :: StringValue?
    if not nameVal then return end
    local itemName = nameVal.Value
    local item = SHOP[itemName]
    if not item then return end
    local template = ReplicatedStorage.ShopItems:FindFirstChild(itemName)
    if not template or not template:IsA("Tool") then return end

    part.Touched:Connect(function(hit)
        local player = playerFromHit(hit)
        if not player then return end
        if DataModule.get(player).Coins < item.Price then return end
        DataModule.increment(player, "Coins", -item.Price)
        local tool = template:Clone()
        tool.Parent = player:FindFirstChild("Backpack")
        DataModule.save(player)
    end)
end
