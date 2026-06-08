import java.sql.*;

try (Connection conn = DriverManager.getConnection(
        "jdbc:sqlserver://localhost:1433;databaseName=app_db;user=app_user;password=secret;encrypt=true;trustServerCertificate=true;")) {

    try (Statement st = conn.createStatement()) {
        st.execute("""
            IF OBJECT_ID('dbo.Users','U') IS NULL
            CREATE TABLE dbo.Users(
                Id BIGINT IDENTITY(1,1) PRIMARY KEY,
                Name NVARCHAR(255) NOT NULL
            )
        """);
    }

    try (PreparedStatement ins = conn.prepareStatement("INSERT INTO dbo.Users(Name) VALUES (?)")) {
        ins.setString(1, "Anna");
        ins.executeUpdate();
    }

    try (PreparedStatement sel = conn.prepareStatement("SELECT Id, Name FROM dbo.Users");
         ResultSet rs = sel.executeQuery()) {
        while (rs.next()) {
            System.out.println(rs.getLong("Id") + " " + rs.getString("Name"));
        }
    }
}
