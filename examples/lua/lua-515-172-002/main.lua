function parse_csv(filename)
    local file = io.open(filename, "r")
    if not file then
        return nil, "Не удалось открыть файл"
    end
    
    local rows = {}
    for line in file:lines() do
        local row = {}
        for field in string.gmatch(line, "[^,]+") do
            table.insert(row, field)
        end
        table.insert(rows, row)
    end
    
    file:close()
    return rows
end

local data, err = parse_csv("users.csv")
if data then
    for _, user in ipairs(data) do
        print(user[1], user[2])
    end
else
    print(err)
end
