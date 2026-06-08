package main

import "fmt"

func main() {
    // Безопасные операции
    var slice []int = make([]int, 3)
    
    // Безопасный доступ к элементам
    for i := range slice {
        slice[i] = i * 10
    }
    
    fmt.Println(slice) // [0 10 20]
    
    // nil-указатель (в Go нет null)
    var str *string
    if str != nil {
        fmt.Println(*str)
    } else {
        fmt.Println("Указатель nil")
    }
}
