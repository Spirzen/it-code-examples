#include <iostream>
#include <string>

class User {
private:
    std::string username;
    std::string password;
    bool logged_in;

public:
    User(const std::string& username, const std::string& password)
        : username(username), password(password), logged_in(false) {}

    void login(const std::string& pwd) {
        if (pwd == password) {
            logged_in = true;
            std::cout << "Добро пожаловать, " << username << "!" << std::endl;
        } else {
            std::cout << "Ошибка: неверный пароль" << std::endl;
        }
    }

    void logout() {
        logged_in = false;
        std::cout << username << " вышел из системы" << std::endl;
    }

    void post_message(const std::string& text) {
        if (!logged_in) {
            std::cout << "Сначала войдите в систему" << std::endl;
            return;
        }
        std::cout << "Сообщение опубликовано: " << text << std::endl;
    }
};

int main() {
    User user("alex", "secret123");
    user.post_message("Привет!");
    user.login("wrong");
    user.login("secret123");
    user.post_message("Привет, мир!");
    user.logout();
    user.post_message("Ещё одно сообщение");
    return 0;
}
