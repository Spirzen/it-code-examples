SELECT
    product_id,
    name,
    category,
    price,
    stock_qty
FROM products
WHERE
    category IN ('Книги', 'Аксессуары')
    AND price BETWEEN 100 AND 1500
    AND stock_qty > 0
ORDER BY
    category ASC,
    price DESC;
