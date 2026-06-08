import java.sql.DriverManager

fun main() {
    DriverManager.getConnection(
        "jdbc:postgresql://localhost:5432/app_db", "app_user", "secret"
    ).use { conn ->
        conn.createStatement().use { st ->
            st.execute("CREATE TABLE IF NOT EXISTS users(id BIGSERIAL PRIMARY KEY, name TEXT NOT NULL)")
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
