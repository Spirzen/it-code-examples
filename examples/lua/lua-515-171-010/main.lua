local FileHandler = {}

function FileHandler:new(filename, mode)
    local handler = setmetatable({}, {__index = self})
    handler.filename = filename
    handler.file = io.open(filename, mode)
    if not handler.file then
        error("Не удалось открыть файл")
    end
    return handler
end

function FileHandler:close()
    if self.file then
        self.file:close()
        self.file = nil
    end
end

-- Использование
local f = FileHandler:new("test.txt", "w")
f:write("Hello")
f:close()
