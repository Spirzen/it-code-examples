local Calculator = {}

function Calculator:new()
    local calc = setmetatable({}, {__index = self})
    return calc
end

function Calculator:calculate(a, b)
    if type(a) == "number" and type(b) == "number" then
        return a + b
    elseif type(a) == "string" and type(b) == "string" then
        return a .. b
    else
        error("Неподдерживаемые типы аргументов")
    end
end

local calc = Calculator:new()
print(calc:calculate(5, 10)) -- 15
print(calc:calculate("Hello", " World")) -- Hello World
