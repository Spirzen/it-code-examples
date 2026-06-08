class User private constructor(
    val id: UserId,
    val name: String,
    val email: Email
) {
    companion object {
        fun create(id: String, name: String, email: String): Result<User, Error> {
            return when {
                name.isBlank() -> Error.InvalidName
                !email.contains('@') -> Error.InvalidEmail
                else -> Success(User(UserId(id), name, Email(email)))
            }
        }
    }
}
