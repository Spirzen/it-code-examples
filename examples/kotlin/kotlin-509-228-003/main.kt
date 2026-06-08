suspend fun <T> retryIo(
    attempts: Int = 3,
    block: suspend () -> T
): T {
    var lastError: Throwable? = null
    repeat(attempts) { index ->
        try {
            return block()
        } catch (e: java.io.IOException) {
            lastError = e
            if (index < attempts - 1) kotlinx.coroutines.delay(300L * (index + 1))
        }
    }
    throw lastError ?: IllegalStateException("Не удалось выполнить запрос")
}
