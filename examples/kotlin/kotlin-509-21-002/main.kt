
import java.io.File
import java.util.Collections

fun sortWords(inputFile: String, outputFile: String) {
    val file = File(inputFile)
    
    if (!file.exists()) {
        println("Файл не найден: $inputFile")
        return
    }

    val content = file.readText()
    val words = content.split("\\s+".toRegex()).filter { it.isNotEmpty() }
    
    Collections.sort(words)
    
    File(outputFile).writeText(words.joinToString("\n"))
    println("Слова успешно сохранены в $outputFile")
}

fun main() {
    sortWords("input.txt", "sorted_output.txt")
}
