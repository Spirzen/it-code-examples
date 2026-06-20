// Практикум: https://spirzen.ru/encyclopedia/4-code-dev/4-05-asinhronnost/3
package main

import (
	"fmt"
	"sync"
	"time"
)

type pageJob struct {
	url string
	d   time.Duration
}

func download(url string, delay time.Duration) {
	time.Sleep(delay)
	fmt.Printf("  Готово: %s\n", url)
}

func sequential(urls []pageJob) time.Duration {
	fmt.Println("\n1. ПОСЛЕДОВАТЕЛЬНО")
	start := time.Now()
	for _, u := range urls {
		download(u.url, u.d)
	}
	elapsed := time.Since(start)
	fmt.Printf("  Время: %.2f с\n", elapsed.Seconds())
	return elapsed
}

func parallel(urls []pageJob) time.Duration {
	fmt.Println("\n2. ГОРУТИНЫ + WaitGroup")
	start := time.Now()
	var wg sync.WaitGroup
	for _, u := range urls {
		wg.Add(1)
		go func(url string, d time.Duration) {
			defer wg.Done()
			download(url, d)
		}(u.url, u.d)
	}
	wg.Wait()
	elapsed := time.Since(start)
	fmt.Printf("  Время: %.2f с\n", elapsed.Seconds())
	return elapsed
}

func main() {
	urls := []pageJob{
		{"https://example.com/page1", 2 * time.Second},
		{"https://example.com/page2", 3500 * time.Millisecond},
		{"https://example.com/page3", 1500 * time.Millisecond},
		{"https://example.com/page4", 2500 * time.Millisecond},
		{"https://example.com/page5", 1 * time.Second},
	}

	fmt.Println("=== Go — sequential vs goroutines ===")

	seq := sequential(urls)
	par := parallel(urls)

	fmt.Println("\n--- Итог ---")
	fmt.Printf("Последовательно: %.2f с\n", seq.Seconds())
	fmt.Printf("Горутины:        %.2f с\n", par.Seconds())
	fmt.Printf("Ускорение:       %.2fx\n", seq.Seconds()/par.Seconds())
}
