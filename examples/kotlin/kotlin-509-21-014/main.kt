data class User(val name: String?, val age: Int?)

fun getUserInfo(user: User?) {
    user?.let { u ->
        val displayName = u.name ?: "Неизвестный пользователь"
        val ageDisplay = u.age?.let { age -> "$age лет" } ?: "Возраст не указан"
        
        println("Имя: $displayName")
        println("Возраст: $ageDisplay")
    } ?: run {
        println("Пользователь не найден")
    }
}

fun main() {
    val user1 = User("Алексей", 30)
    val user2 = User(null, null)
    val user3: User? = null
    
    getUserInfo(user1)
    println("---")
    getUserInfo(user2)
    println("---")
    getUserInfo(user3)
}
