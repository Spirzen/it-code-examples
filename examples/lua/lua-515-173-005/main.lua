local ops = {
    function() error("op 1 failed") end,
    function() return "op 2 ok" end,
    function() error("op 3 failed") end,
}

for i = 1, #ops do
    local ok, result = pcall(ops[i])
    if ok then
        print("Op", i, "ok:", result)
    else
        print("Op", i, "err:", result)
    end
end
