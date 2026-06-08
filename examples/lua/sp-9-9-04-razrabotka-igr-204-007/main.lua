--!strict
local PhysicsService = game:GetService("PhysicsService")
local Players = game:GetService("Players")

local GROUP = "ObbyPlayers"

PhysicsService:RegisterCollisionGroup(GROUP)
PhysicsService:CollisionGroupSetCollidable(GROUP, GROUP, false)

Players.PlayerAdded:Connect(function(player)
    player.CharacterAdded:Connect(function(char)
        for _, desc in char:GetDescendants() do
            if desc:IsA("BasePart") then
                desc.CollisionGroup = GROUP
            end
        end
    end)
end)
