func makeCounter() func() int {
    count := 0
    return func() int {
        count++
        return count
    }
}

c1 := makeCounter()
c2 := makeCounter()

fmt.Println(c1()) // 1
fmt.Println(c1()) // 2
fmt.Println(c2()) // 1 — независимый счётчик
