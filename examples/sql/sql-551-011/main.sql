WITH активные_клиенты AS (
    SELECT 
        client_id,
        client_name,
        registration_date,
        last_order_date,
        total_orders
    FROM клиенты
    WHERE статус = 'активный'
    AND last_order_date >= CURRENT_DATE - INTERVAL '180 days'
)
SELECT 
    'премиум' AS сегмент,
    COUNT(*) AS количество,
    SUM(total_orders) AS общее_количество_заказов
FROM активные_клиенты
WHERE total_orders > 20

UNION ALL

SELECT 
    'стандарт' AS сегмент,
    COUNT(*) AS количество,
    SUM(total_orders) AS общее_количество_заказов
FROM активные_клиенты
WHERE total_orders BETWEEN 5 AND 20

UNION ALL

SELECT 
    'начинающие' AS сегмент,
    COUNT(*) AS количество,
    SUM(total_orders) AS общее_количество_заказов
FROM активные_клиенты
WHERE total_orders < 5;
