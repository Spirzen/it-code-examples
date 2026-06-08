// Доступ по индексу (нулевая база)
const firstTask = tasks[0]; 
console.log("Первая задача:", firstTask.title);

// Доступ к последнему элементу через отрицательный индекс
const lastTask = tasks[tasks.length - 1]; 
console.log("Последняя задача:", lastTask.title);

// Изменение существующего значения
tasks[1].status = "in-progress"; // Меняем статус второй задачи
console.log("Обновленный статус 2-й задачи:", tasks[1].status);

// Добавление элементов в конец (Push)
tasks.push({ id: 4, title: "Рефакторинг кода", status: "todo" });

// Добавление элементов в начало (Unshift)
tasks.unshift({ id: 0, title: "Самая важная задача", status: "urgent" });

// Удаление последнего элемента (Pop)
const removedTask = tasks.pop();
console.log("Удаленная задача:", removedTask.title);

// Удаление первого элемента (Shift)
const shiftedTask = tasks.shift();
console.log("Сдвинутая задача:", shiftedTask.title);

// Вставка/удаление в середине (Splice)
// Удаляем 1 элемент начиная с индекса 2 и добавляем новый
tasks.splice(2, 1, { id: 99, title: "Новая задача взамен старой", status: "review" });

// Проверка наличия элемента (includes)
const hasReview = tasks.some(t => t.status === "review");
console.log("Есть ли задача со статусом review?", hasReview);
