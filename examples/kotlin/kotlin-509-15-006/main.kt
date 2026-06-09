class Student(val name: String) {
    private val grades = mutableListOf<Int>()

    fun addGrade(grade: Int) {
        grades.add(grade)
        println("Оценка $grade добавлена для $name")
    }

    fun averageScore(): Double {
        if (grades.isEmpty()) return 0.0
        return grades.average()
    }

    fun isPassing(): Boolean = averageScore() >= PASSING_SCORE

    fun info() {
        println("Студент: $name")
        println("Оценки: $grades")
        println("Средний балл: ${"%.1f".format(averageScore())}")
        println(if (isPassing()) "Зачёт получен" else "Зачёт не получен")
    }

    companion object {
        const val PASSING_SCORE = 60
    }
}

fun main() {
    val student = Student("Анна")
    student.addGrade(70)
    student.addGrade(85)
    student.addGrade(55)
    student.info()
}
