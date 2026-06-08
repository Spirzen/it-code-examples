local function read_file(path)
    local file, open_err = io.open(path, "r")
    if not file then
        error("cannot open file: " .. open_err)
    end
    local content = file:read("*all")
    file:close()
    return content
end

local ok, data = pcall(read_file, "nonexistent.txt")
if not ok then
    print("Read failed:", data)
end
