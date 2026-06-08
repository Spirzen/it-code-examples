val conn = DriverManager.getConnection(
    "jdbc:postgresql://localhost:5432/mydb",
    "user", "password"
)

val stmt = conn.prepareStatement("SELECT id, name FROM users WHERE id = ?")
stmt.setLong(1, 101L)
val rs = stmt.executeQuery()

while (rs.next()) {
    val id = rs.getLong("id")
    val name = rs.getString("name")
    println("$id: $name")
}

rs.close()
stmt.close()
conn.close()
