package main

import (

	"fmt"
	"net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Привет! Это микросервис на Go, работающий внутри контейнера.")
}

func main() {
	http.HandleFunc("/", helloHandler)
	fmt.Println("Сервер запущен на порту 8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Printf("Ошибка запуска сервера: %v\n", err)
	}
}
