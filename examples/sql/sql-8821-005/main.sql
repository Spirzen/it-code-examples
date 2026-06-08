-- Материализация общего табличного выражения
WITH /*+ MATERIALIZE */ продажи_за_год AS (
    SELECT 
        customer_id,
        COUNT(*) AS order_count,
        SUM(order_total) AS total_spent,
        MAX(order_date) AS last_order_date
    FROM orders
    WHERE order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 YEAR)
    GROUP BY customer_id
)
SELECT 
    c.customer_name,
    c.customer_segment,
    py.order_count,
    py.total_spent,
    py.last_order_date,
    RANK() OVER (PARTITION BY c.customer_segment ORDER BY py.total_spent DESC) AS segment_rank
FROM customers c
JOIN продажи_за_год py ON c.customer_id = py.customer_id
WHERE py.total_spent > 10000
ORDER BY py.total_spent DESC;
