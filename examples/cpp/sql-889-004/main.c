#include <mysql.h>
#include <stdio.h>

int main(void) {
    MYSQL *conn = mysql_init(NULL);
    if (!mysql_real_connect(conn, "localhost", "app_user", "secret", "app_db", 3306, NULL, 0)) return 1;

    mysql_query(conn, "CREATE TABLE IF NOT EXISTS users(id BIGINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL) ENGINE=InnoDB");
    mysql_query(conn, "INSERT INTO users(name) VALUES ('Anna')");
    mysql_query(conn, "SELECT id, name FROM users");

    MYSQL_RES *res = mysql_store_result(conn);
    MYSQL_ROW row;
    while ((row = mysql_fetch_row(res))) {
        printf("%s %s\n", row[0], row[1]);
    }
    mysql_free_result(res);
    mysql_close(conn);
    return 0;
}
