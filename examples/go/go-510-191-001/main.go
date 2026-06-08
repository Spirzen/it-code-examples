func loadConfig(path string) ([]byte, error) {
    b, err := os.ReadFile(path)
    if err != nil {
        return nil, fmt.Errorf("load config from %s: %w", path, err)
    }
    return b, nil
}

data, err := loadConfig("config.yaml")
if err != nil {
    if errors.Is(err, os.ErrNotExist) {
        log.Println("конфиг не найден, используем значения по умолчанию")
    } else {
        log.Println("ошибка чтения конфига:", err)
    }
}
_ = data
