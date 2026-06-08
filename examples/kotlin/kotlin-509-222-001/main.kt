
import kotlinx.coroutines.*

suspend fun fetchTitle(): String {
    delay(100)
    return "Kotlin"
}

fun main() = runBlocking {
    launch {
        println("A: ${fetchTitle()}")
    }
    launch {
        println("B: ${fetchTitle()}")
    }
}
