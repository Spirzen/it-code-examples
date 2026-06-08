CREATE OR REPLACE PROCEDURE process_order(
    p_order_id integer,
    p_new_status varchar
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_old_status varchar;
    v_user_id integer;
BEGIN
    -- Сохраняем текущее состояние
    SELECT status, user_id INTO v_old_status, v_user_id
    FROM orders WHERE id = p_order_id;
    
    -- Обновляем статус
    UPDATE orders
    SET 
        status = p_new_status,
        updated_at = CURRENT_TIMESTAMP
    WHERE id = p_order_id;
    
    -- Журналируем изменение
    INSERT INTO order_status_log (
        order_id,
        old_status,
        new_status,
        changed_at,
        changed_by
    ) VALUES (
        p_order_id,
        v_old_status,
        p_new_status,
        CURRENT_TIMESTAMP,
        current_user
    );
    
    -- Фиксируем транзакцию
    COMMIT;
END;
$$;

-- Вызов процедуры
CALL process_order(456, 'shipped');
