package main

import (
	"context"
	"fmt"
	"github.com/jackc/pgx/v5"
)

func main() {
	ctx := context.Background()
	conn, _ := pgx.Connect(ctx, "postgres://app_user:secret@localhost:5432/app_db")
	defer conn.Close(ctx)

	conn.Exec(ctx, `CREATE TABLE IF NOT EXISTS users(id BIGSERIAL PRIMARY KEY, name TEXT NOT NULL)`)
	conn.Exec(ctx, `INSERT INTO users(name) VALUES ($1)`, "Anna")

	rows, _ := conn.Query(ctx, `SELECT id, name FROM users`)
	defer rows.Close()
	for rows.Next() {
		var id int64
		var name string
		rows.Scan(&id, &name)
		fmt.Println(id, name)
	}
}
