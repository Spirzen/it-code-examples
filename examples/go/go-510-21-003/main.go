type Job struct { /* ... */ }
type Result struct { /* ... */ }

func worker(id int, jobs <-chan Job, results chan<- Result) {
    for job := range jobs {
        // выполнение job
        results <- Result{ /* ... */ }
    }
}

func main() {
    const numWorkers = 8
    jobs := make(chan Job, 100)
    results := make(chan Result, 100)

    for w := 1; w <= numWorkers; w++ {
        go worker(w, jobs, results)
    }

    // отправка задач
    for _, j := range taskList {
        jobs <- j
    }
    close(jobs) // сигнал для всех worker'ов: больше задач не будет

    // сбор результатов
    for i := 0; i < len(taskList); i++ {
        <-results
    }
}
