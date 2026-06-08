
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

fun counter(): Flow<Int> = flow {
    for (i in 1..5) {
        delay(200)
        emit(i)
    }
}

suspend fun main() {
    counter().collect { println(it) }
}
