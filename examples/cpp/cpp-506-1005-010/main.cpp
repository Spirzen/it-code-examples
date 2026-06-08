#include <iostream>
#include <filesystem>
#include <iomanip>

namespace fs = std::filesystem;

void printDiskUsage(const fs::path& root) {
    auto total = fs::space(root).total_bytes;
    auto free = fs::space(root).free_bytes;
    auto used = total - free;

    double percentUsed = (static_cast<double>(used) / total) * 100.0;

    std::cout << "Диск: " << root << std::endl;
    std::cout << "Всего: " << total << " байт" << std::endl;
    std::cout << "Занято: " << used << " байт (" << std::fixed << std::setprecision(2) << percentUsed << "%)" << std::endl;
    std::cout << "Свободно: " << free << " байт" << std::endl;
    std::cout << "---------------------------" << std::endl;
}

int main() {
    fs::path root("/"); // Для Linux/macOS используйте "/" или конкретный том
    
    #ifdef _WIN32
    root = "C:\\"; // Для Windows
    #endif

    printDiskUsage(root);
    return 0;
}
