
import io.ktor.client.call.*
import io.ktor.client.request.*
import io.ktor.http.*
import kotlinx.coroutines.runBlocking

suspend fun demo(client: HttpClient) {
    val health: Map<String, String> = client.get("http://127.0.0.1:8080/health").body()
    println(health)

    val notes: List<Note> = client.get("http://127.0.0.1:8080/notes").body()
    println("Заметок: ${notes.size}")

    val created: Note = client.post("http://127.0.0.1:8080/notes") {
        contentType(ContentType.Application.Json)
        setBody(NoteCreate("Из клиента"))
    }.body()
    println("Создано: ${created.id} — ${created.text}")
}

fun main() = runBlocking {
    val client = HttpClient(CIO) {
        install(ContentNegotiation) { json() }
    }
    try {
        demo(client)
    } finally {
        client.close()
    }
}
