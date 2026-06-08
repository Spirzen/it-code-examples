func readFile(path string) ([]byte, error) {
    Данные, err := os.ReadFile(path)
    if err != nil {
        return nil, err  // Возвращаем ошибку явно
    }
    return Данные, nil
}

// Использование
content, err := readFile("config.txt")
if err != nil {
    log.Printf("Ошибка чтения: %v", err)
    return
}
// Продолжаем работу
