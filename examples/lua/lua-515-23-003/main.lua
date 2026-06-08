-- ServerScriptService/CoinManager.luau
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ServerStorage = game:GetService("ServerStorage")

local COIN_TEMPLATE = ReplicatedStorage:WaitForChild("CoinTemplate")
local COIN_SPAWN_POINTS = ServerStorage:WaitForChild("CoinSpawns")  -- Folder с Part'ами

local coinCount = 0
local coins = {}

local function spawnCoin(at: Vector3)
    local coin = COIN_TEMPLATE:Clone()
    coin.Position = at
    coin.Anchored = true
    coin.Parent = workspace

    local touchedConn
    touchedConn = coin.Touched:Connect(function(hit)
        local character = hit:FindFirstAncestorOfClass("Model")
        if not character then return end

        local player = game.Players:GetPlayerFromCharacter(character)
        if not player then return end

        -- Валидация: не слишком ли часто?
        if os.clock() - (coins[coin] or 0) < 0.5 then return end

        coinCount += 1
        coins[coin] = os.clock()
        touchedConn:Disconnect()
        coin:Destroy()

        -- Уведомляем клиента
        game.ReplicatedStorage.CoinCollected:FireClient(player, coinCount)
    end)

    coins[coin] = 0
end

-- Спавним по точкам
for _, point in COIN_SPAWN_POINTS:GetChildren() do
    if point:IsA("BasePart") then
        spawnCoin(point.Position)
    end
end
