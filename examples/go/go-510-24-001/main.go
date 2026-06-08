package main

import (

	"bufio"
	"fmt"
	"os"
)

func main() {
	fmt.Print("Введите ваше имя: ")

	// Создаём буферизованный читатель для os.Stdin
	reader := bufio.NewReader(os.Stdin)

	// Читаем строку до символа новой строки
	name, err := reader.ReadString('\n')

	// Проверяем наличие ошибки
	if err != nil {
		fmt.Fprintf(os.Stderr, "Ошибка ввода: %v\n", err)
		os.Exit(1)
	}

	// Удаляем завершающий символ перевода строки
	name = name[:len(name)-1]

	// Формируем и выводим приветствие
	greeting := "Hello, " + name + "!"
	fmt.Println(greeting)
}
