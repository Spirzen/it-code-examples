interface Printer {
    fun print(message: String)
}

class ConsolePrinter : Printer {
    override fun print(message: String) = println(message)
}

class LoggingPrinter(val impl: Printer) : Printer by impl {
    override fun print(message: String) {
        println("[LOG] $message")
        impl.print(message)
    }
}
