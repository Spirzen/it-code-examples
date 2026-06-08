--!strict
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local RoundStatus = ReplicatedStorage.Remotes.RoundStatus :: RemoteEvent

local MIN_PLAYERS = 2
local INTERMISSION = 15
local ROUND_TIME = 300

local GameRunner = {}
local competitors: { Player } = {}

local function broadcast(phase: string, seconds: number?)
    RoundStatus:FireAllClients(phase, seconds or 0)
end

local function fillCompetitors()
    table.clear(competitors)
    for _, p in Players:GetPlayers() do
        table.insert(competitors, p)
    end
end

function GameRunner.gameLoop()
    while true do
        broadcast("Waiting", 0)
        repeat
            task.wait(1)
        until #Players:GetPlayers() >= MIN_PLAYERS

        for t = INTERMISSION, 1, -1 do
            broadcast("Intermission", t)
            task.wait(1)
        end

        fillCompetitors()
        for _, p in competitors do
            p:LoadCharacter()
        end
        broadcast("Combat", ROUND_TIME)

        local deadline = os.clock() + ROUND_TIME
        while os.clock() < deadline do
            local alive = 0
            local winner: Player? = nil
            for _, p in competitors do
                local hum = p.Character and p.Character:FindFirstChildOfClass("Humanoid")
                if hum and hum.Health > 0 then
                    alive += 1
                    winner = p
                end
            end
            if alive <= 1 then
                if winner then
                    broadcast("Winner", 0)
                end
                break
            end
            task.wait(0.5)
        end

        task.wait(8)
    end
end

return GameRunner
