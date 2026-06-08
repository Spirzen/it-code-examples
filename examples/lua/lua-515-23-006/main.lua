-- Services/PlayerService.luau
type PlayerData = { coins: number, level: number }

local PlayerService = {}
PlayerService.__index = PlayerService

function PlayerService.new()
    local self = setmetatable({
        _players = {} :: { [Player]: PlayerData },
    }, PlayerService)
    return self
end

function PlayerService:Init()
    game.Players.PlayerAdded:Connect(function(player)
        self._players[player] = { coins = 0, level = 1 }
        -- Загрузка из DataStore — отдельный сервис
    end)

    game.Players.PlayerRemoving:Connect(function(player)
        self._players[player] = nil
    end)
end

function PlayerService:GetCoins(player: Player): number
    local record = self._players[player]
    return record and record.coins or 0
end

function PlayerService:AddCoins(player: Player, amount: number)
    local record = self._players[player]
    if record then
        record.coins += amount
        -- Оповещение GUI через RemoteEvent или Signal
    end
end

return PlayerService
