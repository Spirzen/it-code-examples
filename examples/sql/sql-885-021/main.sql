-- Поиск объектов, принадлежащих роли
SELECT 
    n.nspname AS schema_name,
    c.relname AS object_name,
    c.relkind AS object_type
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE c.relowner = (SELECT oid FROM pg_roles WHERE rolname = 'old_user');

-- Передача прав на объекты другой роли
REASSIGN OWNED BY old_user TO new_user;

-- Удаление оставшихся привилегий
DROP OWNED BY old_user;

-- Удаление роли
DROP ROLE old_user;
