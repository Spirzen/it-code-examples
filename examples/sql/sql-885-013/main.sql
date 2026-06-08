-- Поиск в функциях и процедурах
SELECT 
    routine_schema,
    routine_name,
    routine_type
FROM information_schema.routines
WHERE routine_definition ILIKE '%products%';

-- Поиск в представлениях
SELECT 
    table_schema,
    table_name
FROM information_schema.views
WHERE view_definition ILIKE '%products%';

-- Поиск в триггерах
SELECT 
    trigger_schema,
    trigger_name,
    event_object_table
FROM information_schema.triggers
WHERE action_statement ILIKE '%products%';

-- Поиск в ограничениях
SELECT 
    tc.table_schema,
    tc.table_name,
    tc.constraint_name,
    ccu.table_name AS foreign_table
FROM information_schema.table_constraints tc
JOIN information_schema.constraint_column_usage ccu 
    ON tc.constraint_name = ccu.constraint_name
WHERE tc.constraint_name ILIKE '%products%'
   OR ccu.table_name ILIKE '%products%';
