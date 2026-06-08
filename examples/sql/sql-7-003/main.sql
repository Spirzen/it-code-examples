SELECT
    o.order_id,
    c.full_name,
    o.order_date,
    SUM(oi.quantity * oi.unit_price) AS order_total,
    SUM(SUM(oi.quantity * oi.unit_price)) OVER (
        PARTITION BY o.customer_id
        ORDER BY o.order_date, o.order_id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_spent
FROM shop_data.orders o
JOIN shop_data.customers c ON c.customer_id = o.customer_id
JOIN shop_data.order_items oi ON oi.order_id = o.order_id
GROUP BY o.order_id, c.full_name, o.order_date, o.customer_id
ORDER BY c.full_name, o.order_date;
