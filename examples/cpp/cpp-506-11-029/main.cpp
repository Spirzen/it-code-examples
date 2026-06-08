#include <iostream>
#include <string>

class Counter {
private:
    int count_ = 0;
    mutable int cache_ = -1; // может меняться даже в const-методах
    mutable bool cache_valid_ = false;

public:
    void increment() {
        ++count_;
        cache_valid_ = false;
    }

    // const-метод: не меняет логическое состояние
    int getCount() const {
        if (!cache_valid_) {
            cache_ = count_;        // OK: cache_ — mutable
            cache_valid_ = true;    // OK: mutable
        }
        return cache_;
    }

    // const-метод не может вызывать неконстантные методы
    // void reset() const { count_ = 0; } // Ошибка!
};

int main() {
    const Counter c; // объект объявлен как const
    // c.increment(); // Ошибка: increment() не const
    std::cout << "Count: " << c.getCount() << '\n'; // OK

    Counter d;
    d.increment();
    std::cout << "Count: " << d.getCount() << '\n'; // OK

    return 0;
}
