#include <iostream>
#include <filesystem>
#include <system_error>

namespace fs = std::filesystem;

bool copyDirectoryWithProgress(const fs::path& source, const fs::path& dest) {
    if (!fs::exists(source)) {
        std::cerr << "Источник не найден: " << source << std::endl;
        return false;
    }

    if (!fs::exists(dest.parent_path())) {
        fs::create_directories(dest.parent_path());
    }

    std::error_code ec;
    fs::copy(source, dest, fs::copy_options::recursive | fs::copy_options::overwrite_if_newer, ec);

    if (ec) {
        std::cerr << "Ошибка копирования: " << ec.message() << std::endl;
        return false;
    }

    std::cout << "Резервное копирование завершено: " << dest << std::endl;
    return true;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Использование: " << argv[0] << " <исходная_папка> <целевая_папка>" << std::endl;
        return 1;
    }

    copyDirectoryWithProgress(argv[1], argv[2]);
    return 0;
}
