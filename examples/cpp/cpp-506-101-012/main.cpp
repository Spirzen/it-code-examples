class DataProcessor 
{
public:
    void process_chunk(const char* data, size_t size)
    {
        if (data == nullptr) {
            throw std::invalid_argument("data pointer cannot be null");
        }
        if (size == 0) {
            throw std::invalid_argument("size must be greater than zero");
        }
        if (size > kMaxChunkSize) {
            throw std::invalid_argument("chunk size exceeds maximum allowed");
        }

        // Основная логика обработки
    }
};
