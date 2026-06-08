-- Экспорт настроек для сравнения
SELECT name, setting 
FROM pg_settings 
WHERE source != 'default'
ORDER BY name;

-- Сравнение версий и расширений
SELECT 
    version(),
    current_setting('server_version_num')::int AS version_num;

SELECT 
    extname,
    extversion,
    extnamespace::regnamespace AS schema_name
FROM pg_extension
ORDER BY extname;
