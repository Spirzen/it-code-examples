
import (

    "database/sql"
    _ "github.com/lib/pq"
)

db, err := sql.Open("postgres", "host=localhost user=timur dbname=universe sslmode=disable")
if err != nil {
    log.Fatal(err)
}
defer db.Close() // хотя для долгоживущего db.Close() обычно не вызывается

if err := db.Ping(); err != nil {
    log.Fatal("failed to connect to DB:", err)
}
