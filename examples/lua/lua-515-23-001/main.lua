-- JumpEffectClient.luau
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

-- Подготавливаем шаблон эффекта (загружен заранее в ReplicatedStorage)
local jumpEffectTemplate = ReplicatedStorage:WaitForChild("JumpEffect"):Clone()

-- Событие для запроса эффекта у сервера
local requestJumpEffect = ReplicatedStorage:WaitForChild("RequestJumpEffect")

humanoid.StateChanged:Connect(function(oldState, newState)
    if newState == Enum.HumanoidStateType.Jumping then
        -- Отправляем запрос серверу — не создаём эффект напрямую!
        requestJumpEffect:FireServer()
    end
end)

-- Сервер отвечает через другой RemoteEvent
local playJumpEffect = ReplicatedStorage:WaitForChild("PlayJumpEffect")
playJumpEffect.OnClientEvent:Connect(function(position: Vector3)
    local effect = jumpEffectTemplate:Clone()
    effect.Position = position
    effect.Parent = workspace
    effect:Emit(10)
    task.delay(2, function() effect:Destroy() end)
end)
