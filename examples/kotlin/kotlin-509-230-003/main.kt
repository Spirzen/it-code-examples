class RouteConfig {
    val routes = mutableListOf<Pair<String, () -> Unit>>()

    fun get(path: String, handler: () -> Unit) {
        routes += path to handler
    }
}

fun routing(block: RouteConfig.() -> Unit): RouteConfig =
    RouteConfig().apply(block)

val app = routing {
    get("/health") { println("ok") }
    get("/version") { println("1.0") }
}
