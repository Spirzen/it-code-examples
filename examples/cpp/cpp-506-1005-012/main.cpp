#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

struct DateParts {
    int day, month, year;
};

DateParts parseDate(const std::string& dateStr, char delimiter) {
    std::stringstream ss(dateStr);
    DateParts parts;
    char sep;
    ss >> parts.day >> sep >> parts.month >> sep >> parts.year;
    return parts;
}

std::string convertToISO(DateParts parts) {
    std::ostringstream oss;
    oss << parts.year << "-" 
        << std::setw(2) << std::setfill('0') << parts.month << "-" 
        << std::setw(2) << std::setfill('0') << parts.day;
    return oss.str();
}

int main() {
    std::string input = "15.12.2023";
    
    DateParts parts = parseDate(input, '.');
    std::string isoFormat = convertToISO(parts);
    
    std::cout << "Ввод: " << input << std::endl;
    std::cout << "Вывод: " << isoFormat << std::endl;

    return 0;
}
