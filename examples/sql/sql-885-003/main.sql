SELECT 
    o.order_number,
    recent_orders.avg_amount,
    o.total_amount
FROM orders o
JOIN (
    SELECT 
        user_id,
        AVG(total_amount) AS avg_amount
    FROM orders
    WHERE status = 'delivered'
    GROUP BY user_id
) recent_orders ON o.user_id = recent_orders.user_id
WHERE o.total_amount > recent_orders.avg_amount;
