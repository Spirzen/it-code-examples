#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

class FileSorter {
public:
    static bool sortFile(const std::string& inputPath, const std::string& outputPath) {
        std::ifstream inputFile(inputPath);
        if (!inputFile.is_open()) {
            std::cerr << "Ошибка открытия входного файла: " << inputPath << std::endl;
            return false;
        }

        std::vector<std::string> lines;
        std::string line;

        while (std::getline(inputFile, line)) {
            lines.push_back(line);
        }
        inputFile.close();

        std::sort(lines.begin(), lines.end());

        std::ofstream outputFile(outputPath);
        if (!outputFile.is_open()) {
            std::cerr << "Ошибка открытия выходного файла: " << outputPath << std::endl;
            return false;
        }

        for (const auto& l : lines) {
            outputFile << l << "\n";
        }
        outputFile.close();

        std::cout << "Файл успешно отсортирован: " << outputPath << std::endl;
        return true;
    }
};

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Использование: " << argv[0] << " <входной_файл> <выходной_файл>" << std::endl;
        return 1;
    }

    FileSorter::sortFile(argv[1], argv[2]);
    return 0;
}
