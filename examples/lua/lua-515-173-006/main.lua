local function safe_call(fn, ...)
    local ok, result = pcall(fn, ...)
    if ok then
        return true, result
    end
    print("Error:", tostring(result))
    return false, result
end

local function risky_op(x)
    if x < 0 then
        error("negative value")
    end
    return x * 2
end

local ok, result = safe_call(risky_op, -5)
