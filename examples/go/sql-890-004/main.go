package main

import (
	"database/sql"
	"fmt"
	_ "github.com/microsoft/go-mssqldb"
)

func main() {
	db, _ := sql.Open("sqlserver", "sqlserver://app_user:secret@localhost:1433?database=app_db&encrypt=disable")
	defer db.Close()

	db.Exec(`IF OBJECT_ID('dbo.Users','U') IS NULL CREATE TABLE dbo.Users(Id BIGINT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(255) NOT NULL)`)
	db.Exec(`INSERT INTO dbo.Users(Name) VALUES (@p1)`, "Anna")

	rows, _ := db.Query(`SELECT Id, Name FROM dbo.Users`)
	defer rows.Close()
	for rows.Next() {
		var id int64
		var name string
		rows.Scan(&id, &name)
		fmt.Println(id, name)
	}
}
