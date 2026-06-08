--!strict

local part = script.Parent :: BasePart

local function onTouched(other: BasePart)
    local character = other.Parent
    if not character then
        return
    end

    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        humanoid.Health = 0
    end
end

part.Touched:Connect(onTouched)
