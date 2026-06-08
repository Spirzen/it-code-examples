function map(t, fn)
    local result = {}
    for k, v in pairs(t) do
        result[k] = fn(v)
    end
    return result
end

function filter(t, pred)
    local result = {}
    for k, v in pairs(t) do
        if pred(v) then
            table.insert(result, v)
        end
    end
    return result
end
