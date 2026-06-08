import java.sql.*;

try (Connection conn = DriverManager.getConnection("jdbc:sqlite:app.db")) {
    try (Statement st = conn.createStatement()) {
        st.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """);
    }

    try (PreparedStatement ins = conn.prepareStatement(
            "INSERT INTO users(name) VALUES (?)")) {
        ins.setString(1, "Anna");
        ins.executeUpdate();
    }

    try (PreparedStatement sel = conn.prepareStatement(
            "SELECT id, name FROM users");
         ResultSet rs = sel.executeQuery()) {
        while (rs.next()) {
            System.out.println(rs.getInt("id") + " " + rs.getString("name"));
        }
    }
}
