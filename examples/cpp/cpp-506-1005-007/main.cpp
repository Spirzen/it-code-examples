#include <iostream>
#include <string>
#include <sstream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>

class HttpClient {
public:
    static std::string sendRequest(const std::string& host, int port, 
                                   const std::string& method, const std::string& path,
                                   const std::string& body = "") {
        int sock = socket(AF_INET, SOCK_STREAM, 0);
        struct sockaddr_in serverAddr;
        serverAddr.sin_family = AF_INET;
        serverAddr.sin_port = htons(port);
        inet_pton(AF_INET, host.c_str(), &serverAddr.sin_addr);

        if (connect(sock, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
            close(sock);
            return "Ошибка подключения";
        }

        std::ostringstream requestStream;
        requestStream << method << " " << path << " HTTP/1.1\r\n";
        requestStream << "Host: " << host << "\r\n";
        requestStream << "Content-Length: " << body.length() << "\r\n";
        requestStream << "Content-Type: application/json\r\n";
        requestStream << "\r\n";
        requestStream << body;

        std::string request = requestStream.str();
        send(sock, request.c_str(), request.length(), 0);

        char buffer[4096];
        std::string response;
        ssize_t bytesRead;
        
        while ((bytesRead = recv(sock, buffer, sizeof(buffer) - 1, 0)) > 0) {
            buffer[bytesRead] = '\0';
            response += buffer;
        }

        close(sock);
        return response;
    }
};

int main() {
    std::string body = "{\"message\": \"Hello from C++\"}";
    std::string response = HttpClient::sendRequest("httpbin.org", 80, "POST", "/post", body);
    
    std::cout << "Ответ:\n" << response << std::endl;
    return 0;
}
