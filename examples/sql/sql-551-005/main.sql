WITH сложные_вычисления AS (
    SELECT 
        product_id,
        product_name,
        category_id,
        base_price,
        (base_price * 1.2) AS price_with_tax,
        (base_price * 0.85) AS discounted_price,
        CASE 
            WHEN stock_quantity > 100 THEN 'high'
            WHEN stock_quantity > 50 THEN 'medium'
            ELSE 'low'
        END AS stock_level
    FROM products
    WHERE active = 1
    AND discontinued = 0
)
SELECT 
    sc.product_name,
    c.category_name,
    sc.price_with_tax,
    sc.discounted_price,
    sc.stock_level
FROM сложные_вычисления sc
JOIN categories c ON sc.category_id = c.category_id
WHERE sc.stock_level = 'high'
UNION ALL
SELECT 
    sc.product_name,
    c.category_name,
    sc.price_with_tax,
    sc.discounted_price,
    sc.stock_level
FROM сложные_вычисления sc
JOIN categories c ON sc.category_id = c.category_id
WHERE sc.price_with_tax > 1000
ORDER BY product_name;
