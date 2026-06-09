class User(private val username: String, private val password: String) {
    private var loggedIn = false

    fun login(password: String) {
        if (password == this.password) {
            loggedIn = true
            println("Добро пожаловать, $username!")
        } else {
            println("Ошибка: неверный пароль")
        }
    }

    fun logout() {
        loggedIn = false
        println("$username вышел из системы")
    }

    fun postMessage(text: String) {
        if (!loggedIn) {
            println("Сначала войдите в систему")
            return
        }
        println("Сообщение опубликовано: $text")
    }
}

fun main() {
    val user = User("alex", "secret123")
    user.postMessage("Привет!")
    user.login("wrong")
    user.login("secret123")
    user.postMessage("Привет, мир!")
    user.logout()
    user.postMessage("Ещё одно сообщение")
}
