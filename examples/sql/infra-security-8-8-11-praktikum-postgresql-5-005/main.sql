CREATE OR REPLACE FUNCTION reject_drop()
RETURNS event_trigger
LANGUAGE plpgsql
AS $$
BEGIN
  IF tg_tag = 'DROP TABLE' THEN
    RAISE EXCEPTION 'DROP TABLE запрещён в production';
  END IF;
END;
$$;

CREATE EVENT TRIGGER protect_drop
  ON sql_drop
  EXECUTE FUNCTION reject_drop();
