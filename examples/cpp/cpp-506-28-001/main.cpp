#include <iostream>
#include <stdexcept>

class DatabaseConnection {
    int connection_id;
public:
    explicit DatabaseConnection(int id) : connection_id(id) {
        std::cout << "Подключение к БД #" << id << " установлено.\n";
    }

    ~DatabaseConnection() {
        std::cout << "Подключение #" << connection_id << " закрыто.\n";
    }

    void query() {
        if (connection_id == 0) {
            throw std::runtime_error("Ошибка подключения");
        }
        std::cout << "Выполнение запроса...\n";
    }
};

void process_data() {
    DatabaseConnection conn(42);
    
    // Имитация ошибки после успешного создания объекта
    if (true) { 
        throw std::runtime_error("Сбой обработки данных");
    }
}

int main() {
    try {
        process_data();
    } catch (const std::exception& e) {
        std::cout << "Поймано исключение: " << e.what() << "\n";
    }
    return 0;
}
