MERGE INTO target_table AS T
USING source_table_or_query AS S
ON T.key = S.key
WHEN MATCHED [AND condition] THEN
    UPDATE SET col = S.col, ...
    -- [DELETE] — Oracle, SQL Server
WHEN NOT MATCHED [BY TARGET] [AND condition] THEN
    INSERT (col1, col2) VALUES (S.col1, S.col2)
WHEN NOT MATCHED BY SOURCE [AND condition] THEN
    DELETE
[RETURNING $action, ...];  -- SQL Server
-- Поддержка: SQL Server (полная), Oracle, PostgreSQL ≥15 (MERGE, ограниченная), Snowflake, BigQuery
-- В SQLite: `INSERT ... ON CONFLICT DO UPDATE/IGNORE`
-- В MySQL: `INSERT ... ON DUPLICATE KEY UPDATE`
