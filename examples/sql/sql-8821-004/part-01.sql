-- Указание порядка соединения таблиц
SELECT /*+ LEADING(c o oi p) */ 
    c.customer_name,
    p.product_name,
    SUM(oi.quantity) AS total_quantity,
    SUM(oi.quantity * oi.unit_price) AS total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
GROUP BY c.customer_name, p.product_name
HAVING SUM(oi.quantity) > 10
ORDER BY total_amount DESC;
