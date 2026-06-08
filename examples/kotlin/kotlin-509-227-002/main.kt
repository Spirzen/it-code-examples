fun main(args: Array<String>) {
    if (args.size < 2) {
        System.err.println("Использование: sum <a> <b>")
        return
    }

    val a = args[0].toIntOrNull()
    val b = args[1].toIntOrNull()
    if (a == null || b == null) {
        System.err.println("Оба аргумента должны быть целыми числами")
        return
    }

    println("Сумма: ${a + b}")
}
