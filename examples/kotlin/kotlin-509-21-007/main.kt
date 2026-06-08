
import java.net.HttpURLConnection
import java.net.URL
import java.io.OutputStream
import java.nio.charset.StandardCharsets

fun sendHttpRequest(method: String, url: String, headers: Map<String, String>, body: String?) {
    val connection = URL(url).openConnection() as HttpURLConnection
    connection.requestMethod = method
    
    headers.forEach { (key, value) ->
        connection.setRequestProperty(key, value)
    }
    
    if (body != null && method in listOf("POST", "PUT")) {
        connection.doOutput = true
        OutputStream(connection.outputStream).use { out ->
            out.write(body.toByteArray(StandardCharsets.UTF_8))
        }
    }
    
    val responseCode = connection.responseCode
    val inputStream = connection.inputStream
    val reader = BufferedReader(InputStreamReader(inputStream))
    
    val response = StringBuilder()
    var line: String?
    while (reader.readLine().also { line = it } != null) {
        response.append(line)
    }
    
    println("Метод: $method")
    println("URL: $url")
    println("Код ответа: $responseCode")
    println("Тело ответа: ${response.toString()}")
    
    inputStream.close()
    connection.disconnect()
}

fun main() {
    val headers = mapOf(
        "Content-Type" to "application/json",
        "Accept" to "application/json"
    )
    val body = """{"name": "Timur", "role": "Developer"}"""
    
    sendHttpRequest("POST", "https://jsonplaceholder.typicode.com/posts", headers, body)
}
