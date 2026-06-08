-- Обработка данными порциями
DO $$
DECLARE
    batch_size integer := 10000;
    processed integer := 1;
BEGIN
    WHILE processed > 0 LOOP
        WITH deleted AS (
            DELETE FROM large_log_table
            WHERE id IN (
                SELECT id FROM large_log_table LIMIT batch_size
            )
            RETURNING id
        )
        SELECT COUNT(*) INTO processed FROM deleted;
        
        COMMIT;
        PERFORM pg_sleep(0.1);
    END LOOP;
END $$;
