#include <iostream>
#include <string>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>

int main() {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(8080);
    inet_pton(AF_INET, "127.0.0.1", &serverAddr.sin_addr);

    connect(sock, (struct sockaddr*)&serverAddr, sizeof(serverAddr));

    std::string request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n";
    send(sock, request.c_str(), request.length(), 0);

    char buffer[1024];
    ssize_t bytesReceived = recv(sock, buffer, sizeof(buffer) - 1, 0);
    buffer[bytesReceived] = '\0';

    std::cout << "Ответ сервера:\n" << buffer << std::endl;

    close(sock);
    return 0;
}
