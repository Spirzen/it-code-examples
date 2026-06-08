package main

import (

	"fmt"
	"os"
)

// Person представляет структуру человека
type Person struct {
	Name string
	Age  int
}

// Employee встраивает Person и добавляет поля работы
type Employee struct {
	Person
	Position string
	Salary   float64
}

// NewEmployee создает нового сотрудника
func NewEmployee(name string, age int, position string, salary float64) *Employee {
	return &Employee{
		Person: Person{
			Name: name,
			Age:  age,
		},
		Position: position,
		Salary:   salary,
	}
}

// GetInfo возвращает информацию о сотруднике
func (e *Employee) GetInfo() string {
	return fmt.Sprintf("Name: %s, Age: %d, Position: %s, Salary: %.2f", e.Name, e.Age, e.Position, e.Salary)
}

// CalculateBonus вычисляет бонус сотрудника
func (e *Employee) CalculateBonus() float64 {
	return e.Salary * 0.1
}

// ProcessData обрабатывает срез целых и возвращает сумму или ошибку
func ProcessData(data []int) (int, error) {
	if len(data) == 0 {
		return 0, fmt.Errorf("empty data provided")
	}

	sum := 0
	for _, value := range data {
		sum += value
	}

	return sum, nil
}

// main является точкой входа в программу
func main() {
	// Создаем нового сотрудника
	emp := NewEmployee("Alice", 30, "Developer", 75000.0)

	// Выводим информацию о сотруднике
	fmt.Println(emp.GetInfo())

	// Вычисляем бонус
	bonus := emp.CalculateBonus()
	fmt.Printf("Bonus: %.2f\n", bonus)

	// Обрабатываем данные
	data := []int{1, 2, 3, 4, 5}
	result, err := ProcessData(data)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error processing data: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Sum of data: %d\n", result)

	// Используем defer для закрытия файла
	file, err := os.Open("example.txt")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error opening file: %v\n", err)
		os.Exit(1)
	}
	defer file.Close()

	// Пример с анонимной функцией и замыканием
	adder := func(x int) func(int) int {
		return func(y int) int {
			return x + y
		}
	}

	f := adder(10)
	fmt.Printf("Result of closure: %d\n", f(5))
}
