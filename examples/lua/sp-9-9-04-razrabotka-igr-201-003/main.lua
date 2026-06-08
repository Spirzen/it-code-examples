local function safeSetAsync(ds, key, value, maxRetries)
    maxRetries = maxRetries or 5
    local delay = 1

    for i = 1, maxRetries do
        local success, err = pcall(function()
            return ds:SetAsync(key, value)
        end)

        if success then return true end

        if not err:find("429") and not err:find("500") then
            warn("Non-retryable error:", err)
            return false
        end

        task.wait(delay)
        delay = math.min(delay * 2, 60) -- max 60 sec
    end
    return false
end
