import java.sql.DriverManager

fun main() {
    DriverManager.getConnection("jdbc:sqlite:app.db").use { conn ->
        conn.createStatement().use { st ->
            st.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        }
        conn.prepareStatement("INSERT INTO users(name) VALUES (?)").use { ps ->
            ps.setString(1, "Anna")
            ps.executeUpdate()
        }
        conn.prepareStatement("SELECT id, name FROM users").use { ps ->
            ps.executeQuery().use { rs ->
                while (rs.next()) println("${rs.getInt("id")} ${rs.getString("name")}")
            }
        }
    }
}
