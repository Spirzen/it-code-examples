local Config = {
    name = "Default",
    version = 1.0,
    settings = {debug = false}
}

function Module:new(config)
    local instance = setmetatable({}, {__index = self})
    for key, value in pairs(config or {}) do
        instance[key] = value
    end
    return instance
end

local mod = Module:new({name = "Custom", debug = true})
print(mod.name) -- Custom
print(mod.debug) -- true
