--!strict

local pad = script.Parent :: BasePart
local BOOST = 80

local function onTouched(other: BasePart)
    local character = other.Parent
    if not character then
        return
    end
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        humanoid.JumpPower = BOOST
        humanoid:ChangeState(Enum.HumanoidStateType.Jumping)
    end
end

pad.Touched:Connect(onTouched)
