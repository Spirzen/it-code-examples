local Signal = require(ReplicatedStorage.Signal)

local PlayerDied = Signal.new()

-- Где-то в Humanoid:
PlayerDied:Fire(player, damageSource)

-- Где-то в UI:
local conn = PlayerDied:Connect(function(player, source)
    if player == game.Players.LocalPlayer then
        screenGui.DeathScreen.Visible = true
    end
end)

-- При уничтожении экрана:
conn:Disconnect()
