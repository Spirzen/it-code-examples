local CURRENT_VERSION = 2

local function migrate(Данные)
    if not Данные then return { version = CURRENT_VERSION, gold = 0 } end
    if data.version == 1 then
        -- v1 → v2: gold → resources.gold
        data.resources = { gold = data.gold }
        data.gold = nil
        data.version = 2
    end
    return Данные
end

-- При загрузке:
local rawData = DS:GetAsync(key)
local data = migrate(rawData)
