CREATE OR REPLACE FUNCTION notify_order_paid()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
  IF NEW.status = 'paid' AND OLD.status IS DISTINCT FROM 'paid' THEN
    PERFORM pg_notify(
      'order_events',
      json_build_object('id', NEW.id, 'status', NEW.status)::text
    );
  END IF;
  RETURN NEW;
END;
$$;
