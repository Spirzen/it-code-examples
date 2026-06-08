#include <iostream>
#include <string>
#include <regex>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>

struct ParsedUrl {
    std::string scheme;
    std::string host;
    int port;
    std::string path;
};

ParsedUrl parseUrl(const std::string& url) {
    ParsedUrl result;
    result.port = 80; // По умолчанию HTTP
    result.scheme = "http";
    result.path = "/";

    // Простая регулярка для разбора
    std::regex re(R"(^(\w+)://([^:/]+)(?::(\d+))?(/.*)?$)");
    std::smatch matches;

    if (std::regex_match(url, matches, re)) {
        if (matches.size() >= 2) result.scheme = matches[1].str();
        if (matches.size() >= 3) result.host = matches[2].str();
        if (matches.size() >= 4 && !matches[3].str().empty()) {
            result.port = std::stoi(matches[3].str());
        }
        if (matches.size() >= 5 && !matches[4].str().empty()) {
            result.path = matches[4].str();
        }
    }
    return result;
}

bool checkAvailability(const std::string& host, int port, const std::string& path) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(port);
    inet_pton(AF_INET, host.c_str(), &serverAddr.sin_addr);

    if (connect(sock, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
        close(sock);
        return false;
    }

    std::string request = "GET " + path + " HTTP/1.1\r\nHost: " + host + "\r\n\r\n";
    send(sock, request.c_str(), request.length(), 0);

    char buffer[1024];
    ssize_t bytesRead = recv(sock, buffer, sizeof(buffer) - 1, 0);
    buffer[bytesRead] = '\0';
    
    close(sock);

    // Извлекаем код ответа (первые 3 цифры после "HTTP/")
    std::string response(buffer);
    size_t pos = response.find(" ");
    if (pos != std::string::npos) {
        std::string codeStr = response.substr(pos + 1, 3);
        int code = std::stoi(codeStr);
        return (code >= 200 && code < 400);
    }
    return false;
}

int main() {
    std::string url = "https://example.com/docs/api";
    
    ParsedUrl parsed = parseUrl(url);
    
    std::cout << "URL: " << url << std::endl;
    std::cout << "Протокол: " << parsed.scheme << std::endl;
    std::cout << "Хост: " << parsed.host << std::endl;
    std::cout << "Порт: " << parsed.port << std::endl;
    std::cout << "Путь: " << parsed.path << std::endl;

    bool available = checkAvailability(parsed.host, parsed.port, parsed.path);
    std::cout << "Доступен: " << (available ? "Да" : "Нет") << std::endl;

    return 0;
}
