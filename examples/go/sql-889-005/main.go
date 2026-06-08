package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db, _ := sql.Open("mysql", "app_user:secret@tcp(localhost:3306)/app_db?parseTime=true")
	defer db.Close()

	db.Exec(`CREATE TABLE IF NOT EXISTS users(id BIGINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL) ENGINE=InnoDB`)
	db.Exec(`INSERT INTO users(name) VALUES (?)`, "Anna")

	rows, _ := db.Query(`SELECT id, name FROM users`)
	defer rows.Close()
	for rows.Next() {
		var id int64
		var name string
		rows.Scan(&id, &name)
		fmt.Println(id, name)
	}
}
