
import java.security.SecureRandom

fun generatePassword(length: Int): String {
    val chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
    val random = SecureRandom()
    return (1..length)
        .map { chars[random.nextInt(chars.length)] }
        .joinToString("")
}

fun main() {
    val passwordLength = 16
    val password = generatePassword(passwordLength)
    println("Сгенерированный пароль: $password")
}
