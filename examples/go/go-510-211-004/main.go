package main

import (
	"fmt"
	"log"

	"gohtmlparser/internal/fetch"
	"gohtmlparser/internal/parse"
)

func main() {
	html, err := fetch.HTML("https://example.com")
	if err != nil {
		log.Fatal(err)
	}

	items, err := parse.ExtractByTag(html, "h1")
	if err != nil {
		log.Fatal(err)
	}
	for i, item := range items {
		fmt.Printf("%d. %s\n", i+1, item)
	}
}
