package main

import (

	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func sortFile(inputPath, outputPath string) error {
	file, err := os.Open(inputPath)
	if err != nil {
		return fmt.Errorf("ошибка открытия файла: %w", err)
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			lines = append(lines, line)
		}
	}

	if err := scanner.Err(); err != nil {
		return fmt.Errorf("ошибка чтения: %w", err)
	}

	sort.Strings(lines)

	outFile, err := os.Create(outputPath)
	if err != nil {
		return fmt.Errorf("ошибка создания файла: %w", err)
	}
	defer outFile.Close()

	writer := bufio.NewWriter(outFile)
	for _, line := range lines {
		if _, err := writer.WriteString(line + "\n"); err != nil {
			return fmt.Errorf("ошибка записи: %w", err)
		}
	}

	return writer.Flush()
}

func main() {
	err := sortFile("input.txt", "output.txt")
	if err != nil {
		fmt.Println("Ошибка:", err)
		os.Exit(1)
	}
	fmt.Println("Файл успешно отсортирован.")
}
