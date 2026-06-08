local mt = {
    __tostring = function(t)
        if t.value == nil then
            error("value is nil")
        end
        return tostring(t.value)
    end
}

local obj = setmetatable({ value = nil }, mt)

local ok, str = pcall(function() return tostring(obj) end)

if not ok then
    print("Metatable error:", str)
end
