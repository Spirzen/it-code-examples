package main

import (

	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func calculate(a float64, b float64, op string) (float64, error) {
	switch op {
	case "+":
		return a + b, nil
	case "-":
		return a - b, nil
	case "*":
		return a * b, nil
	case "/":
		if b == 0 {
			return 0, fmt.Errorf("деление на ноль невозможно")
		}
		return a / b, nil
	default:
		return 0, fmt.Errorf("неподдерживаемая операция: %s", op)
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Введите первое число: ")
	num1Str, _ := reader.ReadString('\n')
	num1, _ := strconv.ParseFloat(strings.TrimSpace(num1Str), 64)

	fmt.Print("Введите операцию (+, -, *, /): ")
	opStr, _ := reader.ReadString('\n')
	op := strings.TrimSpace(opStr)

	fmt.Print("Введите второе число: ")
	num2Str, _ := reader.ReadString('\n')
	num2, _ := strconv.ParseFloat(strings.TrimSpace(num2Str), 64)

	result, err := calculate(num1, num2, op)
	if err != nil {
		fmt.Println("Ошибка:", err)
		return
	}

	fmt.Printf("Результат: %.2f\n", result)
}
