-- ServerScript (в ServerScriptService)
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local ToolUse = ReplicatedStorage.Remotes.ToolUse

local COOLDOWN = 0.5
local playerLastUse = {}

ToolUse.OnServerEvent:Connect(function(player, targetPos)
    -- 1. Валидация игрока
    if not player or not player.Character then return end
    local humanoid = player.Character:FindFirstChild("Humanoid")
    if not humanoid or humanoid.Health <= 0 then return end

    -- 2. Античит: проверка расстояния
    local root = player.Character:FindFirstChild("HumanoidRootPart")
    if not root then return end
    local distance = (root.Position - targetPos).Magnitude
    if distance > 300 then return end -- слишком далеко

    -- 3. Анти-спам: cooldown
    local now = tick()
    if playerLastUse[player] and (now - playerLastUse[player]) < COOLDOWN then
        return
    end
    playerLastUse[player] = now

    -- 4. Выполнение действия (на сервере!)
    -- spawn bullet, apply damage, etc.
end)
