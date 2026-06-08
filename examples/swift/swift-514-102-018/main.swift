class Engine {
    var horsepower: Int
    var isRunning: Bool = false
    
    init(horsepower: Int) {
        self.horsepower = horsepower
    }
    
    func start() {
        isRunning = true
        print("Двигатель запущен")
    }
    
    func stop() {
        isRunning = false
        print("Двигатель остановлен")
    }
}

class Wheel {
    var size: Int
    var pressure: Double
    
    init(size: Int, pressure: Double) {
        self.size = size
        self.pressure = pressure
    }
    
    func rotate() {
        print("Колесо вращается")
    }
}

class Car {
    let engine: Engine
    var wheels: [Wheel]
    var brand: String
    
    init(brand: String, engine: Engine, wheels: [Wheel]) {
        self.brand = brand
        self.engine = engine
        self.wheels = wheels
    }
    
    func start() {
        engine.start()
        print("\(brand) готов к движению")
    }
    
    func drive() {
        engine.start()
        wheels.forEach { $0.rotate() }
    }
}

let carEngine = Engine(horsepower: 200)
let carWheels = [
    Wheel(size: 17, pressure: 2.3),
    Wheel(size: 17, pressure: 2.3),
    Wheel(size: 17, pressure: 2.3),
    Wheel(size: 17, pressure: 2.3)
]

let myCar = Car(brand: "Toyota", engine: carEngine, wheels: carWheels)
myCar.start()
