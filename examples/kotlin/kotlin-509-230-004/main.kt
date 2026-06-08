class QueryBuilder {
    private val parts = mutableListOf<String>()

    fun select(vararg fields: String) {
        parts += "SELECT " + fields.joinToString(", ")
    }

    fun from(table: String) {
        parts += "FROM $table"
    }

    fun build(): String = parts.joinToString(" ")
}

fun query(block: QueryBuilder.() -> Unit): String =
    QueryBuilder().apply(block).build()
