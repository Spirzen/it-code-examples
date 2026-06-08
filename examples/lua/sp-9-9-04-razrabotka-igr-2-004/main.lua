-- LocalScript внутри StarterGui/ScreenGui/TextButton

local button = script.Parent
local enabled = true

local function onClick()
	if not enabled then return end

	-- Изменение свойства объекта GUI
	button.TextColor3 = Color3.new(1, 0, 0)

	-- Вызов удалённой функции (безопасно!)
	game.ReplicatedStorage.RemoteEvents.Action:FireServer("ButtonClick")
end

local connection = button.MouseButton1Click:Connect(onClick)

script.Destroying:Connect(function()
	enabled = false
	if connection then connection:Disconnect() end
end)
