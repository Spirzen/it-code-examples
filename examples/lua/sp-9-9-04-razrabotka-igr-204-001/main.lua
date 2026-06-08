--!strict

local DataStoreService = game:GetService("DataStoreService")
local Players = game:GetService("Players")

local STORE = DataStoreService:GetDataStore("ObbyPlayerData_v1")

export type PlayerData = {
    Coins: number,
    Stage: number,
    Wins: number,
}

local DEFAULT: PlayerData = {
    Coins = 0,
    Stage = 1,
    Wins = 0,
}

local DataModule = {}
local session: { [Player]: PlayerData } = {}
local saveCooldown: { [Player]: number } = {}

local SAVE_INTERVAL = 60

local function key(player: Player): string
    return "u_" .. player.UserId
end

function DataModule.get(player: Player): PlayerData
    return session[player] or table.clone(DEFAULT)
end

function DataModule.load(player: Player): PlayerData
    local data = table.clone(DEFAULT)
    local ok, result = pcall(function()
        return STORE:GetAsync(key(player))
    end)
    if ok and type(result) == "table" then
        for k, v in pairs(DEFAULT) do
            if type(result[k]) == typeof(v) then
                data[k] = result[k]
            end
        end
    end
    session[player] = data
    return data
end

function DataModule.save(player: Player): boolean
    local data = session[player]
    if not data then
        return false
    end
    local now = os.clock()
    if saveCooldown[player] and now - saveCooldown[player] < 2 then
        return false
    end
    saveCooldown[player] = now
    local ok = pcall(function()
        STORE:SetAsync(key(player), data)
    end)
    return ok
end

function DataModule.increment(player: Player, field: "Coins" | "Stage" | "Wins", amount: number)
    local data = session[player]
    if not data then
        return
    end
    local current = data[field]
    if type(current) == "number" then
        data[field] = current + amount
    end
end

function DataModule.setStage(player: Player, stage: number)
    local data = session[player]
    if not data then
        return
    end
    if stage > data.Stage then
        data.Stage = stage
    end
end

Players.PlayerRemoving:Connect(function(player)
    DataModule.save(player)
    session[player] = nil
end)

task.spawn(function()
    while true do
        task.wait(SAVE_INTERVAL)
        for _, player in Players:GetPlayers() do
            DataModule.save(player)
        end
    end
end)

return DataModule
