class FileHandler {
    std::string filename;
    FILE* handle;

public:
    FileHandler(const std::string& name)
        : filename(name),                    // инициализация std::string
          handle(std::fopen(name.c_str(), "r"))  // инициализация handle
    {
        if (!handle)
            throw std::runtime_error("Failed to open file: " + name);
        // тело конструктора: логика после инициализации
    }

    ~FileHandler() {
        if (handle)
            std::fclose(handle);  // освобождение ресурса
    }
};
