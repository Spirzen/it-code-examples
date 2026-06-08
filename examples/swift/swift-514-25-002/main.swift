@propertyWrapper
struct Logged<Value> {
    private var value: Value
    init(wrappedValue: Value) { self.value = wrappedValue }

    var wrappedValue: Value {
        get { value }
        set {
            print("было: \(value), стало: \(newValue)")
            value = newValue
        }
    }

    var projectedValue: Logged<Value> { self }
    func reset(to newValue: Value) { value = newValue }
}

struct Form {
    @Logged var email = ""
}

var form = Form()
form.email = "a@b.c"
form.$email.reset(to: "")
