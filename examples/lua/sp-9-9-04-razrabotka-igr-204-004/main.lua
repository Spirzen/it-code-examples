--!strict

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local DataModule = require(ReplicatedStorage.Modules.DataModule)
local StatsUpdated = ReplicatedStorage.Remotes.StatsUpdated :: RemoteEvent

local function pushStats(player: Player)
    local data = DataModule.get(player)
    StatsUpdated:FireClient(player, data.Coins, data.Stage, data.Wins)
end

local function setupLeaderstats(player: Player, data: DataModule.PlayerData)
    local ls = Instance.new("Folder")
    ls.Name = "leaderstats"
    ls.Parent = player

    local coins = Instance.new("IntValue")
    coins.Name = "Coins"
    coins.Value = data.Coins
    coins.Parent = ls

    local stage = Instance.new("IntValue")
    stage.Name = "Stage"
    stage.Value = data.Stage
    stage.Parent = ls
end

Players.PlayerAdded:Connect(function(player)
    local data = DataModule.load(player)
    setupLeaderstats(player, data)
    pushStats(player)

    player.CharacterAdded:Connect(function(character)
        local stage = data.Stage
        local spawnPart = workspace.Stages:FindFirstChild("Stage" .. stage)
        if spawnPart and spawnPart:FindFirstChild("Spawn") then
            local spawn = spawnPart.Spawn :: BasePart
            character:PivotTo(spawn.CFrame + Vector3.new(0, 3, 0))
        end
    end)
end)

game:BindToClose(function()
    for _, player in Players:GetPlayers() do
        DataModule.save(player)
        player:Kick("Сервер перезапускается. Прогресс сохранён.")
    end
    task.wait(3)
end)
