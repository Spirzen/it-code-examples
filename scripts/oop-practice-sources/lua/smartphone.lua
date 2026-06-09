local Smartphone = {}

function Smartphone:new(model)
    local obj = setmetatable({model = model, _battery = 20}, {__index = self})
    return obj
end

function Smartphone:call()
    self._battery = math.max(0, self._battery - 5)
    print("Звонок с " .. self.model .. "... Заряд: " .. self._battery .. "%")
end

function Smartphone:charge()
    self._battery = math.min(100, self._battery + 30)
    print("Зарядка " .. self.model .. "... Заряд: " .. self._battery .. "%")
end

function Smartphone:show_status()
    print("Смартфон " .. self.model .. ": заряд " .. self._battery .. "%")
end

local phone = Smartphone:new("Pixel")
phone:show_status()
phone:call()
phone:charge()
phone:show_status()
