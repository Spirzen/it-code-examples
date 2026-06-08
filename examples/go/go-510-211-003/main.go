package parse

import (
	"fmt"
	"strings"

	"golang.org/x/net/html"
)

// ExtractByTag извлекает текстовое содержимое всех элементов с указанным тегом.
// Например, tag="h2" вернёт все заголовки второго уровня.
func ExtractByTag(htmlContent, tag string) ([]string, error) {
	tag = strings.ToLower(strings.TrimSpace(tag))
	if tag == "" {
		return nil, fmt.Errorf("тег не может быть пустым")
	}

	doc, err := html.Parse(strings.NewReader(htmlContent))
	if err != nil {
		return nil, fmt.Errorf("разбор HTML: %w", err)
	}

	var results []string
	var walk func(*html.Node)

	walk = func(n *html.Node) {
		if n.Type == html.ElementNode && n.Data == tag {
			text := strings.TrimSpace(collectText(n))
			if text != "" {
				results = append(results, text)
			}
		}
		for child := n.FirstChild; child != nil; child = child.NextSibling {
			walk(child)
		}
	}

	walk(doc)
	return results, nil
}

// collectText собирает весь текст внутри узла (включая вложенные элементы).
func collectText(n *html.Node) string {
	if n.Type == html.TextNode {
		return n.Data
	}

	var b strings.Builder
	for child := n.FirstChild; child != nil; child = child.NextSibling {
		b.WriteString(collectText(child))
	}
	return b.String()
}
