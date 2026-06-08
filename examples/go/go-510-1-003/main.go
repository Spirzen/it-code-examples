package main

import (

    "fmt"
    "sync"
    "time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        fmt.Printf("Worker %d начал работу с задачей %d\n", id, j)
        time.Sleep(time.Second)
        fmt.Printf("Worker %d завершил задачу %d\n", id, j)
        results <- j * 2
    }
}

func main() {
    const numJobs = 5
    jobs := make(chan int, numJobs)
    results := make(chan int, numJobs)
    
    // Запуск нескольких воркеров
    var wg sync.WaitGroup
    for w := 1; w <= 3; w++ {
        wg.Add(1)
        go func(wid int) {
            defer wg.Done()
            worker(wid, jobs, results)
        }(w)
    }
    
    // Отправка задач
    for j := 1; j <= numJobs; j++ {
        jobs <- j
    }
    close(jobs)
    
    // Ожидание завершения всех воркеров
    go func() {
        wg.Wait()
        close(results)
    }()
    
    // Сбор результатов
    for r := range results {
        fmt.Printf("Результат: %d\n", r)
    }
}
