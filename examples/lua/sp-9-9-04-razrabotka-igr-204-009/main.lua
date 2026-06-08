--!strict
-- StageFinish.server.luau — подключите из GameMain или отдельным Script

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local DataModule = require(ReplicatedStorage.Modules.DataModule)
local StatsUpdated = ReplicatedStorage.Remotes.StatsUpdated :: RemoteEvent

local function hookFinish(finishPart: BasePart, stageIndex: number)
    finishPart.Touched:Connect(function(hit)
        local character = hit:FindFirstAncestorOfClass("Model")
        if not character then
            return
        end
        local player = Players:GetPlayerFromCharacter(character)
        if not player then
            return
        end
        DataModule.setStage(player, stageIndex + 1)
        DataModule.increment(player, "Wins", 1)
        DataModule.save(player)

        local ls = player:FindFirstChild("leaderstats")
        if ls then
            local stageVal = ls:FindFirstChild("Stage") :: IntValue?
            if stageVal then
                stageVal.Value = DataModule.get(player).Stage
            end
        end
        local data = DataModule.get(player)
        StatsUpdated:FireClient(player, data.Coins, data.Stage, data.Wins)
    end)
end

for _, stage in workspace.Stages:GetChildren() do
    local n = tonumber(stage.Name:match("%d+"))
    local finish = stage:FindFirstChild("Finish") :: BasePart?
    if n and finish then
        hookFinish(finish, n)
    end
end
