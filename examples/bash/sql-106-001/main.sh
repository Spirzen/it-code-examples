# Тестовая база и данные
createdb shop_backup_test
psql shop_backup_test -c "
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT,
    price NUMERIC
);
INSERT INTO products (name, price) VALUES ('Товар А', 100.00);
"

pg_dump -Fc -f shop_backup.dump shop_backup_test
createdb shop_restored
pg_restore -d shop_restored shop_backup.dump
psql shop_restored -c "SELECT * FROM products;"
