package main

import (
	"fmt"
	"log"

	"gohtmlparser/internal/fetch"
)

func main() {
	html, err := fetch.HTML("https://example.com")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Загружено %d байт\n", len(html))
}
