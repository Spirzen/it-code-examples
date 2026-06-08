-- Оптимизация запроса к звездообразной схеме
SELECT /*+ STAR */ 
    t.time_year,
    p.product_category,
    c.customer_region,
    SUM(f.sales_amount) AS total_sales,
    COUNT(f.sale_id) AS transaction_count
FROM sales_facts f
JOIN time_dimension t ON f.time_id = t.time_id
JOIN product_dimension p ON f.product_id = p.product_id
JOIN customer_dimension c ON f.customer_id = c.customer_id
WHERE t.time_year = 2025
GROUP BY t.time_year, p.product_category, c.customer_region
ORDER BY total_sales DESC;
