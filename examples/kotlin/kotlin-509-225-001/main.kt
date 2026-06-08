data class Order(val region: String, val amount: Int)

val orders = listOf(
    Order("EU", 100),
    Order("EU", 50),
    Order("US", 200)
)

val byRegion = orders.groupBy { it.region }
// Map: "EU" -> [Order(...), Order(...)], "US" -> [...]

val totalByRegion = orders.groupingBy { it.region }
    .fold(0) { acc, order -> acc + order.amount }
// Map: "EU" -> 150, "US" -> 200

val userById = users.associateBy { it.name }  // ключ — name
