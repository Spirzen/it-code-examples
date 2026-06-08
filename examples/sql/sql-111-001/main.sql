CREATE SCHEMA IF NOT EXISTS shop_data;

CREATE TABLE IF NOT EXISTS shop_data.customers (
    customer_id SERIAL PRIMARY KEY,
    full_name   TEXT NOT NULL,
    email       TEXT UNIQUE,
    city        TEXT,
    created_at  TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS shop_data.products (
    product_id SERIAL PRIMARY KEY,
    name       TEXT NOT NULL,
    price      NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    category   TEXT
);

CREATE TABLE IF NOT EXISTS shop_data.orders (
    order_id    SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES shop_data.customers(customer_id),
    order_date  DATE DEFAULT CURRENT_DATE,
    status      TEXT DEFAULT 'new'
);

CREATE TABLE IF NOT EXISTS shop_data.order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id      INT NOT NULL REFERENCES shop_data.orders(order_id),
    product_id    INT NOT NULL REFERENCES shop_data.products(product_id),
    quantity      INT NOT NULL CHECK (quantity > 0),
    unit_price    NUMERIC(10, 2) NOT NULL,
    UNIQUE (order_id, product_id)
);

-- Демо-данные
INSERT INTO shop_data.customers (full_name, email, city) VALUES
  ('Анна Иванова', 'anna@example.com', 'Москва'),
  ('Борис Петров', 'boris@example.com', 'СПб')
ON CONFLICT DO NOTHING;

INSERT INTO shop_data.products (name, price, category) VALUES
  ('SQL для профессионалов', 1299.00, 'Книги'),
  ('USB-кабель', 299.00, 'Аксессуары')
ON CONFLICT DO NOTHING;
