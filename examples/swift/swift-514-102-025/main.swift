public class PublicClass {
    public var publicProperty: String = "Публичное"
    internal var internalProperty: String = "Внутреннее"
    fileprivate var fileprivateProperty: String = "Файловое"
    private var privateProperty: String = "Приватное"
    
    public func publicMethod() {
        print("Публичный метод")
    }
    
    internal func internalMethod() {
        print("Внутренний метод")
    }
    
    fileprivate func fileprivateMethod() {
        print("Файловый метод")
    }
    
    private func privateMethod() {
        print("Приватный метод")
    }
}

internal class InternalClass {
    // По умолчанию все объявления internal
    var property: String = "Свойство"
    
    func method() {
        print("Метод")
    }
}

fileprivate class FilePrivateClass {
    var property: String = "Свойство"
}

private class PrivateClass {
    var property: String = "Свойство"
}
