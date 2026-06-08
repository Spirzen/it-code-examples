WITH ranked AS (
    SELECT
        category,
        name,
        price,
        ROW_NUMBER() OVER (
            PARTITION BY category
            ORDER BY price DESC
        ) AS rn
    FROM shop_data.products
)
SELECT category, name, price
FROM ranked
WHERE rn <= 3;
