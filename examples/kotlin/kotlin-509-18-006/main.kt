interface UserRepository {
    suspend fun findById(id: Long): User?
    suspend fun save(user: User)
}

class PostgresUserRepository(val db: org.jetbrains.exposed.sql.Database) : UserRepository { ... }
class CachedUserRepository(
    private val cache: RedisClient,
    private val delegate: UserRepository
) : UserRepository {
    override suspend fun findById(id: Long): User? {
        val cached = cache.get("user:$id")?.let { Json.decodeFromString<User>(it) }
        return cached ?: delegate.findById(id).also { u ->
            if (u != null) cache.set("user:$id", Json.encodeToString(u))
        }
    }
}
