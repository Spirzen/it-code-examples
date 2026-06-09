class Smartphone {
    private let model: String
    private var battery: Int

    init(model: String) {
        self.model = model
        self.battery = 20
    }

    func call() {
        battery = max(0, battery - 5)
        print("Звонок с \(model)... Заряд: \(battery)%")
    }

    func charge() {
        battery = min(100, battery + 30)
        print("Зарядка \(model)... Заряд: \(battery)%")
    }

    func showStatus() {
        print("Смартфон \(model): заряд \(battery)%")
    }
}

let phone = Smartphone(model: "Pixel")
phone.showStatus()
phone.call()
phone.charge()
phone.showStatus()
