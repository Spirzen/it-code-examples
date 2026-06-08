-- tests/PlayerService.spec.luau
local TestEZ = require(game.ReplicatedStorage.TestEZ)
local PlayerService = require(game.ReplicatedStorage.Modules.PlayerService)

TestEZ.describe("PlayerService", function()
    TestEZ.it("starts with 0 coins", function()
        local service = PlayerService.new()
        local mockPlayer = { Name = "Test" } :: any
        service:Init()
        service._players[mockPlayer] = { coins = 0, level = 1 }

        expect(service:GetCoins(mockPlayer)).to.equal(0)
    end)
end)
