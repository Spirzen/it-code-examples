class FileHandler {
private:
    FILE* file;
    
public:
    FileHandler(const char* filename) {
        file = fopen(filename, "r");   // выделяем ресурс
    }
    
    ~FileHandler() {                    // деструктор
        if (file) {
            fclose(file);               // освобождаем ресурс АВТОМАТИЧЕСКИ
        }
    }
    
    void read() { /* ... */ }
};

// Использование (RAII — Resource Acquisition Is Initialization)
void processFile() {
    FileHandler fh("data.txt");   // ресурс захвачен
    fh.read();                    // работаем
    // здесь fh уничтожится, деструктор закроет файл — даже если исключение!
}
