class Car(val brand: String) {
    var fuel: Double = 40.0
        private set
    var mileage: Int = 0
        private set

    fun refuel(liters: Double) {
        fuel += liters
        println("Заправка: +${liters.toInt()} л. Топливо: ${"%.1f".format(fuel)} л")
    }

    fun drive(km: Int) {
        val needed = km * FUEL_PER_KM
        if (needed > fuel) {
            println("Ошибка: недостаточно топлива")
            return
        }
        fuel -= needed
        mileage += km
        println("Проехали $km км. Топливо: ${"%.1f".format(fuel)} л. Пробег: $mileage км")
        if (mileage >= SERVICE_INTERVAL) {
            println("⚠️ ВНИМАНИЕ: требуется техобслуживание!")
        }
    }

    companion object {
        const val SERVICE_INTERVAL = 15000
        const val FUEL_PER_KM = 0.1
    }
}

fun main() {
    val car = Car("Lada")
    car.refuel(10.0)
    car.drive(5000)
    car.drive(11000)
}
