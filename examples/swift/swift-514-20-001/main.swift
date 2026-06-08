struct TodoItem: Identifiable {
    let id = UUID()
    var title: String
    var isDone: Bool
}

var todos: [TodoItem] = [
    TodoItem(title: "Установить Xcode", isDone: true),
    TodoItem(title: "Прочитать про optionals", isDone: false)
]

todos.append(TodoItem(title: "Написать первый Playground", isDone: false))
let pending = todos.filter { !$0.isDone }
print("Осталось: \(pending.count)")
