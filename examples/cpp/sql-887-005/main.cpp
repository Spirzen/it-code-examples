#include <SQLiteCpp/SQLiteCpp.h>
#include <iostream>

int main() {
    SQLite::Database db("app.db", SQLite::OPEN_READWRITE | SQLite::OPEN_CREATE);
    db.exec("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT NOT NULL)");

    {
        SQLite::Statement q(db, "INSERT INTO users(name) VALUES (?)");
        q.bind(1, "Anna");
        q.exec();
    }

    SQLite::Statement s(db, "SELECT id, name FROM users");
    while (s.executeStep()) {
        std::cout << s.getColumn(0).getInt() << " " << s.getColumn(1).getString() << "\n";
    }
}
