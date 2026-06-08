
import java.net.HttpURLConnection
import java.net.URL

fun sendRequest(url: String) {
    val connection = URL(url).openConnection() as HttpURLConnection
    connection.requestMethod = "GET"
    
    val responseCode = connection.responseCode
    val inputStream = connection.inputStream
    val reader = BufferedReader(InputStreamReader(inputStream))
    
    var line: String?
    val response = StringBuilder()
    
    while (reader.readLine().also { line = it } != null) {
        response.append(line)
    }
    
    println("Код ответа: $responseCode")
    println("Ответ сервера: ${response.toString()}")
    
    inputStream.close()
    connection.disconnect()
}

fun main() {
    sendRequest("http://localhost:8080")
}
