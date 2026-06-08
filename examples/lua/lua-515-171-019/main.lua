local Button = {}

function Button:new(label)
    local button = setmetatable({}, {__index = self})
    button.label = label
    button.action = function() print("Нажата кнопка: " .. label) end
    return button
end

function Button:setAction(fn)
    self.action = fn
end

local btn1 = Button:new("OK")
local btn2 = Button:new("Cancel")

btn2:setAction(function() print("Отмена действия") end)

btn1.action() -- Нажата кнопка: OK
btn2.action() -- Отмена действия
