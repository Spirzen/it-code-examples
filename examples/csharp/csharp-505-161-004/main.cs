using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

class TaskTracker
{
    class TaskItem
    {
        public int Id { get; set; }
        public string Description { get; set; }
        public bool IsCompleted { get; set; }
    }

    static void Main()
    {
        string filePath = "tasks.json";
        List<TaskItem> tasks = LoadTasks(filePath);

        Console.WriteLine("Добавьте новую задачу (введите описание, 'q' для выхода):");
        
        while (true)
        {
            string input = Console.ReadLine();
            if (input.ToLower() == "q") break;

            int id = tasks.Count > 0 ? tasks.Max(t => t.Id) + 1 : 1;
            tasks.Add(new TaskItem { Id = id, Description = input, IsCompleted = false });
            SaveTasks(tasks, filePath);
            Console.WriteLine($"Задача #{id} добавлена.");
        }

        Console.WriteLine("\nВсе задачи:");
        foreach (var task in tasks)
        {
            string status = task.IsCompleted ? "[x]" : "[ ]";
            Console.WriteLine($"{status} {task.Id}: {task.Description}");
        }
    }

    static List<TaskItem> LoadTasks(string path)
    {
        if (!File.Exists(path)) return new List<TaskItem>();
        
        string json = File.ReadAllText(path);
        return JsonSerializer.Deserialize<List<TaskItem>>(json) ?? new List<TaskItem>();
    }

    static void SaveTasks(List<TaskItem> tasks, string path)
    {
        string json = JsonSerializer.Serialize(tasks);
        File.WriteAllText(path, json);
    }
}
