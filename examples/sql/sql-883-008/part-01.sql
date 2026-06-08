-- ANSI-совместимый стиль (PostgreSQL)
CREATE FUNCTION add_numbers(a INT, b INT)
RETURNS INT
LANGUAGE SQL
AS $$
    SELECT a + b;
$$;

-- PL/pgSQL (многострочный)
CREATE FUNCTION factorial(n INT)
RETURNS BIGINT
LANGUAGE plpgsql
AS $$
DECLARE
    res BIGINT := 1;
    i INT;
BEGIN
    FOR i IN 1..n LOOP
        res := res * i;
    END LOOP;
    RETURN res;
END;
$$;

-- Возвращающая таблицу (PostgreSQL)
CREATE FUNCTION get_employees_by_dept(did INT)
RETURNS TABLE(id INT, name TEXT, salary NUMERIC)
LANGUAGE sql
AS $$
    SELECT id, name, salary
    FROM employees
    WHERE dept_id = did;
$$;
-- Использование: SELECT * FROM get_employees_by_dept(5);
