WITH 
category_stats AS (
    SELECT 
        category_id,
        COUNT(*) AS product_count,
        AVG(price) AS avg_price
    FROM products
    GROUP BY category_id
),
top_categories AS (
    SELECT category_id
    FROM category_stats
    WHERE product_count >= 5 AND avg_price > 1000
)
SELECT 
    p.name,
    p.price,
    cs.product_count,
    cs.avg_price
FROM products p
JOIN category_stats cs ON p.category_id = cs.category_id
JOIN top_categories tc ON p.category_id = tc.category_id
ORDER BY p.price DESC;
