--!strict

local ServerStorage = game:GetService("ServerStorage")
local template = ServerStorage:WaitForChild("FallingCube") :: BasePart

while true do
    local clone = template:Clone()
    clone.Position = Vector3.new(math.random(-20, 20), 30, math.random(-20, 20))
    clone.Parent = workspace
    task.delay(5, function()
        clone:Destroy()
    end)
    task.wait(2)
end
