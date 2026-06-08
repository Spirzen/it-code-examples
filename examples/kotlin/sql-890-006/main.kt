import java.sql.DriverManager

fun main() {
    DriverManager.getConnection(
        "jdbc:sqlserver://localhost:1433;databaseName=app_db;user=app_user;password=secret;encrypt=true;trustServerCertificate=true;"
    ).use { conn ->
        conn.createStatement().use { st ->
            st.execute(
                "IF OBJECT_ID('dbo.Users','U') IS NULL CREATE TABLE dbo.Users(Id BIGINT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(255) NOT NULL)"
            )
        }
        conn.prepareStatement("INSERT INTO dbo.Users(Name) VALUES (?)").use { ps ->
            ps.setString(1, "Anna")
            ps.executeUpdate()
        }
        conn.prepareStatement("SELECT Id, Name FROM dbo.Users").use { ps ->
            ps.executeQuery().use { rs ->
                while (rs.next()) println("${rs.getLong("Id")} ${rs.getString("Name")}")
            }
        }
    }
}
