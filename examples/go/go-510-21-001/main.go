func fetchFromSource(id int, out chan<- Result) {
    res, err := http.Get(fmt.Sprintf("https://api.example.com/data/%d", id))
    if err != nil {
        out <- Result{Err: err}
        return
    }
    // ... обработка ответа
    out <- Result{Data: data}
}

func main() {
    ch := make(chan Result, 10)
    for i := 1; i <= 5; i++ {
        go fetchFromSource(i, ch)
    }

    var results []Result
    for i := 0; i < 5; i++ {
        results = append(results, <-ch)
    }
    close(ch)
    // анализ results
}
