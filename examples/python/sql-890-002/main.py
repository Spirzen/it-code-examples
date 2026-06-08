import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};Server=localhost,1433;Database=app_db;UID=app_user;PWD=secret;Encrypt=yes;TrustServerCertificate=yes;"
)
cur = conn.cursor()

cur.execute("""
IF OBJECT_ID('dbo.Users','U') IS NULL
CREATE TABLE dbo.Users(
    Id BIGINT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(255) NOT NULL
)
""")

cur.execute("INSERT INTO dbo.Users(Name) VALUES (?)", ("Anna",))
conn.commit()

cur.execute("SELECT Id, Name FROM dbo.Users")
for row in cur.fetchall():
    print(row[0], row[1])

cur.execute("UPDATE dbo.Users SET Name=? WHERE Id=?", ("Ann", 1))
cur.execute("DELETE FROM dbo.Users WHERE Id=?", (1,))
conn.commit()
conn.close()
