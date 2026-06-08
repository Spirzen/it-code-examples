interface Notifier {
    fun send(message: String)
}

class EmailNotifier : Notifier {
    override fun send(message: String) = println("Email: $message")
}

class AuditNotifier(private val delegate: Notifier) : Notifier by delegate {
    override fun send(message: String) {
        println("AUDIT -> ${System.currentTimeMillis()}")
        delegate.send(message)
    }
}
