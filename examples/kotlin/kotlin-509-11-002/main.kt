val Users = object : Table() {
    val id = integer("id").autoIncrement()
    val name = varchar("name", 50)
    val email = varchar("email", 100).uniqueIndex()
}

transaction {
    val id = Users.insert {
        it[name] = "Alice"
        it[email] = "alice@example.com"
    } get Users.id

    val user = Users.select { Users.id eq id }.firstOrNull()
}
