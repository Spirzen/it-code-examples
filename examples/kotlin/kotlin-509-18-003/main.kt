class User(id: EntityID<Long>) : LongEntity(id) {
    companion object : LongEntityClass<User>(Users)

    var name by Users.name
    var email by Users.email
    var createdAt by Users.createdAt
}

// Использование
val user = User.new {
    name = "Анна"
    email = "anna@example.com"
}
user.refresh() // синхронизация с БД
