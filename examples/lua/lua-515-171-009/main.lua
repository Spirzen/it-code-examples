local Prototype = {}

function Prototype:new(baseObject)
    local newObj = {}
    for k, v in pairs(baseObject) do
        newObj[k] = v
    end
    setmetatable(newObj, {__index = self})
    return newObj
end

local template = {color = "blue", size = "L"}
local newItem = Prototype:new(template)
print(newItem.color) -- blue
