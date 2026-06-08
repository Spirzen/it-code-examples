local ConfigCache = {}

function ConfigCache.load(filename)
    if ConfigCache.Data then
        return ConfigCache.Data
    end
    
    local file = io.open(filename, "r")
    if not file then
        return {}
    end
    
    local config = {}
    for line in file:lines() do
        local key, value = string.match(line, "(%w+)=(.*)")
        if key then
            config[key] = tonumber(value) or value
        end
    end
    
    file:close()
    ConfigCache.Data = config
    return config
end

local cfg = ConfigCache.load("config.txt")
