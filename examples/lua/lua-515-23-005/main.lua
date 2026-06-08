-- init.luau
local Services = {}

-- Ленивая инициализация
function Services.GetService<T>(name: string): T
    if not rawget(Services, name) then
        local module = require(script.Parent.Services[name])
        Services[name] = module.new()
        if Services[name].Init then Services[name]:Init() end
    end
    return Services[name] :: T
end

-- Экспорт в глобальную область (только для внутреннего использования)
_G.Services = Services

-- Запуск
Services.GetService("PlayerService")
