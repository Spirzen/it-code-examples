WITH RECURSIVE category_tree AS (
    -- Базовый случай: корневые категории
    SELECT 
        id,
        name,
        parent_id,
        name AS path,
        1 AS level
    FROM categories
    WHERE parent_id IS NULL
    
    UNION ALL
    
    -- Рекурсивный случай: дочерние категории
    SELECT 
        c.id,
        c.name,
        c.parent_id,
        ct.path || ' > ' || c.name,
        ct.level + 1
    FROM categories c
    INNER JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT 
    id,
    name,
    path,
    level
FROM category_tree
ORDER BY path;
