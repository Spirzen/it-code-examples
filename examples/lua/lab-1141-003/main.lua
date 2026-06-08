--!strict

local coin = script.Parent :: BasePart
local collected = false

local function onTouched(other: BasePart)
    if collected then
        return
    end

    local character = other.Parent
    if not character then
        return
    end

    local player = game:GetService("Players"):GetPlayerFromCharacter(character)
    if not player then
        return
    end

    local leaderstats = player:FindFirstChild("leaderstats")
    local coins = leaderstats and leaderstats:FindFirstChild("Coins") :: IntValue?
    if not coins then
        return
    end

    collected = true
    coins.Value += 1
    coin.Transparency = 1
    coin.CanTouch = false
end

coin.Touched:Connect(onTouched)
