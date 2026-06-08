-- Явное указание таблиц фактов и измерений
SELECT /*+ FACT(f) DIMENSION(t p c) */ 
    t.time_quarter,
    p.product_name,
    SUM(f.quantity) AS total_quantity,
    SUM(f.sales_amount) AS total_sales
FROM sales_facts f
JOIN time_dimension t ON f.time_id = t.time_id
JOIN product_dimension p ON f.product_id = p.product_id
JOIN customer_dimension c ON f.customer_id = c.customer_id
WHERE t.time_year = 2025
  AND c.customer_region = 'North America'
GROUP BY t.time_quarter, p.product_name
HAVING SUM(f.sales_amount) > 10000
ORDER BY total_sales DESC;
