
import java.lang.ProcessBuilder
import java.io.BufferedReader
import java.io.InputStreamReader

fun listProcesses() {
    val command = if (System.getProperty("os.name").contains("win")) {
        arrayOf("cmd.exe", "/c", "tasklist")
    } else {
        arrayOf("ps", "-aux")
    }
    
    val processBuilder = ProcessBuilder(*command)
    val process = processBuilder.start()
    
    BufferedReader(InputStreamReader(process.inputStream)).use { reader ->
        var line: String?
        while (reader.readLine().also { line = it } != null) {
            println(line)
        }
    }
    
    process.waitFor()
}

fun main() {
    listProcesses()
}
