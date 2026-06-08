extension Int {
    var squared: Int {
        return self * self
    }

    func times(_ closure: () -> Void) {
        for _ in 0..<self {
            closure()
        }
    }
}

print(5.squared) // 25
3.times { print("Hello") }
