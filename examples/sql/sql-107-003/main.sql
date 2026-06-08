CREATE TABLE products (
    product_id   SERIAL PRIMARY KEY,
    sku          VARCHAR(20) NOT NULL,
    name         TEXT NOT NULL,
    category     VARCHAR(30),
    price        NUMERIC(10, 2) NOT NULL,
    stock_qty    INTEGER NOT NULL DEFAULT 0,
    created_at   DATE NOT NULL
);

INSERT INTO products (sku, name, category, price, stock_qty, created_at) VALUES
  ('BOOK-001', 'Алгоритмы', 'Книги', 799.00, 15, '2023-01-15'),
  ('BOOK-002', 'SQL для профессионалов', 'Книги', 1299.00, 0, '2023-02-20'),
  ('GADGET-001', 'USB-кабель', 'Аксессуары', 299.00, 42, '2023-03-10'),
  ('GADGET-002', 'Power bank', 'Аксессуары', 1499.00, 8, '2023-03-12'),
  ('OFFICE-001', 'Блокнот', 'Канцелярия', 99.00, 120, '2023-01-30');
