GRANT privilege [, ...] ON object_type object_name TO {user | role} [, ...]
[WITH GRANT OPTION];  -- даёт право передавать привилегию дальше

-- Привилегии (зависят от объекта):
-- Для таблиц/представлений:
--   SELECT, INSERT, UPDATE [(col, ...)], DELETE, TRUNCATE, REFERENCES, TRIGGER
-- Для схем:
--   USAGE, CREATE
-- Для базы:
--   CONNECT, CREATE, TEMPORARY (TEMP)
-- Для домена/типа:
--   USAGE
-- Для функций:
--   EXECUTE

-- Примеры:
GRANT SELECT, INSERT ON TABLE employees TO analyst;
GRANT UPDATE (salary) ON employees TO manager;
GRANT USAGE ON SCHEMA public TO developer;
GRANT EXECUTE ON FUNCTION calc_bonus(INT) TO payroll_role;

-- ALL PRIVILEGES — передаёт все доступные привилегии на объект.
-- PUBLIC — особая роль: все пользователи.
GRANT SELECT ON employees TO PUBLIC;
