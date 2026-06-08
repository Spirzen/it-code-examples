class TaskBuilder {
    List<String> Задачи = []

    def task(String description, Closure action) {
        Задачи << description
        action()
    }
}

def builder = new TaskBuilder()
builder.task("Compile sources") {
    println "Compiling..."
}
builder.task("Run tests") {
    println "Тестирование..."
}

println builder.Задачи
// [Compile sources, Run tests]
