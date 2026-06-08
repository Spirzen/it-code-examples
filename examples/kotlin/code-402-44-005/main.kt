var name: String = "Алексей"
name = null // Ошибка компиляции

var nullableName: String? = "Мария"
nullableName = null // Разрешено

// Безопасный вызов
val length = nullableName?.length

// Оператор Elvis
val displayName = nullableName ?: "Гость"

// Утверждение ненулевого значения
val safeName: String = nullableName!! // Исключение при null
