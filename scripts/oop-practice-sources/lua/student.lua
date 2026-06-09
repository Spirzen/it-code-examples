local Student = {PASSING_SCORE = 60}

function Student:new(name)
    local obj = setmetatable({name = name, grades = {}}, {__index = self})
    return obj
end

function Student:add_grade(grade)
    table.insert(self.grades, grade)
    print("Оценка " .. grade .. " добавлена для " .. self.name)
end

function Student:average_score()
    if #self.grades == 0 then
        return 0
    end
    local sum = 0
    for _, g in ipairs(self.grades) do
        sum = sum + g
    end
    return sum / #self.grades
end

function Student:is_passing()
    return self:average_score() >= self.PASSING_SCORE
end

function Student:info()
    local avg = self:average_score()
    print("Студент: " .. self.name)
    print("Оценки: " .. table.concat(self.grades, ", "))
    print(string.format("Средний балл: %.1f", avg))
    if self:is_passing() then
        print("Зачёт получен")
    else
        print("Зачёт не получен")
    end
end

local student = Student:new("Анна")
student:add_grade(70)
student:add_grade(85)
student:add_grade(55)
student:info()
