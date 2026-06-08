--!strict
-- LocalScript в StarterPlayerScripts

local RunService = game:GetService("RunService")
local folder = workspace:WaitForChild("Spinners")

RunService.RenderStepped:Connect(function(dt)
    for _, part in folder:GetChildren() do
        if part:IsA("BasePart") then
            local speed = part:GetAttribute("SpinSpeed") or 1
            part.CFrame = part.CFrame * CFrame.Angles(0, math.rad(speed) * dt, 0)
        end
    end
end)
