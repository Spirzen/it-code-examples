CREATE OR REPLACE FUNCTION orders_total(p_customer_id bigint)
RETURNS numeric
LANGUAGE plpgsql
STABLE
AS $$
DECLARE
  v_total numeric;
BEGIN
  SELECT COALESCE(SUM(amount), 0) INTO v_total
  FROM orders
  WHERE customer_id = p_customer_id
    AND status = 'paid';

  RETURN v_total;
END;
$$;
