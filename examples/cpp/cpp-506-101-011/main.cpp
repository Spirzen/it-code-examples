class LargeDataBuffer 
{
public:
    // Конструктор перемещения
    LargeDataBuffer(LargeDataBuffer&& other) noexcept
        : data_(other.data_), size_(other.size_) 
    {
        other.data_ = nullptr;
        other.size_ = 0;
    }

    // Оператор присваивания перемещением
    LargeDataBuffer& operator=(LargeDataBuffer&& other) noexcept 
    {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
        }
        return *this;
    }

private:
    char* data_;
    size_t size_;
};
