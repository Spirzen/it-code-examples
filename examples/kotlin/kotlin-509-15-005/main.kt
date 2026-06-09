class Smartphone(private val model: String) {
    private var battery: Int = 20

    fun call() {
        battery = maxOf(0, battery - 5)
        println("Звонок с $model... Заряд: $battery%")
    }

    fun charge() {
        battery = minOf(100, battery + 30)
        println("Зарядка $model... Заряд: $battery%")
    }

    fun showStatus() {
        println("Смартфон $model: заряд $battery%")
    }
}

fun main() {
    val phone = Smartphone("Pixel")
    phone.showStatus()
    phone.call()
    phone.charge()
    phone.showStatus()
}
