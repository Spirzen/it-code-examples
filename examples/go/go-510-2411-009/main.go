package main

import (

	"fmt"
	"io"
	"os"
	"path/filepath"
	"time"
)

func copyFile(src, dst string) error {
	sourceFile, err := os.Open(src)
	if err != nil {
		return err
	}
	defer sourceFile.Close()

	destFile, err := os.Create(dst)
	if err != nil {
		return err
	}
	defer destFile.Close()

	if _, err := io.Copy(destFile, sourceFile); err != nil {
		return err
	}
	return nil
}

func createBackup(sourceDir string) error {
	timestamp := time.Now().Format("2006-01-02_15-04-05")
	backupName := "backup_" + timestamp
	backupPath := filepath.Join(sourceDir, backupName)

	files, err := os.ReadDir(sourceDir)
	if err != nil {
		return err
	}

	for _, file := range files {
		if file.IsDir() {
			continue
		}
		
		srcPath := filepath.Join(sourceDir, file.Name())
		dstPath := filepath.Join(backupPath, file.Name())
		
		// Создание целевой директории бэкапа
		os.MkdirAll(backupPath, 0755)
		
		if err := copyFile(srcPath, dstPath); err != nil {
			fmt.Printf("Не удалось скопировать %s: %v\n", file.Name(), err)
			continue
		}
		fmt.Printf("Скопировано: %s\n", file.Name())
	}
	return nil
}

func main() {
	dir := "."
	fmt.Println("Начало резервного копирования...")
	if err := createBackup(dir); err != nil {
		fmt.Println("Ошибка:", err)
	} else {
		fmt.Println("Резервное копирование завершено.")
	}
}
