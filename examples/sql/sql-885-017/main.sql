-- Запросы с наибольшим временем выполнения
SELECT 
    query,
    calls,
    total_exec_time,
    mean_exec_time,
    rows
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;

-- Запросы, создающие временные файлы
SELECT 
    query,
    temp_blks_read,
    temp_blks_written
FROM pg_stat_statements
WHERE temp_blks_read > 0 OR temp_blks_written > 0
ORDER BY temp_blks_written DESC;
