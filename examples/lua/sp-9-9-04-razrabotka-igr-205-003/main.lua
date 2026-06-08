--!strict
-- LocalScript в Tool

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Debris = game:GetService("Debris")

local player = Players.LocalPlayer
local mouse = player:GetMouse()
local tool = script.Parent :: Tool
local handle = tool:WaitForChild("Handle") :: BasePart
local settings = require(tool:WaitForChild("Settings"))
local Hit = ReplicatedStorage.Remotes.Hit :: RemoteEvent
local Replicate = ReplicatedStorage.Remotes.Replicate :: RemoteEvent

local equipped = false
local firing = false

tool.Equipped:Connect(function()
    equipped = true
end)
tool.Unequipped:Connect(function()
    equipped = false
    firing = false
end)

local function castRay(): (Instance?, Vector3, Vector3, Vector3)
    local char = player.Character
    if not char then
        return nil, Vector3.zero, Vector3.zero, Vector3.zero
    end
    local origin = handle.Position
    local direction = (mouse.Hit.Position - origin).Unit * settings.range

    local params = RaycastParams.new()
    params.FilterType = Enum.RaycastFilterType.Exclude
    params.FilterDescendantsInstances = { char, workspace.Effects }

    local result = workspace:Raycast(origin, direction, params)
    local pos = if result then result.Position else origin + direction
    return result and result.Instance or nil, pos, direction, origin
end

local function drawTracer(origin: Vector3, pos: Vector3)
    Replicate:FireServer(tool, origin, pos)
end

local function tryFire()
    if not equipped or tool:FindFirstChild("Debounce") and (tool.Debounce :: BoolValue).Value then
        return
    end
    local waitTime = 60 / settings.rateOfFire
    local deb = tool:FindFirstChild("Debounce") :: BoolValue?
    if deb then deb.Value = true end
    task.delay(waitTime, function()
        if deb then deb.Value = false end
    end)

    local hit, pos, direction, origin = castRay()
    drawTracer(origin, pos)
    if hit then
        local relCFrame = hit.CFrame:ToObjectSpace(CFrame.new(pos))
        Hit:FireServer(tool, hit, direction, origin, relCFrame)
    end
end

mouse.Button1Down:Connect(function()
    firing = true
    if settings.fireMode == "SEMI" then
        tryFire()
    else
        task.spawn(function()
            while firing and equipped do
                tryFire()
                task.wait(60 / settings.rateOfFire)
            end
        end)
    end
end)

mouse.Button1Up:Connect(function()
    firing = false
end)
