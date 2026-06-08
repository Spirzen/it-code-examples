class ObservableList<T>(
    private val delegate: MutableList<T>
) : MutableList<T> by delegate {
    private val observers = mutableListOf<(List<T>) -> Unit>()

    override fun add(element: T): Boolean {
        val result = delegate.add(element)
        notifyObservers()
        return result
    }

    fun addObserver(observer: (List<T>) -> Unit) {
        observers += observer
    }

    private fun notifyObservers() {
        observers.forEach { it(delegate) }
    }
}
