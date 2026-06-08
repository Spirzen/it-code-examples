CREATE OR REPLACE FUNCTION batch_update_prices(
    p_category_id integer,
    p_multiplier numeric,
    p_batch_size integer DEFAULT 1000
)
RETURNS TABLE (
    processed_count integer,
    iteration integer
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_updated integer;
    v_iteration integer := 0;
BEGIN
    LOOP
        v_iteration := v_iteration + 1;
        
        WITH updated AS (
            UPDATE products
            SET 
                price = price * p_multiplier,
                updated_at = CURRENT_TIMESTAMP
            WHERE id IN (
                SELECT id FROM products
                WHERE category_id = p_category_id
                  AND updated_at < CURRENT_TIMESTAMP - INTERVAL '1 hour'
                LIMIT p_batch_size
            )
            RETURNING id
        )
        SELECT COUNT(*) INTO v_updated FROM updated;
        
        processed_count := v_updated;
        iteration := v_iteration;
        RETURN NEXT;
        
        EXIT WHEN v_updated < p_batch_size;
        
        -- Пауза для снижения нагрузки
        PERFORM pg_sleep(0.1);
    END LOOP;
END;
$$;

-- Использование
SELECT * FROM batch_update_prices(5, 1.15, 500);
