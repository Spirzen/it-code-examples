local function fail(code, message)
    error({ code = code, message = message }, 2)
end

local function validate_input(value)
    if value == nil then
        fail(400, "missing input")
    elseif value < 0 then
        fail(401, "must be non-negative")
    end
    return "ok"
end

local ok, err = pcall(validate_input, nil)

if not ok and type(err) == "table" then
    print(err.code, err.message)
end
