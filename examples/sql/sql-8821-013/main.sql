-- Регулярный мониторинг производительности запросов с подсказками
-- Создание представления для отслеживания медленных запросов
CREATE VIEW slow_queries_with_hints AS
SELECT 
    query_id,
    query_text,
    execution_count,
    total_elapsed_time / execution_count AS avg_elapsed_time_ms,
    total_logical_reads / execution_count AS avg_logical_reads,
    total_physical_reads / execution_count AS avg_physical_reads,
    CASE 
        WHEN query_text LIKE '%/*+%' THEN 'Contains hints'
        ELSE 'No hints'
    END AS hint_status
FROM query_stats
WHERE total_elapsed_time / execution_count > 1000  -- Среднее время выполнения более 1 секунды
ORDER BY avg_elapsed_time_ms DESC;

-- Регулярная проверка планов выполнения для запросов с подсказками
SELECT 
    qs.query_id,
    qs.query_text,
    qp.query_plan,
    qs.last_execution_time,
    qs.execution_count
FROM query_stats qs
CROSS APPLY query_plan qp
WHERE qs.query_text LIKE '%/*+%'
  AND qs.last_execution_time > DATE_SUB(CURRENT_DATE, INTERVAL 7 DAY)
ORDER BY qs.last_execution_time DESC;
