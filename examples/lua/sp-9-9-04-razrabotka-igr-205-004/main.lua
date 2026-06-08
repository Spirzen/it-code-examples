--!strict
local Players = game:GetService("Players")
local Weapons = {}

local function angleBetween(a: Vector3, b: Vector3): number
    local cos = math.clamp(a.Unit:Dot(b.Unit), -1, 1)
    return math.acos(cos)
end

function Weapons.verifyHit(
    shooter: Player,
    tool: Tool,
    claimedHit: Instance,
    direction: Vector3,
    origin: Vector3,
    relCFrame: CFrame,
    settings: any
): boolean
    local char = shooter.Character
    if not char or not tool:IsDescendantOf(char) then
        return false
    end
    if direction.Magnitude < 0.01 then
        return false
    end
    if (origin - char:GetPivot().Position).Magnitude > 12 then
        return false
    end
    local toTarget = (claimedHit.Position - origin).Unit
    if angleBetween(direction.Unit, toTarget) > math.rad(8) then
        return false
    end
    local recomposed = claimedHit.CFrame:ToWorldSpace(relCFrame).Position
    if (recomposed - claimedHit.Position).Magnitude > 2 then
        return false
    end
    if (origin - claimedHit.Position).Magnitude > settings.range + 10 then
        return false
    end
    return true
end

function Weapons.applyDamage(shooter: Player, hit: Instance, settings: any)
    local model = hit:FindFirstAncestorOfClass("Model")
    if not model then return end
    local victim = Players:GetPlayerFromCharacter(model)
    if not victim or victim == shooter then return end
    local hum = model:FindFirstChildOfClass("Humanoid")
    if not hum or hum.Health <= 0 then return end
    local dmg = settings.damage
    if hit.Name == "Head" then
        dmg *= settings.headshotMultiplier
    end
    hum:TakeDamage(dmg)
    -- increment Kills in Data if hum died
end

return Weapons
