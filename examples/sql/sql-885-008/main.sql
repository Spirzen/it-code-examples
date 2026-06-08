CREATE OR REPLACE FUNCTION get_user_orders(
    p_user_id integer,
    p_status varchar DEFAULT NULL
)
RETURNS TABLE (
    order_id integer,
    order_number varchar,
    total_amount numeric,
    created_at timestamp
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        o.id,
        o.order_number,
        o.total_amount,
        o.created_at
    FROM orders o
    WHERE o.user_id = p_user_id
      AND (p_status IS NULL OR o.status = p_status)
    ORDER BY o.created_at DESC;
END;
$$;

-- Использование
SELECT * FROM get_user_orders(123, 'delivered');
