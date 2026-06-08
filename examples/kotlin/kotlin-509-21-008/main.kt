
import java.io.File

fun scanDirectory(path: String, indent: Int = 0) {
    val file = File(path)
    
    if (!file.exists()) {
        println("Директория не найдена: $path")
        return
    }
    
    if (file.isDirectory) {
        println("${" ".repeat(indent)}📁 ${file.name}/")
        file.listFiles()?.forEach { subFile ->
            scanDirectory(subFile.absolutePath, indent + 2)
        }
    } else {
        println("${" ".repeat(indent)}📄 ${file.name} (${file.length()} байт)")
    }
}

fun main() {
    scanDirectory(".")
}
