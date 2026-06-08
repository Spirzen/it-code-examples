class Employee
  attr_reader :id, :hire_date
  attr_writer :department
  attr_accessor :name, :position, :salary
  
  def initialize(id, name, position, salary)
    @id = id
    @name = name
    @position = position
    @salary = salary
    @hire_date = Time.now
    @department = "IT"
  end
end

emp = Employee.new(101, "Иван Петров", "Разработчик", 100000)
puts emp.id          # 101
puts emp.name        # Иван Петров
puts emp.position    # Разработчик
puts emp.hire_date   # 2026-02-11 12:00:00 +0300

emp.name = "Иван Сидоров"
emp.position = "Старший разработчик"
emp.salary = 150000
emp.department = "DevOps"
