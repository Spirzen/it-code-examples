fun calculate(a: Double, b: Double, operator: Char): Double? {
    return when (operator) {
        '+' -> a + b
        '-' -> a - b
        '*' -> a * b
        '/' -> if (b != 0.0) a / b else null
        else -> null
    }
}

fun main() {
    print("Введите первое число: ")
    val num1 = readLine()?.toDoubleOrNull() ?: run { 
        println("Ошибка ввода числа"); return 
    }

    print("Введите операцию (+, -, *, /): ")
    val op = readLine()?.firstOrNull() ?: run { 
        println("Ошибка ввода операции"); return 
    }

    print("Введите второе число: ")
    val num2 = readLine()?.toDoubleOrNull() ?: run { 
        println("Ошибка ввода числа"); return 
    }

    val result = calculate(num1, num2, op)

    if (result != null) {
        println("Результат: $result")
    } else {
        println("Неверная операция или деление на ноль.")
    }
}
