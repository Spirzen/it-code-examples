class Vehicle {
    let brand: String
    let model: String
    var currentSpeed: Double
    
    init(brand: String, model: String) {
        // Фаза 1: инициализация всех свойств
        self.brand = brand
        self.model = model
        self.currentSpeed = 0.0
        
        // Фаза 2: можно использовать self
        print("Создан \(brand) \(model)")
    }
    
    convenience init(brand: String) {
        self.init(brand: brand, model: "Базовая модель")
    }
}

class ElectricCar: Vehicle {
    let batteryCapacity: Double
    var chargeLevel: Double
    
    init(brand: String, model: String, batteryCapacity: Double) {
        // Фаза 1 дочернего класса
        self.batteryCapacity = batteryCapacity
        self.chargeLevel = 100.0
        
        // Вызов инициализатора родителя до завершения фазы 1
        super.init(brand: brand, model: model)
        
        // Фаза 2 дочернего класса
        print("Электромобиль готов, заряд: \(chargeLevel)%")
    }
}
