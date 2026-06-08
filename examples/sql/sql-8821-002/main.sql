-- Параллельное сканирование таблицы с 8 процессами
SELECT /*+ PARALLEL(sales 8) */ 
    region,
    SUM(amount) AS total_sales,
    COUNT(*) AS transaction_count
FROM sales
WHERE sale_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 YEAR)
GROUP BY region
ORDER BY total_sales DESC;

-- Параллельное соединение двух таблиц
SELECT /*+ PARALLEL(s 4) PARALLEL(c 4) */ 
    c.customer_name,
    SUM(s.amount) AS total_purchases,
    COUNT(s.sale_id) AS purchase_count
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
WHERE s.sale_date >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
GROUP BY c.customer_id, c.customer_name
HAVING SUM(s.amount) > 10000
ORDER BY total_purchases DESC;
