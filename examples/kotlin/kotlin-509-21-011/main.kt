
import java.net.URL
import java.net.HttpURLConnection

fun parseAndCheckUrl(urlString: String) {
    try {
        val url = URL(urlString)
        
        println("Протокол: ${url.protocol}")
        println("Хост: ${url.host}")
        println("Порт: ${url.port}")
        println("Путь: ${url.path}")
        println("Запрос: ${url.query}")
        
        val connection = url.openConnection() as HttpURLConnection
        connection.requestMethod = "HEAD"
        connection.connectTimeout = 5000
        connection.readTimeout = 5000
        
        val responseCode = connection.responseCode
        
        if (responseCode == HttpURLConnection.HTTP_OK) {
            println("Статус: Доступен ($responseCode)")
        } else {
            println("Статус: Недоступен ($responseCode)")
        }
        
        connection.disconnect()
    } catch (e: Exception) {
        println("Ошибка: ${e.message}")
    }
}

fun main() {
    parseAndCheckUrl("https://example.com/path/to/resource?key=value")
}
