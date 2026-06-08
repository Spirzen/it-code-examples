local Configuration = {}

function Configuration:new(key, value)
    local config = {key = key, value = value, locked = false}
    
    local public = setmetatable({}, {__index = self})
    
    function public:setNewValue(newValue)
        if self.locked then
            error("Конфигурация заблокирована")
        end
        self.value = newValue
    end
    
    function public:lock()
        self.locked = true
    end
    
    return public
end

local config = Configuration:new("theme", "dark")
config:setNewValue("light")
config:lock()
-- config:setNewValue("red") -- Ошибка: Конфигурация заблокирована
