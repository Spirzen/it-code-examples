-- JumpEffectServer.luau
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local requestJumpEffect = Instance.new("RemoteEvent")
requestJumpEffect.Name = "RequestJumpEffect"
requestJumpEffect.Parent = ReplicatedStorage

local playJumpEffect = Instance.new("RemoteEvent")
playJumpEffect.Name = "PlayJumpEffect"
playJumpEffect.Parent = ReplicatedStorage

requestJumpEffect.OnServerEvent:Connect(function(player: Player)
    -- Валидация: жив ли персонаж? Делал ли он прыжок легально?
    local character = player.Character
    if not character then return end

    local humanoid = character:FindFirstChild("Humanoid")
    if not humanoid or humanoid:GetState() ~= Enum.HumanoidStateType.Jumping then
        warn(player.Name .. " attempted invalid jump effect")
        return
    end

    -- Определяем позицию: обычно — под центром масс
    local rootPart = character:FindFirstChild("HumanoidRootPart")
    if not rootPart then return end

    local position = rootPart.Position - Vector3.new(0, 2, 0)  -- чуть ниже ног
    playJumpEffect:FireClient(player, position)  -- только этому игроку
end)
