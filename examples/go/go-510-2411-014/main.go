package main

import (

	"fmt"
	"net/http"
	"sync"
	"time"
)

type Result struct {
	URL      string
	Status   int
	Error    error
}

func checkConcurrency(urls []string, workers int) []Result {
	results := make([]Result, len(urls))
	var wg sync.WaitGroup
	semaphore := make(chan struct{}, workers)

	for i, url := range urls {
		wg.Add(1)
		go func(index int, target string) {
			defer wg.Done()
			
			semaphore <- struct{}{} // Занимаем слот
			defer func() { <-semaphore }() // Освобождаем слот

			client := &http.Client{Timeout: 5 * time.Second}
			resp, err := client.Head(target)
			
			status := 0
			if err == nil {
				status = resp.StatusCode
				defer resp.Body.Close()
			}

			results[index] = Result{
				URL:    target,
				Status: status,
				Error:  err,
			}
		}(i, url)
	}

	wg.Wait()
	return results
}

func main() {
	targets := []string{
		"https://google.com",
		"https://github.com",
		"https://example.com",
		"https://invalid-site-test.com",
	}

	fmt.Println("Запуск параллельной проверки...")
	start := time.Now()
	res := checkConcurrency(targets, 3) // Максимум 3 одновременных запроса
	elapsed := time.Since(start)

	for _, r := range res {
		if r.Error != nil {
			fmt.Printf("%s: Ошибка - %v\n", r.URL, r.Error)
		} else {
			fmt.Printf("%s: Статус %d\n", r.URL, r.Status)
		}
	}
	fmt.Printf("Время выполнения: %v\n", elapsed)
}
