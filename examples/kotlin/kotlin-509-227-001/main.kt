fun main() {
    while (true) {
        println("1 — сложить  2 — выход")
        when (readln().trim()) {
            "1" -> {
                val a = readln().toIntOrNull() ?: continue
                val b = readln().toIntOrNull() ?: continue
                println(a + b)
            }
            "2" -> break
            else -> println("Неизвестная команда")
        }
    }
}
