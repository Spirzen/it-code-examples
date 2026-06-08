type Address struct {
    Street string
    City   string
}

type Person struct {
    Name string
    Address // анонимное поле — встраивание
}

func main() {
    p := Person{
        Name: "Алексей",
        Address: Address{
            Street: "Ленина, 10",
            City:   "Уфа",
        },
    }
    fmt.Println(p.City) // Доступ к полю City напрямую — как будто оно в Person
}
