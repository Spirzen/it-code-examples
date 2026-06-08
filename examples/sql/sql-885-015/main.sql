-- Статистика по индексам таблицы
SELECT 
    indexrelname AS index_name,
    idx_scan AS times_used,
    idx_tup_read AS tuples_read,
    idx_tup_fetch AS tuples_fetched
FROM pg_stat_user_indexes
WHERE schemaname = 'public' 
  AND relname = 'products'
ORDER BY idx_scan DESC;

-- Индексы, которые не используются
SELECT 
    schemaname,
    tablename,
    indexname
FROM pg_stat_user_indexes
WHERE idx_scan = 0 
  AND schemaname = 'public'
ORDER BY pg_relation_size(indexrelid) DESC;
