package main

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"time"
)

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	req, _ := http.NewRequestWithContext(ctx, http.MethodGet, "https://httpbin.org/get", nil)
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()

	body, _ := io.ReadAll(io.LimitReader(res.Body, 256))
	fmt.Printf("status=%d body=%q\n", res.StatusCode, body)
}
