local function level_3()
    error("error at level 3")
end

local function level_2()
    level_3()
end

local function level_1()
    local ok, err = pcall(level_2)
    if not ok then
        print(debug.traceback("Trace:", 2))
        print(err)
    end
end

level_1()
