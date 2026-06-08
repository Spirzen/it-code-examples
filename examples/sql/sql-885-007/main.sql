SELECT 
    user_id,
    created_at,
    total_amount,
    FIRST_VALUE(total_amount) OVER (
        PARTITION BY user_id 
        ORDER BY created_at
    ) AS first_order_amount,
    LAST_VALUE(total_amount) OVER (
        PARTITION BY user_id 
        ORDER BY created_at
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_order_amount
FROM orders;
