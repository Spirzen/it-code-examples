CREATE OR REPLACE PROCEDURE update_department_stats()
LANGUAGE plpgsql
AS $$
DECLARE
    dept_record RECORD;
BEGIN
    FOR dept_record IN 
        SELECT d.id, d.name, COUNT(e.id) as emp_count, SUM(e.salary) as total_salary
        FROM departments d
        LEFT JOIN employees e ON d.id = e.department_id
        GROUP BY d.id, d.name
    LOOP
        RAISE NOTICE 'Отдел: %, Количество сотрудников: %, Общий фонд: %', 
                     dept_record.name, dept_record.emp_count, dept_record.total_salary;
        
        -- Здесь можно добавить логику записи статистики в отдельную таблицу
        -- INSERT INTO dept_statistics ...
    END LOOP;
END;
$$;
