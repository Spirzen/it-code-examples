#include <iostream>
#include <string>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <cstring>

#define PORT 8080

void handleClient(int clientSocket) {
    char buffer[1024];
    ssize_t bytesRead = read(clientSocket, buffer, sizeof(buffer) - 1);
    
    if (bytesRead > 0) {
        buffer[bytesRead] = '\0';
        
        std::string response = "HTTP/1.1 200 OK\r\n"
                               "Content-Type: text/plain\r\n"
                               "Connection: close\r\n"
                               "\r\n"
                               "Hello from C++ Server!";

        write(clientSocket, response.c_str(), response.length());
    }
    
    close(clientSocket);
}

int main() {
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    bind(serverSocket, (struct sockaddr*)&address, sizeof(address));
    listen(serverSocket, 3);

    std::cout << "Сервер запущен на порту " << PORT << std::endl;

    while (true) {
        struct sockaddr_in clientAddress;
        socklen_t clientLen = sizeof(clientAddress);
        int clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddress, &clientLen);

        if (clientSocket < 0) continue;

        handleClient(clientSocket);
    }

    close(serverSocket);
    return 0;
}
