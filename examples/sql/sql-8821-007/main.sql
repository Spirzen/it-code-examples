-- Оптимизация запроса к таблице фактов продаж
SELECT /*+ 
    PARALLEL(sales_facts 8) 
    PARALLEL(time_dim 2) 
    PARALLEL(product_dim 2) 
    PARALLEL(customer_dim 2) 
    STAR 
    FACT(sales_facts) 
    DIMENSION(time_dim product_dim customer_dim)
*/ 
    td.fiscal_year,
    td.fiscal_quarter,
    pd.product_category,
    pd.product_subcategory,
    cd.customer_region,
    cd.customer_segment,
    COUNT(sf.sale_id) AS transaction_count,
    SUM(sf.quantity) AS total_quantity,
    SUM(sf.sales_amount) AS total_sales,
    AVG(sf.sales_amount) AS avg_transaction_value
FROM sales_facts sf
JOIN time_dimension td ON sf.time_id = td.time_id
JOIN product_dimension pd ON sf.product_id = pd.product_id
JOIN customer_dimension cd ON sf.customer_id = cd.customer_id
WHERE td.fiscal_year = 2025
  AND cd.customer_region IN ('North America', 'Europe')
GROUP BY 
    td.fiscal_year,
    td.fiscal_quarter,
    pd.product_category,
    pd.product_subcategory,
    cd.customer_region,
    cd.customer_segment
HAVING SUM(sf.sales_amount) > 1000000
ORDER BY total_sales DESC;
