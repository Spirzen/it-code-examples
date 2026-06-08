package main

import (

	"fmt"
	"os"
	"path/filepath"
)

func scanDirectory(root string) error {
	return filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		
		indent := ""
		relPath, _ := filepath.Rel(root, path)
		for i := 0; i < len(filepath.SplitList(relPath)); i++ {
			indent += "  "
		}

		typeStr := "файл"
		if info.IsDir() {
			typeStr = "каталог"
		}
		
		fmt.Printf("%s[%s] %s (%d байт)\n", indent, typeStr, info.Name(), info.Size())
		return nil
	})
}

func main() {
	currentDir, _ := os.Getwd()
	fmt.Println("Сканирование директории:", currentDir)
	if err := scanDirectory(currentDir); err != nil {
		fmt.Println("Ошибка:", err)
	}
}
