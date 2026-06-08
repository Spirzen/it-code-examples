-- Plugin.lua
local Plugin = script:FindFirstAncestorWhichIsA("Plugin")
local Selection = game:GetService("Selection")

local button = Plugin:CreateToolbar("Tools"):CreateButton(
    "FixPart",
    "Привести Part к стандарту",
    "rbxassetid://123456789"
)

button.Click:Connect(function()
    for _, obj in ipairs(Selection:Get()) do
        if obj:IsA("BasePart") then
            obj.Material = Enum.Material.Plastic
            obj.BrickColor = BrickColor.new("Bright blue")
            obj.Anchored = true
            obj.CanCollide = true
        end
    end
end)
