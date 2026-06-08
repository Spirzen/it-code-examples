#include <iostream>
#include <memory>

class ManagedArray {
private:
    int* data;
    size_t size;

public:
    ManagedArray(size_t s) : size(s) {
        std::cout << "Выделение памяти под массив размером " << size << std::endl;
        data = new int[size];
        for (size_t i = 0; i < size; ++i) {
            data[i] = static_cast<int>(i);
        }
    }

    ~ManagedArray() {
        std::cout << "Освобождение памяти массива" << std::endl;
        delete[] data;
        data = nullptr;
    }

    // Запрет копирования (чтобы избежать двойного удаления)
    ManagedArray(const ManagedArray&) = delete;
    ManagedArray& operator=(const ManagedArray&) = delete;

    // Разрешение перемещения
    ManagedArray(ManagedArray&& other) noexcept : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
    }

    ManagedArray& operator=(ManagedArray&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }

    void print() const {
        std::cout << "Массив: ";
        for (size_t i = 0; i < size; ++i) {
            std::cout << data[i] << " ";
        }
        std::cout << std::endl;
    }
};

// Пример использования умного указателя (std::unique_ptr)
void useSmartPointer() {
    std::unique_ptr<ManagedArray> ptr(new ManagedArray(5));
    ptr->print();
    // Память освободится автоматически при выходе из области видимости
}

int main() {
    {
        ManagedArray arr(3);
        arr.print();
        // Деструктор вызывается здесь
    }

    useSmartPointer();
    // Деструктор вызывается здесь

    return 0;
}
