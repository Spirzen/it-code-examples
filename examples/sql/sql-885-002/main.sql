SELECT 
    category_stats.name,
    category_stats.product_count,
    category_stats.avg_price
FROM (
    SELECT 
        c.name,
        COUNT(p.id) AS product_count,
        AVG(p.price) AS avg_price
    FROM categories c
    LEFT JOIN products p ON c.id = p.category_id
    GROUP BY c.id, c.name
) AS category_stats
WHERE category_stats.product_count > 5;
