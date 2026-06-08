local function elevator_floor(floor_number)
    print("Лифт на этаже", floor_number)
    coroutine.yield("doors_close") -- Ждем команду закрыть двери
    print("Двери закрыты на этаже", floor_number)
    
    -- Переход в состояние движения
    coroutine.yield("move_up") -- Или move_down
    print("Лифт едет...")
    coroutine.yield("arrive") -- Ждем прибытия
    print("Лифт прибыл на этаж", floor_number)
    
    coroutine.yield("doors_open") -- Ждем команду открыть двери
    print("Двери открыты на этаже", floor_number)
end

local function controller()
    local co = coroutine.create(elevator_floor)
    
    -- Имитация запросов от пассажиров
    coroutine.resume(co, 1) -- Запрос на 1 этаж
    
    -- Симуляция событий системы
    coroutine.resume(co, "doors_close") -- Команда закрыть
    coroutine.resume(co, "move_up")     -- Команда ехать
    coroutine.resume(co, "arrive")      -- Прибытие
    coroutine.resume(co, "doors_open")  -- Открыть
end

controller()
