-- ModuleScript: Logger.lua
local LogService = game:GetService("LogService")

local Logger = {}

function Logger.info(tag: string, ...)
    LogService:Message(("[INFO][%s] %s"):format(tag, table.concat({...}, " ")))
end

function Logger.warn(tag: string, ...)
    LogService:Warning(("[WARN][%s] %s"):format(tag, table.concat({...}, " ")))
end

function Logger.error(tag: string, ...)
    LogService:Error(("[ERROR][%s] %s"):format(tag, table.concat({...}, " ")))
end

-- Экспорт для внешнего анализа
function Logger.getHistory()
    return LogService:GetLogHistory()
end

return Logger
