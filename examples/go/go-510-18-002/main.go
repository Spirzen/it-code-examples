func generate(nums []int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for _, n := range nums {
            out <- n
        }
    }()
    return out
}

func square(in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for n := range in {
            out <- n * n
        }
    }()
    return out
}

func sum(in <-chan int) int {
    total := 0
    for n := range in {
        total += n
    }
    return total
}

// Использование:
nums := []int{1, 2, 3, 4}
result := sum(square(generate(nums))) // 30
