data class Ticket(val id: Int, val owner: String?)

val tickets = listOf(
    Ticket(1, "Ann"),
    Ticket(2, null),
    Ticket(3, "Bob"),
    Ticket(4, "Ann")
)

val uniqueOwners = tickets
    .mapNotNull { it.owner }
    .map { it.trim() }
    .filter { it.isNotBlank() }
    .toSet()
    .sorted()

println(uniqueOwners) // [Ann, Bob]
