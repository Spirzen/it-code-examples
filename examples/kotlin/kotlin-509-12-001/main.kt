@Serializable
data class UserDto(
    val id: Long,
    val name: String?,
    val email: String?
)

data class User(
    val id: Long,
    val name: String,
    val email: String
)

fun UserDto.toDomain(): User =
    User(
        id = id,
        name = name ?: "Без имени",
        email = email ?: "unknown@example.com"
    )
