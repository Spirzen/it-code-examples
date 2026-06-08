local FileFactory = {}

function FileFactory.create(filename, mode)
    local file, err = io.open(filename, mode)
    if not file then
        error("Ошибка открытия файла: " .. err)
    end
    return setmetatable({
        _file = file,
        _filename = filename,
        _mode = mode
    }, {
        __index = {
            read = function(self) return self._file:read() end,
            write = function(self, chunk) self._file:write(chunk) end,
            close = function(self) self._file:close() end
        }
    })
end

local f = FileFactory.create("test.txt", "w")
f:write("Тест")
f:close()
