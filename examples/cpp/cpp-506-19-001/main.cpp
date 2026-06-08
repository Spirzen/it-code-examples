class FileHandle {
    FILE* fp = nullptr;
public:
    explicit FileHandle(const char* name, const char* mode)
        : fp(std::fopen(name, mode)) {
        if (!fp) throw std::runtime_error("fopen failed");
    }
    ~FileHandle() {
        if (fp) std::fclose(fp);
    }
    FILE* get() const { return fp; }

    // Запрещаем копирование (единственное владение)
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;

    // Разрешаем перемещение
    FileHandle(FileHandle&& other) noexcept : fp(other.fp) { other.fp = nullptr; }
    FileHandle& operator=(FileHandle&& other) noexcept {
        if (this != &other) {
            if (fp) std::fclose(fp);
            fp = other.fp;
            other.fp = nullptr;
        }
        return *this;
    }
};
