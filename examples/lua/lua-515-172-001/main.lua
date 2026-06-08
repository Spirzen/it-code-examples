function split(str, sep)
    local parts = {}
    local start = 1
    local sepLen = #sep
    while true do
        local pos = string.find(str, sep, start, true)
        if not pos then break end
        table.insert(parts, string.sub(str, start, pos - 1))
        start = pos + sepLen
    end
    table.insert(parts, string.sub(str, start))
    return parts
end

local data = "apple,banana,cherry"
local fruits = split(data, ",")
for _, fruit in ipairs(fruits) do
    print(fruit)
end
