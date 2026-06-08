function write_binary(filename, data)
    local file = io.open(filename, "wb")
    if not file then
        return false
    end
    
    file:write(data)
    file:close()
    return true
end

function read_binary(filename)
    local file = io.open(filename, "rb")
    if not file then
        return nil
    end
    
    local data = file:read("*all")
    file:close()
    return data
end

local binary_data = string.char(0x00, 0xFF, 0xAA)
write_binary("data.bin", binary_data)
local read_data = read_binary("data.bin")
print(read_data)
