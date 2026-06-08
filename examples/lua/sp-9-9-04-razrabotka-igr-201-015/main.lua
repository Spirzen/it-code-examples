-- Server
local HttpService = game:GetService("HttpService")

local function sendWebhook(playerName, action)
    local payload = HttpService:JSONEncode({
        content = ("**%s** %s"):format(playerName, action),
        username = "Game Logger"
    })

    spawn(function()
        local success, response = pcall(function()
            return HttpService:PostAsync(
                "https://discord.com/api/webhooks/...",
                payload,
                Enum.HttpContentType.ApplicationJson
            )
        end)
        if not success then
            warn("Webhook failed:", response)
        end
    end)
end

Players.PlayerAdded:Connect(function(player)
    sendWebhook(player.Name, "присоединился к серверу")
end)
