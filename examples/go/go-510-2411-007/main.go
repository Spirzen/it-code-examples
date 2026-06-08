package main

import (

	"bytes"
	"fmt"
	"io"
	"net/http"
)

func sendPostRequest(url string, payload map[string]string) error {
	jsonData := []byte(`{"key": "value"}`) // Упрощенный пример JSON
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
	if err != nil {
		return err
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("User-Agent", "Go-Custom-Client/1.0")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Printf("Статус: %d, Тело: %s\n", resp.StatusCode, string(body))
	return nil
}

func main() {
	sendPostRequest("http://example.com/api/data", nil)
}
