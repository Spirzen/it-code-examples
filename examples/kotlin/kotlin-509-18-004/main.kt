// INSERT
database.insert(Users) {
    set(Users.name, "Мария")
    set(Users.email, "maria@example.com")
    set(Users.createdAt, LocalDateTime.now())
}

// UPDATE
database.update(Users) {
    set(Users.email, "new@example.com")
    where { Users.id eq 42 }
}

// DELETE
database.delete(Users) { Users.id eq 42 }
