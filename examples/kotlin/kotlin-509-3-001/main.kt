class Outer {
    private val bar: Int = 1

    class Nested {
        fun foo() = 2
    }

    inner class Inner {
        fun foo() = bar // доступ к bar
    }
}

val nested = Outer.Nested().foo() // 2
val inner = Outer().Inner().foo() // 1
