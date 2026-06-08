#include <libpq-fe.h>
#include <stdio.h>

int main(void) {
    PGconn *conn = PQconnectdb("host=localhost dbname=app_db user=app_user password=secret");
    if (PQstatus(conn) != CONNECTION_OK) return 1;

    PQexec(conn, "CREATE TABLE IF NOT EXISTS users(id BIGSERIAL PRIMARY KEY, name TEXT NOT NULL)");
    PQexecParams(conn, "INSERT INTO users(name) VALUES ($1)", 1, NULL, (const char*[]){"Anna"}, NULL, NULL, 0);

    PGresult *res = PQexec(conn, "SELECT id, name FROM users");
    int rows = PQntuples(res);
    for (int i = 0; i < rows; i++) {
        printf("%s %s\n", PQgetvalue(res, i, 0), PQgetvalue(res, i, 1));
    }
    PQclear(res);
    PQfinish(conn);
    return 0;
}
