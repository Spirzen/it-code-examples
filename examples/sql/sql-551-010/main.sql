WITH RECURSIVE структура_подразделений AS (
    -- Корневые подразделения
    SELECT 
        department_id,
        department_name,
        parent_department_id,
        department_name AS полный_путь,
        1 AS уровень
    FROM подразделения
    WHERE parent_department_id IS NULL
    
    UNION ALL
    
    -- Дочерние подразделения
    SELECT 
        d.department_id,
        d.department_name,
        d.parent_department_id,
        CONCAT(s.полный_путь, ' / ', d.department_name) AS полный_путь,
        s.уровень + 1 AS уровень
    FROM подразделения d
    INNER JOIN структура_подразделений s 
        ON d.parent_department_id = s.department_id
)
SELECT 
    department_id,
    department_name,
    полный_путь,
    уровень
FROM структура_подразделений
ORDER BY полный_путь;
