--!strict

local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")

local player = Players.LocalPlayer
local NORMAL = 16
local SPRINT = 28

local function getHumanoid(): Humanoid?
    local character = player.Character
    if not character then
        return nil
    end
    return character:FindFirstChildOfClass("Humanoid")
end

UserInputService.InputBegan:Connect(function(input, processed)
    if processed then
        return
    end
    if input.KeyCode == Enum.KeyCode.LeftShift then
        local hum = getHumanoid()
        if hum then
            hum.WalkSpeed = SPRINT
        end
    end
end)

UserInputService.InputEnded:Connect(function(input, _processed)
    if input.KeyCode == Enum.KeyCode.LeftShift then
        local hum = getHumanoid()
        if hum then
            hum.WalkSpeed = NORMAL
        end
    end
end)

player.CharacterAdded:Connect(function()
    local hum = getHumanoid()
    if hum then
        hum.WalkSpeed = NORMAL
    end
end)
