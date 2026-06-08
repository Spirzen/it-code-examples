-- ModuleScript: Promise.luau
export type Promise<T> = {
    andThen: <U>(self: Promise<T>, (T) -> U | Promise<U>) -> Promise<U>,
    catch: (self: Promise<T>, (string) -> T) -> Promise<T>,
    await: (self: Promise<T>) -> T,
}

local Promise = {}
Promise.__index = Promise

function Promise.new<T>(executor: (resolve: (T) -> (), reject: (string) -> ()) -> ())
    local self = setmetatable({
        _state = "pending" :: "pending" | "fulfilled" | "rejected",
        _value = nil :: T?,
        _reason = nil :: string?,
        _onFulfilled = {} :: { (T) -> () },
        _onRejected = {} :: { (string) -> () },
    }, Promise)

    local function resolve(value: T)
        if self._state ~= "pending" then return end
        self._state = "fulfilled"
        self._value = value
        for _, cb in self._onFulfilled do task.spawn(cb, value) end
    end

    local function reject(reason: string)
        if self._state ~= "pending" then return end
        self._state = "rejected"
        self._reason = reason
        for _, cb in self._onRejected do task.spawn(cb, reason) end
    end

    task.spawn(executor, resolve, reject)
    return self
end

-- Реализация andThen, catch, await — опущена для краткости, но доступна в open-source библиотеках (например, NevermoreEngine)

-- Использование:
local p = Promise.new(function(resolve, reject)
    task.delay(1, function()
        resolve("done")
    end)
end)

p:andThen(function(result)
    print(result)  -- "done"
    return result .. " and processed"
end):andThen(print)  -- "done and processed"
