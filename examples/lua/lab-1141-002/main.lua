--!strict

local Players = game:GetService("Players")

local function setupLeaderstats(player: Player)
    local folder = Instance.new("Folder")
    folder.Name = "leaderstats"
    folder.Parent = player

    local coins = Instance.new("IntValue")
    coins.Name = "Coins"
    coins.Value = 0
    coins.Parent = folder
end

Players.PlayerAdded:Connect(setupLeaderstats)
