def name = 'Alice'
println "Hello, $name"

def greet = { who -> println "Hello, $who" }
greet('Bob')

def list = [1, 2, 3]
def map = [name: 'John', age: 30]

new File('test.txt').eachLine { line ->
    println line
}

try {
    1 / 0
} catch (e) {
    println "Error: ${e.message}"
}
