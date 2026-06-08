
import socket

host = "example.com"
port = 80

with socket.create_connection((host, port), timeout=5) as client:
    request = (
        "GET / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "Connection: close\r\n\r\n"
    )
    client.sendall(request.encode("utf-8"))

    response = client.recv(1024)
    print("Первые байты ответа:")
    print(response.decode("utf-8", errors="ignore"))
