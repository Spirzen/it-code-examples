  ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
  defer cancel()

  req, err := http.NewRequestWithContext(ctx, http.MethodGet, "https://example.com", nil)
  if err != nil {
      return err
  }
  resp, err := http.DefaultClient.Do(req)
  if err != nil {
      if errors.Is(err, context.DeadlineExceeded) {
          return fmt.Errorf("запрос не уложился в 5 секунд")
      }
      return err
  }
  defer resp.Body.Close()
