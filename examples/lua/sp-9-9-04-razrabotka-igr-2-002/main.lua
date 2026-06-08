-- 1. Создаём экземпляр
local part1 = Instance.new("Part")
part1.Name = "Cube"
part1.Parent = workspace  -- ← объект попадает в сцену

-- 2. Переменная — ссылка
local ref1 = part1
local ref2 = workspace.Cube

print(part1 == ref1)  -- true
print(part1 == ref2)  -- true (один и тот же экземпляр)

-- 3. Клонирование создаёт **новый экземпляр**
local part2 = part1:Clone()
part2.Parent = workspace
part2.Name = "Cube2"

print(part1 == part2) -- false (разные объекты в памяти)
