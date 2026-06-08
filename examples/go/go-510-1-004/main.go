package main

import (

    "fmt"
    "log"
    "net/http"
)

// Простой веб-сервер, демонстрирующий производительность
func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Привет из Go!")
}

func main() {
    http.HandleFunc("/", handler)
    
    // Лёгкое и быстрое развёртывание
    log.Fatal(http.ListenAndServe(":8080", nil))
}
