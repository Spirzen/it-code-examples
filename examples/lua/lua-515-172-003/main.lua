function save_config(filename, config)
    local file = io.open(filename, "w")
    if not file then
        return false
    end
    
    for key, value in pairs(config) do
        file:write(key, "=", tostring(value), "\n")
    end
    
    file:close()
    return true
end

function load_config(filename)
    local config = {}
    local file = io.open(filename, "r")
    if not file then
        return nil
    end
    
    for line in file:lines() do
        local key, value = string.match(line, "(%w+)=(.*)")
        if key and value then
            config[key] = tonumber(value) or value
        end
    end
    
    file:close()
    return config
end

local settings = {
    width = 800,
    height = 600,
    fullscreen = true
}

save_config("settings.cfg", settings)
local loaded = load_config("settings.cfg")
print(loaded.width, loaded.fullscreen)
