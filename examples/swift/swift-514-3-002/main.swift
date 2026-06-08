class Vehicle {
    var brand: String
    var maxSpeed: Int

    init(brand: String, maxSpeed: Int) {
        self.brand = brand
        self.maxSpeed = maxSpeed
    }

    func describe() -> String {
        return "Vehicle: \(brand), max speed \(maxSpeed)"
    }

    deinit {
        print("\(brand) deallocated")
    }
}
