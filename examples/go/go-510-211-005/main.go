package main

import (
	"flag"
	"fmt"
	"log"
	"os"

	"gohtmlparser/internal/fetch"
	"gohtmlparser/internal/parse"
)

func main() {
	url := flag.String("url", "", "URL страницы для парсинга (обязательный)")
	tag := flag.String("tag", "h2", "HTML-тег для извлечения: h1, h2, h3, a и т.д.")
	flag.Parse()

	if *url == "" {
		fmt.Println("Парсер веб-страниц — извлекает данные из HTML.")
		fmt.Println()
		fmt.Println("Использование:")
		fmt.Println("  go run . -url <адрес> [-tag <тег>]")
		fmt.Println()
		fmt.Println("Примеры:")
		fmt.Println("  go run . -url https://example.com -tag h1")
		fmt.Println("  go run . -url https://news.ycombinator.com -tag a")
		os.Exit(1)
	}

	log.Printf("Скачиваем страницу: %s", *url)
	htmlContent, err := fetch.HTML(*url)
	if err != nil {
		log.Fatalf("Ошибка загрузки: %v", err)
	}
	log.Printf("Загружено %d байт", len(htmlContent))

	log.Printf("Ищем элементы <%s>...", *tag)
	items, err := parse.ExtractByTag(htmlContent, *tag)
	if err != nil {
		log.Fatalf("Ошибка парсинга: %v", err)
	}

	if len(items) == 0 {
		log.Printf("Элементы <%s> не найдены.", *tag)
		return
	}

	fmt.Printf("\nНайдено %d элементов <%s>:\n\n", len(items), *tag)
	for i, item := range items {
		fmt.Printf("%d. %s\n", i+1, item)
	}
}
