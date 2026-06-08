class ValueHolder<T> {
    private var _value: T
    private var observers: [(T) -> Void] = []

    init(_ value: T) {
        self._value = value
    }

    var value: T {
        didSet {
            observers.forEach { $0(value) }
        }
    }

    func observe(_ handler: @escaping (T) -> Void) {
        observers.append(handler)
    }
}
