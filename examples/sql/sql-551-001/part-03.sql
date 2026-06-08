WITH рейтинги_продуктов AS (
    SELECT 
        product_id,
        product_name,
        category,
        sales_amount,
        RANK() OVER (PARTITION BY category ORDER BY sales_amount DESC) AS category_rank,
        ROW_NUMBER() OVER (ORDER BY sales_amount DESC) AS global_rank
    FROM products
    WHERE active = 1
)
SELECT 
    product_name,
    category,
    sales_amount,
    category_rank,
    global_rank
FROM рейтинги_продуктов
WHERE category_rank <= 3;
