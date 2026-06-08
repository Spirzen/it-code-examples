local function hookSpawnPart(part: BasePart)
    local stageVal = part:FindFirstChild("Stage") :: IntValue?
    if not stageVal then return end
    local targetStage = stageVal.Value
    part.Touched:Connect(function(hit)
        local player = playerFromHit(hit)
        if not player then return end
        local current = DataModule.get(player).Stage
        if current == targetStage - 1 then
            DataModule.setStage(player, targetStage)
            DataModule.save(player)
            -- FireClient StatsUpdated …
        end
    end)
end
