
import groovy.sql.Sql

def sql = Sql.newInstance(url, user, pass, driver)
def books = [
    [title: "Groovy in Action", author: "D. Konig", price: 50G, active: true],
    [title: "Legacy Java",      author: "Team",     price: 35G, active: false]
]

sql.withTransaction {
    books.findAll { it.active }.each { b ->
        sql.executeInsert(
            "INSERT INTO books(title, author, price) VALUES (?, ?, ?)",
            [b.title, b.author, b.price]
        )
    }
}
sql.close()
