class Foo {
    def doSomething() {
        def data = [name: 'James', location: 'London']
        for (e in data) {
            println("entry ${e.key} is ${e.value}")
        }
    }

    def closureExample(collection) {
        collection.each { println("value ${it}") }
    }

    static void main(args) {
        def values = [1, 2, 3, 'abc']
        def foo = new Foo()
        foo.closureExample(values)
        foo.doSomething()
    }
}
