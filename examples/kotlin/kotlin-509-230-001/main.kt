class MenuBuilder {
    private val items = mutableListOf<String>()

    fun item(text: String) {
        items += text
    }

    fun build(): List<String> = items.toList()
}

fun menu(block: MenuBuilder.() -> Unit): List<String> =
    MenuBuilder().apply(block).build()

val lunch = menu {
    item("Суп")
    item("Салат")
    item("Чай")
}
