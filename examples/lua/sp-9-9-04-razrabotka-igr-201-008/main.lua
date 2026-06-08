-- ModuleScript: Janitor.lua
local Janitor = {}
Janitor.__index = Janitor

function Janitor.new()
    return setmetatable({ _tasks = {} }, Janitor)
end

function Janitor:Add(task: any, key: string?)
    if typeof(task) == "RBXScriptConnection" then
        if key then
            self._tasks[key] = task
        else
            table.insert(self._tasks, task)
        end
        return task
    elseif type(task) == "function" then
        local conn
        conn = game:GetService("RunService").Heartbeat:Connect(function()
            conn:Disconnect()
            task()
        end)
        if key then
            self._tasks[key] = conn
        else
            table.insert(self._tasks, conn)
        end
        return conn
    elseif typeof(task) == "Instance" then
        table.insert(self._tasks, function() task:Destroy() end)
        return task
    else
        error("Unsupported task type")
    end
end

function Janitor:Cleanup()
    for _, task in ipairs(self._tasks) do
        if typeof(task) == "RBXScriptConnection" then
            task:Disconnect()
        elseif type(task) == "function" then
            task()
        end
    end
    for key in pairs(self._tasks) do
        self._tasks[key] = nil
    end
end

return Janitor
