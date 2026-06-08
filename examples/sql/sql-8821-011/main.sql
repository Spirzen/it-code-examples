-- Сравнение производительности с подсказкой и без нее
-- Тест 1: Без подсказки
SET STATISTICS TIME ON;
SET STATISTICS IO ON;

SELECT 
    c.customer_name,
    p.product_category,
    SUM(oi.quantity) AS total_quantity,
    SUM(oi.quantity * oi.unit_price) AS total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
GROUP BY c.customer_name, p.product_category
HAVING SUM(oi.quantity * oi.unit_price) > 10000
ORDER BY total_amount DESC;

SET STATISTICS TIME OFF;
SET STATISTICS IO OFF;

-- Тест 2: С подсказкой
SET STATISTICS TIME ON;
SET STATISTICS IO ON;

SELECT /*+ USE_HASH(c o oi p) PARALLEL(4) */ 
    c.customer_name,
    p.product_category,
    SUM(oi.quantity) AS total_quantity,
    SUM(oi.quantity * oi.unit_price) AS total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
GROUP BY c.customer_name, p.product_category
HAVING SUM(oi.quantity * oi.unit_price) > 10000
ORDER BY total_amount DESC;

SET STATISTICS TIME OFF;
SET STATISTICS IO OFF;
