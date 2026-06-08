class Counter {
    var value: Int = 0
    
    func increment() {
        value += 1
    }
    
    func reset() {
        value = 0
    }
}

let counter1 = Counter()
let counter2 = counter1

counter1.increment()
counter1.increment()

print("counter1.value = \(counter1.value)") // 2
print("counter2.value = \(counter2.value)") // 2

counter2.reset()
print("counter1.value = \(counter1.value)") // 0
