#include <iostream>
#include <string>
#include <vector>
#include <random>
#include <chrono>

class PasswordGenerator {
private:
    std::string characters;
    std::mt19937 generator;

public:
    PasswordGenerator() {
        // Инициализация генератора случайных чисел на основе текущего времени
        auto seed = std::chrono::high_resolution_clock::now().time_since_epoch().count();
        generator.seed(static_cast<unsigned long>(seed));

        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";
    }

    std::string generate(size_t length) {
        if (length == 0) return "";

        std::uniform_int_distribution<size_t> distribution(0, characters.size() - 1);
        std::string password;
        password.reserve(length);

        for (size_t i = 0; i < length; ++i) {
            password += characters[distribution(generator)];
        }

        return password;
    }
};

int main() {
    PasswordGenerator gen;
    size_t length = 16; // Стандартная длина пароля

    std::cout << "Сгенерированный пароль: " << gen.generate(length) << std::endl;

    return 0;
}
