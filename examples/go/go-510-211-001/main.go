package fetch

import (
	"fmt"
	"io"
	"net/http"
	"time"
)

const userAgent = "GoHTMLParser/1.0 (+https://github.com/example/gohtmlparser)"

// HTML скачивает HTML-страницу по URL и возвращает её содержимое как строку.
func HTML(url string) (string, error) {
	client := &http.Client{
		Timeout: 15 * time.Second,
	}

	req, err := http.NewRequest(http.MethodGet, url, nil)
	if err != nil {
		return "", fmt.Errorf("создание запроса: %w", err)
	}

	// Некоторые сайты отклоняют запросы без User-Agent.
	req.Header.Set("User-Agent", userAgent)

	resp, err := client.Do(req)
	if err != nil {
		return "", fmt.Errorf("выполнение запроса: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("неожиданный статус: %s", resp.Status)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", fmt.Errorf("чтение ответа: %w", err)
	}

	return string(body), nil
}
