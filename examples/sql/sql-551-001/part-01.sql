WITH заказы_клиентов AS (
    SELECT 
        c.customer_id,
        c.customer_name,
        o.order_id,
        o.order_date,
        o.total_amount
    FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    WHERE o.order_date >= '2025-01-01'
)
SELECT 
    customer_name,
    COUNT(order_id) AS количество_заказов,
    SUM(total_amount) AS общая_сумма
FROM заказы_клиентов
GROUP BY customer_name
ORDER BY общая_сумма DESC;
