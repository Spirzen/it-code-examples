class BaseClass {
    func performAction() {
        print("Базовое действие")
    }
    
    final func criticalAction() {
        print("Критическое действие")
    }
}

class DerivedClass: BaseClass {
    override func performAction() {
        print("Расширенное действие")
        super.performAction()
    }
    
    // Ошибка: нельзя переопределить final метод
    // override func criticalAction() { }
}
