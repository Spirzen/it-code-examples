local function my_msgh(err)
    return debug.traceback(tostring(err), 2)
end

local function risky_op()
    error("critical failure")
end

local ok, err = xpcall(risky_op, my_msgh)

if ok then
    print("OK")
else
    print("Caught:", err)  -- строка с traceback
end
