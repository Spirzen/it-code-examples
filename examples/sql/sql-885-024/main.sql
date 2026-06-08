CREATE OR REPLACE FUNCTION measure_execution()
RETURNS void AS $$
DECLARE
    start_time timestamp;
    end_time timestamp;
BEGIN
    start_time := clock_timestamp();
    
    -- Выполнение целевой логики
    PERFORM heavy_operation();
    
    end_time := clock_timestamp();
    RAISE NOTICE 'Execution time: %', end_time - start_time;
END;
$$ LANGUAGE plpgsql;
