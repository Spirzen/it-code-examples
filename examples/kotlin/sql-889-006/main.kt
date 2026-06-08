import java.sql.DriverManager

fun main() {
    DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/app_db", "app_user", "secret"
    ).use { conn ->
        conn.createStatement().use { st ->
            st.execute(
                "CREATE TABLE IF NOT EXISTS users(id BIGINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL) ENGINE=InnoDB"
            )
        }
        conn.prepareStatement("INSERT INTO users(name) VALUES (?)").use { ps ->
            ps.setString(1, "Anna")
            ps.executeUpdate()
        }
        conn.prepareStatement("SELECT id, name FROM users").use { ps ->
            ps.executeQuery().use { rs ->
                while (rs.next()) println("${rs.getLong("id")} ${rs.getString("name")}")
            }
        }
    }
}
