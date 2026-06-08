func swapValues<T>(_ a: inout T, _ b: inout T) {
    let temporary = a
    a = b
    b = temporary
}

func firstElement<T>(_  [T]) -> T? {
    return array.first
}

func contains<T: Equatable>(_ array: [T], value: T) -> Bool {
    return array.contains(value)
}

func merge<T>(_ first: [T], _ second: [T]) -> [T] {
    return first + second
}

var x = 5
var y = 10
swapValues(&x, &y)
print("x = \(x), y = \(y)")

let names = ["Анна", "Борис", "Виктор"]
if let first = firstElement(names) {
    print("Первое имя: \(first)")
}

let numbers = [1, 2, 3, 4, 5]
print("Содержит 3: \(contains(numbers, value: 3))")

let combined = merge([1, 2], [3, 4])
print("Объединённый массив: \(combined)")
