local function hookKillPart(part: BasePart)
    part.Touched:Connect(function(hit)
        local player, char = playerFromHit(hit)
        local hum = char and char:FindFirstChildOfClass("Humanoid")
        if player and hum and hum.Health > 0 then
            hum.Health = 0
        end
    end)
end

local function hookDamagePart(part: BasePart)
    local damageVal = part:FindFirstChild("Damage") :: IntValue?
    if not damageVal then return end
    local debouncing = false
    part.Touched:Connect(function(hit)
        local player, char = playerFromHit(hit)
        local hum = char and char:FindFirstChildOfClass("Humanoid")
        if player and hum and not debouncing then
            debouncing = true
            hum:TakeDamage(damageVal.Value)
            task.delay(0.1, function()
                debouncing = false
            end)
        end
    end)
end
