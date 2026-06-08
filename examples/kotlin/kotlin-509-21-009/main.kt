
import java.io.File
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun createBackup(sourceDir: String, backupDir: String) {
    val source = File(sourceDir)
    val timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd_HH-mm-ss"))
    val targetDir = File("$backupDir/backup_$timestamp")
    
    if (!source.exists() || !source.isDirectory) {
        println("Источник не существует или не является директорией: $sourceDir")
        return
    }
    
    targetDir.mkdirs()
    
    source.listFiles()?.forEach { file ->
        if (file.isFile) {
            val targetFile = File(targetDir, file.name)
            file.copyTo(targetFile, overwrite = true)
            println("Скопировано: ${file.name}")
        }
    }
    
    println("Резервное копирование завершено в $targetDir")
}

fun main() {
    createBackup("./data", "./backups")
}
