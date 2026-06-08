const tasks = [
  { id: 1, title: "Написать код", completed: false },
  { id: 2, title: "Протестировать", completed: true }
];

// Добавление новой задачи
tasks.push({ id: 3, title: "Документировать", completed: false });

// Поиск незавершенных задач
const pendingTasks = tasks.filter(task => !task.completed);

// Изменение статуса задачи
tasks.forEach(task => {
  if (task.id === 1) {
    task.completed = true;
  }
});

// Удаление выполненной задачи
const updatedTasks = tasks.filter(task => task.id !== 2);
