-- ModuleScript: Signal.lua
local Signal = {}
Signal.__index = Signal

function Signal.new()
    local self = setmetatable({
        _binds = {}
    }, Signal)
    return self
end

function Signal:Connect(callback: function)
    table.insert(self._binds, callback)
    return {
        Disconnect = function(this)
            for i, bind in ipairs(self._binds) do
                if bind == this then
                    table.remove(self._binds, i)
                    break
                end
            end
        end
    }
end

function Signal:Fire(...)
    for _, bind in ipairs(self._binds) do
        task.spawn(bind, ...)
    end
end

function Signal:DisconnectAll()
    self._binds = {}
end

return Signal
