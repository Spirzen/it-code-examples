-- Server
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local GAME_PASS_ID = 12345678

Players.PlayerAdded:Connect(function(player)
    local success, owns = pcall(function()
        return MarketplaceService:PlayerOwnsGamePassAsync(player.UserId, GAME_PASS_ID)
    end)

    if success and owns then
        player:SetAttribute("HasVIP", true)
        -- Открыть VIP-меню, выдать бонус и т.п.
    end
end)
