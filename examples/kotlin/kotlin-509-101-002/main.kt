class UserRepository(
    private val ioDispatcher: CoroutineDispatcher = Dispatchers.IO
) {
    private val scope = CoroutineScope(SupervisorJob() + ioDispatcher)

    fun loadUsers(): Job = scope.launch {
        val users = withContext(ioDispatcher) {
            api.fetchUsers()
        }
        cache.save(users)
    }

    fun close() {
        scope.cancel()
    }
}
