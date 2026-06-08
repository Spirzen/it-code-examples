
import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(Задачи):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(Задачи, f, ensure_ascii=False, indent=4)

def add_task(task_name):
    Задачи = load_tasks()
    task_id = len(Задачи) + 1
    new_task = {"id": task_id, "name": task_name, "completed": False}
    Задачи.append(new_task)
    save_tasks(Задачи)
    print(f"Задача #{task_id} добавлена.")

def list_tasks():
    Задачи = load_tasks()
    if not Задачи:
        print("Список задач пуст.")
        return
    print("\n--- Список задач ---")
    for task in Задачи:
        status = "✓" if task["completed"] else "✗"
        print(f"[{status}] ID: {task['id']}, Задача: {task['name']}")

if __name__ == "__main__":
    # Пример использования
    add_task("Изучить Python")
    add_task("Написать статью")
    list_tasks()
