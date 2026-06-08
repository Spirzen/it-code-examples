// А. forEach — выполнение действия для каждого элемента (без возврата нового массива)
console.log("\n--- Обход всех задач ---");
tasks.forEach((task, index) => {
  console.log(`[${index}] ${task.title} (${task.status})`);
});

// Б. Map — трансформация данных (создание нового массива)
// Пример: получаем только заголовки всех задач
const titlesOnly = tasks.map(task => task.title);
console.log("\nТолько заголовки:", titlesOnly);

// В. Filter — фильтрация данных
// Пример: оставляем только задачи, которые еще не выполнены
const pendingTasks = tasks.filter(task => task.status !== "done");
console.log("\ntasks в работе:", pendingTasks.map(t => t.title));

// Г. Reduce — свертка массива в одно значение
// Пример: подсчет количества задач со статусом "todo"
const todoCount = tasks.reduce((count, task) => {
  return task.status === "todo" ? count + 1 : count;
}, 0); // 0 — начальное значение накопителя
console.log("\nКоличество задач 'todo':", todoCount);

// Д. Find / FindIndex — поиск конкретного элемента
const urgentTask = tasks.find(task => task.status === "urgent");
const urgentIndex = tasks.findIndex(task => task.status === "urgent");

if (urgentTask) {
  console.log("\nНайдена срочная задача:", urgentTask.title, "на индексе", urgentIndex);
} else {
  console.log("\nСрочных задач не найдено.");
}

// Е. Sort — сортировка (важно: sort меняет исходный массив)
// Сортируем задачи по приоритету статуса (условно: urgent > in-progress > todo > done)
const priorityOrder = { "urgent": 1, "in-progress": 2, "todo": 3, "done": 4 };

tasks.sort((a, b) => priorityOrder[a.status] - priorityOrder[b.status]);
console.log("\nОтсортированный список задач:");
tasks.forEach(t => console.log(`- ${t.title} (${t.status})`));

// Примечание: Для неизменяемой сортировки (ES2023+) можно использовать toSorted()
// const sortedCopy = tasks.toSorted((a, b) => ...);
