-- Использование триггера для проверки лимита
CREATE OR REPLACE FUNCTION check_item_limit()
RETURNS TRIGGER AS $$
DECLARE
    v_count integer;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM order_items
    WHERE order_id = NEW.order_id;
    
    IF v_count >= 100 THEN
        RAISE EXCEPTION 'Limit exceeded for order items';
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_item_limit
BEFORE INSERT ON order_items
FOR EACH ROW EXECUTE FUNCTION check_item_limit();
