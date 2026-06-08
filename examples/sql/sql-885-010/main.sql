CREATE OR REPLACE FUNCTION safe_divide(
    numerator numeric,
    denominator numeric,
    default_value numeric DEFAULT 0
)
RETURNS numeric
LANGUAGE plpgsql
AS $$
BEGIN
    IF denominator = 0 THEN
        RETURN default_value;
    END IF;
    RETURN numerator / denominator;
EXCEPTION
    WHEN OTHERS THEN
        RETURN default_value;
END;
$$;
