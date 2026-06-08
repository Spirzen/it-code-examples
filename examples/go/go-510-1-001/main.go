package main

import "fmt"

// Интерфейсы для композиции поведения
type Speaker interface {
    Speak() string
}

type Walker interface {
    Walk() string
}

// Композиция через встраивание структур
type Person struct {
    Name string
}

func (p Person) Speak() string {
    return fmt.Sprintf("%s говорит", p.Name)
}

func (p Person) Walk() string {
    return fmt.Sprintf("%s идёт", p.Name)
}

// Составной тип через композицию
type Student struct {
    Person
    Grade int
}

func (s Student) Study() string {
    return fmt.Sprintf("%s учится", s.Name)
}

func main() {
    s := Student{Person: Person{Name: "Анна"}, Grade: 5}
    
    // Используем композицию поведения
    fmt.Println(s.Speak())
    fmt.Println(s.Walk())
    fmt.Println(s.Study())
}
