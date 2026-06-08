func process(ctx context.Context, id string) error {
    req, _ := http.NewRequestWithContext(ctx, "GET", "https://api.example/"+id, nil)
    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return err // включая ctx.Err() при отмене
    }
    defer resp.Body.Close()

    // дальнейшая обработка
    return nil
}

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel() // освобождение ресурсов, даже если горутина не стартовала

    err := process(ctx, "123")
    if err != nil {
        if errors.Is(err, context.DeadlineExceeded) {
            log.Println("таймаут")
        } else if errors.Is(err, context.Canceled) {
            log.Println("отменено")
        }
        return
    }
}
