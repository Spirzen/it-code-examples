local DatabaseConnection = {}

function DatabaseConnection:new(host, port)
    local conn = setmetatable({}, {__index = self})
    conn.host = host
    conn.port = port
    conn.isConnected = false
    conn:connect() -- Автоматическое подключение при создании
    return conn
end

function DatabaseConnection:connect()
    -- Имитация подключения
    self.isConnected = true
    print("Подключение к " .. self.host .. ":" .. self.port)
end

local db = DatabaseConnection:new("localhost", 3306)
