--!strict

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local event = ReplicatedStorage:WaitForChild("AddCoinRequest") :: RemoteEvent

local COOLDOWN = 1
local lastPress: { [Player]: number } = {}

event.OnServerEvent:Connect(function(player: Player)
    local now = os.clock()
    local prev = lastPress[player] or 0
    if now - prev < COOLDOWN then
        return
    end
    lastPress[player] = now

    local leaderstats = player:FindFirstChild("leaderstats")
    local coins = leaderstats and leaderstats:FindFirstChild("Coins") :: IntValue?
    if coins then
        coins.Value += 1
        print(player.Name, "получил монету. Всего:", coins.Value)
    end
end)
