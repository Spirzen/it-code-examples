-- Оптимизация рекурсивного запроса для иерархии организационной структуры
WITH RECURSIVE /*+ MATERIALIZE */ организационная_иерархия AS (
    -- Начальный уровень: топ-менеджеры
    SELECT /*+ INDEX(employees emp_manager_idx) */
        employee_id,
        employee_name,
        manager_id,
        job_title,
        department_id,
        1 AS hierarchy_level,
        CAST(employee_name AS VARCHAR(1000)) AS hierarchy_path
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Рекурсивный уровень: подчиненные
    SELECT /*+ USE_NL(e oh) INDEX(e emp_manager_idx) */
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.job_title,
        e.department_id,
        oh.hierarchy_level + 1 AS hierarchy_level,
        CONCAT(oh.hierarchy_path, ' -> ', e.employee_name) AS hierarchy_path
    FROM employees e
    JOIN организационная_иерархия oh ON e.manager_id = oh.employee_id
    WHERE oh.hierarchy_level < 10
)
SELECT /*+ NO_PARALLEL */
    employee_id,
    LPAD(' ', (hierarchy_level - 1) * 4) || employee_name AS indented_name,
    manager_id,
    job_title,
    department_id,
    hierarchy_level,
    hierarchy_path,
    COUNT(*) OVER (PARTITION BY employee_id) AS direct_reports_count
FROM организационная_иерархия
ORDER BY hierarchy_path;
