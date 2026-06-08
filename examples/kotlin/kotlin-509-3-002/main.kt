class HTML {
    fun body(init: BODY.() -> Unit): BODY {
        val body = BODY()
        body.init()
        children.add(body)
        return body
    }
}

fun html(init: HTML.() -> Unit): HTML {
    val html = HTML()
    html.init()
    return html
}
