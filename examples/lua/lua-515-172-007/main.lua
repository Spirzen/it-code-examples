local Logger = {}

function Logger.init(level, file)
    local log_file = io.open(file, "a")
    Logger.level = level
    Logger.file = log_file
end

function Logger.log(level, message)
    if level >= Logger.level then
        local timestamp = os.date("%Y-%m-%d %H:%M:%S")
        Logger.file:write(string.format("[%s] [%s] %s\n", timestamp, level, message))
    end
end

Logger.init(1, "app.log")
Logger.log(1, "Информационное сообщение")
Logger.log(2, "Предупреждение")
