class Repo {
    private val scope = CoroutineScope(SupervisorJob() + Dispatchers.IO)

    fun refresh(onDone: (String) -> Unit) {
        scope.launch {
            val data = fetchTitle()
            withContext(Dispatchers.Main) {
                onDone(data)
            }
        }
    }

    fun close() {
        scope.cancel()
    }
}
