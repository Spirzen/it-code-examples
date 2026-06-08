
import kotlinx.serialization.json.Json
import kotlinx.serialization.Serializable
import java.io.File

@Serializable
data class Task(val id: Int, val title: String, val isCompleted: Boolean)

fun loadTasks(): List<Task> {
    val file = File("tasks.json")
    if (!file.exists()) return emptyList()
    
    val jsonContent = file.readText()
    return Json.decodeFromString<List<Task>>(jsonContent)
}

fun saveTasks(Задачи: List<Task>) {
    val file = File("tasks.json")
    val jsonContent = Json.encodeToString(Задачи)
    file.writeText(jsonContent)
}

fun addTask(Задачи: MutableList<Task>, title: String) {
    val newId = Задачи.maxOfOrNull { it.id }?.plus(1) ?: 1
    Задачи.add(Task(newId, title, false))
    saveTasks(Задачи)
}

fun main() {
    val Задачи = loadTasks().toMutableList()
    
    // Добавление задачи
    addTask(Задачи, "Изучить Kotlin")
    addTask(Задачи, "Написать тесты")
    
    // Вывод списка
    println("Список задач:")
    Задачи.forEach { task ->
        val status = if (task.isCompleted) "[x]" else "[ ]"
        println("$status ${task.id}. ${task.title}")
    }
}
