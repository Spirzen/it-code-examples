
import socket
import threading

class ChatServer:
    def __init__(self, host='127.0.0.1', port=5555):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.nicknames = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Сервер запущен на {self.host}:{self.port}")
        print("Ожидание подключений...")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Подключение от {addr}")

            client_socket.send("NICK".encode('utf-8'))
            nickname = client_socket.recv(1024).decode('utf-8')

            self.clients.append(client_socket)
            self.nicknames.append(nickname)

            print(f"Никнейм: {nickname}")
            self.broadcast(f"{nickname} присоединился к чату!".encode('utf-8'))
            client_socket.send("Подключён к серверу".encode('utf-8'))

            thread = threading.Thread(target=self.handle_client, args=(client_socket, nickname))
            thread.start()

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.send(message)
            except OSError:
                pass

    def handle_client(self, client_socket, nickname):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"{nickname}: {message}")
                    self.broadcast(f"{nickname}: {message}".encode('utf-8'))
                else:
                    self.remove_client(client_socket, nickname)
                    break
            except OSError:
                self.remove_client(client_socket, nickname)
                break

    def remove_client(self, client_socket, nickname):
        if client_socket in self.clients:
            index = self.clients.index(client_socket)
            self.clients.remove(client_socket)
            self.nicknames.remove(nickname)
            client_socket.close()
            self.broadcast(f"{nickname} покинул чат.".encode('utf-8'))
            print(f"{nickname} отключился")

if __name__ == "__main__":
    server = ChatServer()
    server.start()
