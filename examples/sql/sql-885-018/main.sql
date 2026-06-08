-- Просмотр текущих настроек
SELECT name, setting, unit, context 
FROM pg_settings 
WHERE name IN (
    'shared_buffers',
    'work_mem',
    'maintenance_work_mem',
    'effective_cache_size',
    'max_connections'
);

-- Изменение параметра на уровне сессии
SET work_mem = '64MB';

-- Изменение параметра на уровне базы данных
ALTER DATABASE mydb SET work_mem = '64MB';

-- Изменение параметра в конфигурации (требует перезагрузки)
-- ALTER SYSTEM SET shared_buffers = '4GB';
-- SELECT pg_reload_conf();
