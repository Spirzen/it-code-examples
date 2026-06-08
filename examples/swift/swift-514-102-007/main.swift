class Vehicle {
    var brand: String
    var model: String
    var year: Int
    
    init(brand: String, model: String, year: Int) {
        self.brand = brand
        self.model = model
        self.year = year
    }
    
    func startEngine() {
        print("Двигатель запущен")
    }
    
    func stopEngine() {
        print("Двигатель остановлен")
    }
}

class Car: Vehicle {
    var numberOfDoors: Int
    
    init(brand: String, model: String, year: Int, doors: Int) {
        self.numberOfDoors = doors
        super.init(brand: brand, model: model, year: year)
    }
    
    func openTrunk() {
        print("Багажник открыт")
    }
}

class Motorcycle: Vehicle {
    var hasSidecar: Bool
    
    init(brand: String, model: String, year: Int, sidecar: Bool) {
        self.hasSidecar = sidecar
        super.init(brand: brand, model: model, year: year)
    }
    
    func doWheelie() {
        print("Выполняется вилли")
    }
}
