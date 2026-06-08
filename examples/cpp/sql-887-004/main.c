#include <sqlite3.h>
#include <stdio.h>

int main(void) {
    sqlite3 *db = NULL;
    if (sqlite3_open("app.db", &db) != SQLITE_OK) return 1;

    sqlite3_exec(db, "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT NOT NULL);", 0, 0, 0);

    sqlite3_stmt *stmt = NULL;
    sqlite3_prepare_v2(db, "INSERT INTO users(name) VALUES (?);", -1, &stmt, NULL);
    sqlite3_bind_text(stmt, 1, "Anna", -1, SQLITE_TRANSIENT);
    sqlite3_step(stmt);
    sqlite3_finalize(stmt);

    sqlite3_prepare_v2(db, "SELECT id, name FROM users;", -1, &stmt, NULL);
    while (sqlite3_step(stmt) == SQLITE_ROW) {
        int id = sqlite3_column_int(stmt, 0);
        const unsigned char *name = sqlite3_column_text(stmt, 1);
        printf("%d %s\n", id, name);
    }
    sqlite3_finalize(stmt);
    sqlite3_close_v2(db);
    return 0;
}
