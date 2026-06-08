-- ModuleScript: Signal.luau
export type Connection = { Disconnect: () -> () }
export type Signal<T...> = {
    Connect: (self: Signal<T...>, callback: (T...) -> ()) -> Connection,
    Fire: (self: Signal<T...>, T...) -> (),
    Once: (self: Signal<T...>, callback: (T...) -> ()) -> Connection,
}

type SignalImpl<T...> = {
    _callbacks: { (T...) -> () },
    _onceCallbacks: { (T...) -> () },
}

local Signal = {}
Signal.__index = Signal

function Signal.new<T...>(): Signal<T...>
    return setmetatable({
        _callbacks = {},
        _onceCallbacks = {},
    } :: SignalImpl<T...>, Signal)
end

function Signal:Connect<T...>(callback: (T...) -> ()): Connection
    table.insert(self._callbacks, callback)
    return {
        Disconnect = function()
            local index = table.find(self._callbacks, callback)
            if index then table.remove(self._callbacks, index) end
        end
    }
end

function Signal:Once<T...>(callback: (T...) -> ()): Connection
    table.insert(self._onceCallbacks, callback)
    return {
        Disconnect = function()
            local index = table.find(self._onceCallbacks, callback)
            if index then table.remove(self._onceCallbacks, index) end
        end
    }
end

function Signal:Fire<T...>(...: T...)
    for _, cb in self._callbacks do
        task.spawn(cb, ...)  -- асинхронный вызов во избежание блокировки
    end
    for _, cb in self._onceCallbacks do
        task.spawn(cb, ...)
    end
    self._onceCallbacks = {}
end

return Signal
