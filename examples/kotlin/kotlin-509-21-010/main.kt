
import java.io.File

fun checkDiskSpace(path: String) {
    val root = File(path)
    val totalSpace = root.totalSpace
    val freeSpace = root.freeSpace
    val usableSpace = root.usableSpace
    
    val usedSpace = totalSpace - usableSpace
    
    println("Диск: $path")
    println("Всего места: ${(totalSpace / (1024 * 1024 * 1024)).toInt()} ГБ")
    println("Свободно: ${(freeSpace / (1024 * 1024 * 1024)).toInt()} ГБ")
    println("Использовано: ${(usedSpace / (1024 * 1024 * 1024)).toInt()} ГБ")
    println("Занято: %.2f%%".format((usedSpace.toDouble() / totalSpace.toDouble()) * 100))
}

fun main() {
    checkDiskSpace("/")
    checkDiskSpace("C:/") // Для Windows
}
