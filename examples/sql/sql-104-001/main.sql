-- Диалект: PostgreSQL
CREATE TABLE clients (
    client_id   SERIAL PRIMARY KEY,
    full_name   TEXT NOT NULL,
    phone       TEXT,
    city        TEXT
);

CREATE TABLE products (
    product_code VARCHAR(20) PRIMARY KEY,
    name         TEXT NOT NULL,
    category     TEXT,
    price        NUMERIC(10, 2) NOT NULL
);

CREATE TABLE orders (
    order_id    SERIAL PRIMARY KEY,
    order_date  DATE NOT NULL DEFAULT CURRENT_DATE,
    client_id   INT NOT NULL REFERENCES clients(client_id)
);

CREATE TABLE order_lines (
    order_id      INT NOT NULL REFERENCES orders(order_id),
    product_code  VARCHAR(20) NOT NULL REFERENCES products(product_code),
    quantity      INT NOT NULL CHECK (quantity > 0),
    PRIMARY KEY (order_id, product_code)
);
