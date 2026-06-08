package main

import (

	"fmt"
	"os/exec"
	"strings"
)

func listProcesses() error {
	var cmd *exec.Cmd
	var args []string

	// Определение команды в зависимости от ОС
	if isWindows() {
		cmd = exec.Command("tasklist", "/FO", "CSV")
		args = []string{}
	} else {
		cmd = exec.Command("ps", "aux")
		args = []string{}
	}

	output, err := cmd.Output()
	if err != nil {
		return fmt.Errorf("ошибка выполнения команды: %w", err)
	}

	lines := strings.Split(string(output), "\n")
	for i, line := range lines {
		if i == 0 && !isWindows() {
			continue // Пропуск заголовка в Linux/Mac
		}
		if line == "" {
			continue
		}
		fmt.Println(line)
	}
	return nil
}

func isWindows() bool {
	return true // Заглушка для примера, в реальности используйте runtime.GOOS
}

func main() {
	fmt.Println("Список процессов:")
	if err := listProcesses(); err != nil {
		fmt.Println("Ошибка:", err)
	}
}
