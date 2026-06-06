data class Task(val id: Int, val title: String, val done: Boolean = false)

fun main() {
    val tasks = listOf(Task(1, "Прочитать статью"), Task(2, "Запустить пример", true))
    for (task in tasks) {
        val mark = when (task.done) {
            true -> "[x]"
            false -> "[ ]"
        }
        println("$mark ${task.title}")
    }
}
