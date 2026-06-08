import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.*
import java.io.IOException

fun unstableApi(): Flow<String> = flow {
    emit(fetchRemoteValue()) // может бросить IOException
}.retryWhen { cause, attempt ->
    if (cause is IOException && attempt < 3) {
        delay(200L * (attempt + 1))
        true
    } else {
        false
    }
}
