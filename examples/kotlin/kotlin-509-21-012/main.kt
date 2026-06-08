
import java.time.LocalDate
import java.time.format.DateTimeFormatter

fun convertDate(dateString: String, inputFormat: String, outputFormats: List<String>) {
    val inputFormatter = DateTimeFormatter.ofPattern(inputFormat)
    val date = LocalDate.parse(dateString, inputFormatter)
    
    outputFormats.forEach { format ->
        val formatter = DateTimeFormatter.ofPattern(format)
        val converted = date.format(formatter)
        println("$format -> $converted")
    }
}

fun main() {
    val inputDate = "2025-11-01"
    val formats = listOf("dd/MM/yyyy", "MMMM dd, yyyy", "yyyy.MM.dd")
    
    convertDate(inputDate, "yyyy-MM-dd", formats)
}
