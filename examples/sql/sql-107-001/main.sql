SELECT name, price
FROM products
WHERE category = 'Книги'
  AND stock_qty > 0
  AND price BETWEEN 300 AND 1000;

SELECT name FROM products WHERE name LIKE 'А%';

SELECT name, price, stock_qty
FROM products
WHERE (category = 'Аксессуары' AND price < 1000)
   OR stock_qty = 0;

-- NULL: только IS NULL / IS NOT NULL
SELECT name, price FROM products WHERE price IS NULL;
SELECT name, price FROM products WHERE price IS NOT NULL;
