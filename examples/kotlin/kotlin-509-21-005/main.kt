
import java.net.ServerSocket
import java.net.Socket
import java.io.PrintWriter
import java.io.BufferedReader
import java.io.InputStreamReader

fun startServer(port: Int) {
    ServerSocket(port).use { server ->
        println("Сервер запущен на порту $port")
        
        while (true) {
            Socket().use { client ->
                BufferedReader(InputStreamReader(client.inputStream)).use { reader ->
                    PrintWriter(client.outputStream, true).use { writer ->
                        val request = reader.readLine()
                        println("Получен запрос: $request")
                        
                        val response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello from Kotlin Server!"
                        writer.println(response)
                    }
                }
            }
        }
    }
}

fun main() {
    startServer(8080)
}
