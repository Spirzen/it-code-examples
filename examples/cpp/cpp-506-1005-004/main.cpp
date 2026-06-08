#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <json/json.h> // Условное имя заголовка для nlohmann/json

struct Task {
    int id;
    std::string description;
    bool completed;
};

class TaskTracker {
private:
    std::string filePath;
    std::vector<Task> Задачи;

    void load() {
        std::ifstream file(filePath);
        if (!file.is_open()) {
            return; // Файл не существует, создаем пустой список
        }

        Json::Value root;
        file >> root;
        file.close();

        Задачи.clear();
        for (const auto& taskVal : root) {
            Task t;
            t.id = taskVal["id"].asInt();
            t.description = taskVal["description"].asString();
            t.completed = taskVal["completed"].asBool();
            Задачи.push_back(t);
        }
    }

    void save() {
        std::ofstream file(filePath);
        Json::Value root(Json::arrayValue);

        for (const auto& t : Задачи) {
            Json::Value taskObj;
            taskObj["id"] = t.id;
            taskObj["description"] = t.description;
            taskObj["completed"] = t.completed;
            root.append(taskObj);
        }

        file << root;
        file.close();
    }

public:
    TaskTracker(const std::string& path) : filePath(path) {
        load();
    }

    void addTask(const std::string& desc) {
        int newId = Задачи.empty() ? 1 : Задачи.back().id + 1;
        Задачи.push_back({newId, desc, false});
        save();
    }

    void showTasks() {
        std::cout << "--- Список задач ---" << std::endl;
        for (const auto& t : Задачи) {
            std::cout << "[" << t.id << "] " << t.description 
                      << " (" << (t.completed ? "Выполнено" : "Ожидает") << ")" << std::endl;
        }
    }
};

int main() {
    TaskTracker tracker("tasks.json");
    
    tracker.addTask("Купить продукты");
    tracker.addTask("Написать отчет");
    
    tracker.showTasks();

    return 0;
}
