-- Test_MathUtils.lua
local TestService = game:GetService("TestService")
local Math = require(game.ReplicatedStorage.Utils.Math)

-- Тест 1: clamp
do
    local result = Math.clamp(15, 0, 10)
    if result ~= 10 then
        TestService:Fail(("clamp(15,0,10) = %d, expected 10"):format(result))
    end
end

-- Тест 2: производительность
do
    TestService:Start()
    for i = 1, 100000 do
        Math.clamp(i % 20, 5, 15)
    end
    local elapsed = TestService:Stop()
    if elapsed > 0.1 then
        TestService:Warn(("clamp 100k calls: %.3f sec (slow)"):format(elapsed))
    end
end

TestService:Check() -- все тесты пройдены
