local Student = {}

function Student:new(name)
    local state = {
        name = name,
        grades = {},
        lastModified = os.date()
    }
    
    local interface = setmetatable({}, {__index = self})
    
    function interface:addGrade(grade)
        if grade >= 0 and grade <= 100 then
            table.insert(state.grades, grade)
            state.lastModified = os.date()
        end
    end
    
    function interface:getAverage()
        local sum = 0
        for _, g in ipairs(state.grades) do
            sum = sum + g
        end
        return #state.grades > 0 and sum / #state.grades or 0
    end
    
    return interface
end

local student = Student:new("Анна")
student:addGrade(90)
student:addGrade(85)
student:addGrade(95)
print(student:getAverage()) -- 90
