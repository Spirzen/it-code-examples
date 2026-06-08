#include <iostream>
#include <filesystem>
#include <string>

namespace fs = std::filesystem;

void scanDirectory(const fs::path& path, int indent = 0) {
    for (const auto& entry : fs::directory_iterator(path)) {
        std::string prefix(indent, ' ');
        if (entry.is_directory()) {
            std::cout << prefix << "[DIR] " << entry.path().filename() << std::endl;
            scanDirectory(entry.path(), indent + 2);
        } else {
            auto size = entry.file_size();
            std::cout << prefix << "[FILE] " << entry.path().filename() 
                      << " (" << size << " байт)" << std::endl;
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Использование: " << argv[0] << " <путь_к_директории>" << std::endl;
        return 1;
    }

    fs::path targetPath(argv[1]);
    if (!fs::exists(targetPath) || !fs::is_directory(targetPath)) {
        std::cerr << "Указанный путь не существует или не является директорией." << std::endl;
        return 1;
    }

    scanDirectory(targetPath);
    return 0;
}
