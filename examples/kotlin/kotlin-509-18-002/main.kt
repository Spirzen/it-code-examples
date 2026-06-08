inline fun <T> Connection.useTransaction(block: Connection.() -> T): T {
    return try {
        autoCommit = false
        val result = block()
        commit()
        result
    } catch (e: Exception) {
        rollback()
        throw e
    } finally {
        autoCommit = true
    }
}

inline fun <reified T> ResultSet.mapRow(mapper: ResultSet.() -> T): List<T> {
    val list = mutableListOf<T>()
    while (next()) {
        list += mapper()
    }
    return list
}
