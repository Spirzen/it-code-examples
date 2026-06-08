local MAX_RETRIES = 5

function DataModule.save(player: Player): boolean
    local data = session[player]
    if not data then return false end
    for attempt = 1, MAX_RETRIES do
        local ok, err = pcall(function()
            STORE:SetAsync(key(player), deepCopy(data))
        end)
        if ok then return true end
        warn("DataStore save retry", attempt, err)
        task.wait(1 + attempt * 0.5)
    end
    return false
end
