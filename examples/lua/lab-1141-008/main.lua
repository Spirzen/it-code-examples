--!strict

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local UserInputService = game:GetService("UserInputService")
local event = ReplicatedStorage:WaitForChild("AddCoinRequest") :: RemoteEvent

UserInputService.InputBegan:Connect(function(input, processed)
    if processed then
        return
    end
    if input.KeyCode == Enum.KeyCode.E then
        event:FireServer()
    end
end)
