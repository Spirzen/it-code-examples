@DslMarker
annotation class HtmlTagMarker

@HtmlTagMarker
abstract class Tag {
    protected val children = mutableListOf<Tag>()
}

@HtmlTagMarker
class Body : Tag() {
    fun p(text: String) { /* добавить параграф */ }
}

@HtmlTagMarker
class Html : Tag() {
    fun body(block: Body.() -> Unit) {
        val b = Body()
        b.block()
        children += b
    }
}

fun html(block: Html.() -> Unit): Html = Html().apply(block)
