const fs = require('fs').promises;
const path = require('path');

const DB_FILE = 'tasks.json';

class TaskTracker {
    constructor() {
        this.tasks = [];
    }

    async load() {
        try {
            const data = await fs.readFile(DB_FILE, 'utf-8');
            this.tasks = JSON.parse(data);
        } catch (error) {
            // Если файл не существует, начинаем с пустого списка
            if (error.code !== 'ENOENT') {
                throw error;
            }
            this.tasks = [];
        }
    }

    async save() {
        const jsonContent = JSON.stringify(this.tasks, null, 2);
        await fs.writeFile(DB_FILE, jsonContent, 'utf-8');
    }

    addTask(title, description = '') {
        const task = {
            id: Date.now(),
            title: title,
            description: description,
            completed: false,
            createdAt: new Date().toISOString()
        };
        this.tasks.push(task);
        this.save();
        console.log(`Задача #${task.id} добавлена.`);
    }

    listTasks() {
        if (this.tasks.length === 0) {
            console.log('Список задач пуст.');
            return;
        }
        this.tasks.forEach(task => {
            const status = task.completed ? '[x]' : '[ ]';
            console.log(`${status} #${task.id}: ${task.title}`);
        });
    }

    toggleTask(id) {
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            task.completed = !task.completed;
            this.save();
            console.log(`Статус задачи #${id} изменен.`);
        } else {
            console.log(`Задача #${id} не найдена.`);
        }
    }
}

// Пример использования
async function main() {
    const tracker = new TaskTracker();
    await tracker.load();
    
    tracker.addTask('Изучить Node.js', 'Прочитать документацию и написать код');
    tracker.listTasks();
    tracker.toggleTask(Date.now()); // Здесь ID должен быть реальным, полученным ранее
    
    console.log('Текущее состояние трекера сохранено в tasks.json');
}

// main();
