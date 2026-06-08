--!strict

local Players = game:GetService("Players")
local player = Players.LocalPlayer
local label = script.Parent :: TextLabel

local function updateCoins()
    local leaderstats = player:FindFirstChild("leaderstats")
    local coins = leaderstats and leaderstats:FindFirstChild("Coins") :: IntValue?
    if coins then
        label.Text = "Монеты: " . tostring(coins.Value)
    end
end

local function hookCoins()
    local leaderstats = player:WaitForChild("leaderstats", 10)
    if not leaderstats then
        warn("leaderstats не найден за 10 с")
        return
    end
    local coins = leaderstats:WaitForChild("Coins", 10) :: IntValue?
    if not coins then
        return
    end
    updateCoins()
    coins.Changed:Connect(updateCoins)
end

player.CharacterAdded:Connect(hookCoins)
if player:FindFirstChild("leaderstats") then
    hookCoins()
end
