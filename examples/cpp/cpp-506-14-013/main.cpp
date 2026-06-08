class GoodBuffer {
    int* data = nullptr;
    size_t size = 0;

public:
    GoodBuffer(size_t n) : size(n), data(new int[n]) {}

    // Конструктор копирования
    GoodBuffer(const GoodBuffer& other)
        : size(other.size), data(new int[other.size]) {
        std::copy(other.data, other.data + other.size, data);
    }

    // Оператор присваивания копированием
    GoodBuffer& operator=(const GoodBuffer& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new int[size];
            std::copy(other.data, other.data + other.size, data);
        }
        return *this;
    }

    // Конструктор перемещения
    GoodBuffer(GoodBuffer&& other) noexcept
        : size(other.size), data(other.data) {
        other.size = 0;
        other.data = nullptr;
    }

    // Оператор присваивания перемещением
    GoodBuffer& operator=(GoodBuffer&& other) noexcept {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = other.data;
            other.size = 0;
            other.data = nullptr;
        }
        return *this;
    }

    ~GoodBuffer() { delete[] data; }
};
