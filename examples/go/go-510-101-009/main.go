// LoadUserData загружает данные пользователя из внешнего сервиса.
// Возвращает ошибку с контекстом операции для упрощения отладки.
func LoadUserData(ctx context.Context, userID string) (*UserData, error) {
    req, err := http.NewRequestWithContext(ctx, "GET", apiURL, nil)
    if err != nil {
        return nil, fmt.Errorf("create request: %w", err)
    }

    req.Header.Set("X-User-ID", userID)

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, fmt.Errorf("execute request: %w", err)
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        return nil, fmt.Errorf("unexpected status %d", resp.StatusCode)
    }

    var Data UserData
    if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
        return nil, fmt.Errorf("decode response: %w", err)
    }

    return &data, nil
}
