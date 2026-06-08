interface Logger {
    fun log(message: String)
}

class ConsoleLogger : Logger {
    override fun log(message: String) = println("[INFO] $message")
}

class Service(logger: Logger) : Logger by logger {
    fun process() {
        logger.log("Starting...")
        // ...
        log("Finished.") // делегирует вызов logger.log()
    }
}
