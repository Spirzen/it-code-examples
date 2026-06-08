struct Stack<Element> {
    private var items: [Element] = []
    
    mutating func push(_ item: Element) {
        items.append(item)
    }
    
    mutating func pop() -> Element? {
        return items.popLast()
    }
    
    func peek() -> Element? {
        return items.last
    }
    
    var isEmpty: Bool {
        return items.isEmpty
    }
    
    var count: Int {
        return items.count
    }
}

class Cache<Key: Hashable, Value> {
    private var storage: [Key: Value] = [:]
    private let capacity: Int
    
    init(capacity: Int) {
        self.capacity = capacity
    }
    
    func get(_ key: Key) -> Value? {
        return storage[key]
    }
    
    mutating func set(_ key: Key, value: Value) {
        if storage.count >= capacity && !storage.keys.contains(key) {
            storage.removeFirst()
        }
        storage[key] = value
    }
    
    mutating func remove(_ key: Key) {
        storage.removeValue(forKey: key)
    }
    
    func contains(_ key: Key) -> Bool {
        return storage.keys.contains(key)
    }
}

enum LegacyResult<Value, Failure> {
    case success(Value)
    case failure(Failure)
    
    var isSuccess: Bool {
        if case .success = self { return true }
        return false
    }
    
    var isFailure: Bool {
        if case .failure = self { return true }
        return false
    }
    
    func getValue() -> Value? {
        if case .success(let value) = self {
            return value
        }
        return nil
    }
}

var intStack = Stack<Int>()
intStack.push(10)
intStack.push(20)
print(intStack.pop() ?? 0)

var stringCache = Cache<String, String>(capacity: 100)
stringCache.set("name", value: "Иван")
if let name = stringCache.get("name") {
    print("Имя из кэша: \(name)")
}

let result: Result<Int, String> = .success(42)
if result.isSuccess, let value = result.getValue() {
    print("Успешный результат: \(value)")
}
