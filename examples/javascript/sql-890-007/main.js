import sql from "mssql";

const pool = await sql.connect({
  user: "app_user",
  password: "secret",
  server: "localhost",
  port: 1433,
  database: "app_db",
  options: { encrypt: true, trustServerCertificate: true },
});

await pool.request().query(`
IF OBJECT_ID('dbo.Users','U') IS NULL
CREATE TABLE dbo.Users(
  Id BIGINT IDENTITY(1,1) PRIMARY KEY,
  Name NVARCHAR(255) NOT NULL
)`);

await pool.request().input("name", sql.NVarChar, "Anna")
  .query("INSERT INTO dbo.Users(Name) VALUES (@name)");

const result = await pool.request().query("SELECT Id, Name FROM dbo.Users");
for (const row of result.recordset) {
  console.log(row.Id, row.Name);
}

await pool.close();
