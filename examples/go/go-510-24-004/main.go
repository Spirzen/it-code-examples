package main

import (

	"bufio"
	"fmt"
	"os"

	"github.com/fatih/color"
)

func main() {
	fmt.Print("Введите ваше имя: ")
	reader := bufio.NewReader(os.Stdin)
	name, err := reader.ReadString('\n')
	if err != nil {
		color.Red("Ошибка ввода: %v", err)
		os.Exit(1)
	}
	name = name[:len(name)-1]

	greeting := buildGreeting(name)
	color.Green(greeting)
}

func buildGreeting(name string) string {
	return "Hello, " + name + "!"
}
