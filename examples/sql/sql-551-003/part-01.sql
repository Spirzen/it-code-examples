WITH RECURSIVE иерархия_отделов AS (
    -- Начальный запрос: корневые элементы
    SELECT 
        department_id,
        department_name,
        parent_department_id,
        department_name AS full_path,
        1 AS level
    FROM departments
    WHERE parent_department_id IS NULL
    
    UNION ALL
    
    -- Рекурсивный запрос: дочерние элементы
    SELECT 
        d.department_id,
        d.department_name,
        d.parent_department_id,
        CONCAT(h.full_path, ' -> ', d.department_name) AS full_path,
        h.level + 1 AS level
    FROM departments d
    INNER JOIN иерархия_отделов h ON d.parent_department_id = h.department_id
)
SELECT 
    department_id,
    department_name,
    full_path,
    level
FROM иерархия_отделов
ORDER BY full_path;
