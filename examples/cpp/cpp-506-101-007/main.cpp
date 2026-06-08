class FileHandle 
{
public:
    explicit FileHandle(const char* path, const char* mode)
        : handle_(std::fopen(path, mode)) 
    {
        if (!handle_) {
            throw std::runtime_error("Failed to open file");
        }
    }

    ~FileHandle() 
    {
        if (handle_) {
            std::fclose(handle_);
        }
    }

    // Запрет копирования
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;

    // Разрешение перемещения
    FileHandle(FileHandle&& other) noexcept
        : handle_(other.handle_) 
    {
        other.handle_ = nullptr;
    }

    FileHandle& operator=(FileHandle&& other) noexcept 
    {
        if (this != &other) {
            if (handle_) std::fclose(handle_);
            handle_ = other.handle_;
            other.handle_ = nullptr;
        }
        return *this;
    }

    std::FILE* get() const { return handle_; }

private:
    std::FILE* handle_;
};
