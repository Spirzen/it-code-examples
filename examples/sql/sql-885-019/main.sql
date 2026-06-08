-- Активные процессы автовакуума
SELECT 
    pid,
    query,
    NOW() - query_start AS duration,
    state
FROM pg_stat_activity
WHERE query LIKE 'autovacuum:%'
  AND state = 'active';

-- Таблицы, нуждающиеся в вакууме
SELECT 
    schemaname,
    relname,
    n_dead_tup,
    n_live_tup,
    last_vacuum,
    last_autovacuum,
    ROUND(100.0 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0), 2) AS dead_ratio
FROM pg_stat_user_tables
WHERE n_dead_tup > 10000
ORDER BY n_dead_tup DESC;
