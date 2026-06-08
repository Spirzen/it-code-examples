local function wait(seconds)
    local start_time = os.time()
    while os.time() < start_time + seconds do
        coroutine.yield() -- Передаем управление внешнему циклу
    end
end

local function move_to_door()
    print("Персонаж идет к двери...")
    wait(2) -- Имитация движения
    print("Персонаж у двери.")
end

local function open_door()
    print("Открываем дверь...")
    wait(1) -- Имитация открытия
    print("Дверь открыта.")
end

local function enter_room()
    print("Персонаж входит в комнату.")
    wait(1)
    print("Персонаж в комнате.")
end

local function game_sequence()
    move_to_door()
    open_door()
    enter_room()
end

local co = coroutine.create(game_sequence)

-- Внешний цикл управления временем
local function game_loop()
    while true do
        local status, err = coroutine.resume(co)
        if not status then
            print("Ошибка в последовательности:", err)
            break
        end
        -- Здесь можно обновлять графику или проверять другие задачи
        collectgarbage("step", 1) -- Освобождение памяти
    end
end

game_loop()
