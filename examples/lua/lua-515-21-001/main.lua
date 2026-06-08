local function generator()
    for i = 1, 5 do
        print("До паузы:", i)
        coroutine.yield(i * 10) -- Возвращаем значение наружу
        print("После паузы:", i) -- Выполнится только при следующем resume
    end
end

local co = coroutine.create(generator)

while true do
    local status, val = coroutine.resume(co)
    if not status then
        break
    end
    print("Получено значение от yield:", val)
    
    if val > 40 then
        break
    end
end
