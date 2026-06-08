package main

import (

	"fmt"
	"net/url"
	"time"
)

func checkURL(target string) error {
	parsedURL, err := url.Parse(target)
	if err != nil {
		return fmt.Errorf("неверный формат URL: %w", err)
	}

	fmt.Printf("Анализ URL: %s\n", target)
	fmt.Printf("  Схема: %s\n", parsedURL.Scheme)
	fmt.Printf("  Хост: %s\n", parsedURL.Host)
	fmt.Printf("  Путь: %s\n", parsedURL.Path)
	fmt.Printf("  Порт: %s\n", parsedURL.Port())

	timeout := 5 * time.Second
	client := &http.Client{
		Timeout: timeout,
	}

	resp, err := client.Head(target)
	if err != nil {
		return fmt.Errorf("проверка недоступна: %w", err)
	}
	defer resp.Body.Close()

	fmt.Printf("  Статус: %d\n", resp.StatusCode)
	fmt.Printf("  Время ответа: OK\n")
	return nil
}

func main() {
	urls := []string{
		"https://github.com",
		"http://invalid-domain-xyz.com",
	}

	for _, u := range urls {
		fmt.Println("---")
		if err := checkURL(u); err != nil {
			fmt.Println("Ошибка:", err)
		}
	}
}
