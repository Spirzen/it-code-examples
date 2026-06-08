package main

import (

    "context"
    "fmt"
    "time"
)

func longTask(ctx context.Context) error {
    select {
    case <-time.After(5 * time.Second):
        return fmt.Errorf("task completed")
    case <-ctx.Done():
        return ctx.Err()
    }
}

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
    defer cancel()
    
    if err := longTask(ctx); err != nil {
        fmt.Println("Error:", err)
    }
}
