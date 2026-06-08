type
  User = object
    name: string
    age: int
    email: string
    isActive: bool

proc isValidUser(u: User): bool =
  u.name.len > 0 and
  u.age >= 18 and
  u.email.contains('@') and
  u.isActive

let user = User(name: "Алексей", age: 25, email: "alex@example.com", isActive: true)
echo "Пользователь валиден: ", isValidUser(user)
