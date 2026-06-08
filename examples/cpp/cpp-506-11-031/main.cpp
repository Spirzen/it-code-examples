#include <iostream>
#include <mutex>
#include <string>

class ThreadSafeLogger {
private:
    mutable std::mutex mtx_;          // защищает внутреннее состояние
    mutable std::string last_message_; // кэш последнего сообщения

public:
    void log(const std::string& msg) const {
        // Метод const, но мы можем менять mutable-поля
        std::lock_guard<std::mutex> lock(mtx_);
        last_message_ = msg;
        std::cout << "[LOG] " << msg << '\n';
    }

    std::string getLastMessage() const {
        std::lock_guard<std::mutex> lock(mtx_);
        return last_message_;
    }
};

int main() {
    const ThreadSafeLogger logger;
    logger.log("Запуск системы");
    logger.log("Обработка данных");

    std::cout << "Последнее: " << logger.getLastMessage() << '\n';

    return 0;
}
