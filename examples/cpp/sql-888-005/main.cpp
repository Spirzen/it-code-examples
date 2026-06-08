#include <pqxx/pqxx>
#include <iostream>

int main() {
    pqxx::connection conn("host=localhost port=5432 dbname=app_db user=app_user password=secret");
    pqxx::work tx(conn);

    tx.exec("CREATE TABLE IF NOT EXISTS users(id BIGSERIAL PRIMARY KEY, name TEXT NOT NULL)");
    tx.exec_params("INSERT INTO users(name) VALUES ($1)", "Anna");

    pqxx::result r = tx.exec("SELECT id, name FROM users");
    for (auto row : r) {
        std::cout << row["id"].as<long>() << " " << row["name"].as<std::string>() << "\n";
    }
    tx.commit();
}
