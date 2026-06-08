local Counter = {}

function Counter:new(startValue)
    local count = startValue or 0
    
    local publicMethods = setmetatable({}, {__index = self})
    
    function publicMethods:increment()
        count = count + 1
    end
    
    function publicMethods:decrement()
        count = count - 1
    end
    
    function publicMethods:getCount()
        return count
    end
    
    return publicMethods
end

local counter = Counter:new(10)
counter:increment()
counter:increment()
print(counter:getCount()) -- 12
-- Прямое изменение count невозможно
