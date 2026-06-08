-- Запрос с документированными подсказками
SELECT 
    /*+ 
        PARALLEL(sales 8)           -- Использовать 8 параллельных процессов для обработки большой таблицы продаж
        PARALLEL(customers 2)       -- Использовать 2 параллельных процесса для таблицы клиентов
        USE_HASH(sales customers)   -- Хеш-соединение эффективно для больших таблиц без селективных индексов
        NO_INDEX(sales)             -- Запретить использование индексов на таблице продаж из-за низкой селективности условий
    */
    c.customer_segment,
    c.customer_region,
    COUNT(s.sale_id) AS transaction_count,
    SUM(s.amount) AS total_sales,
    AVG(s.amount) AS avg_transaction_value
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
WHERE s.sale_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 YEAR)
  AND c.active_status = 'Y'
GROUP BY c.customer_segment, c.customer_region
HAVING SUM(s.amount) > 100000
ORDER BY total_sales DESC;
