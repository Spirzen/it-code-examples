WITH RECURSIVE дерево_категорий AS (
    SELECT 
        category_id,
        category_name,
        parent_category_id,
        category_name AS full_path,
        1 AS level
    FROM categories
    WHERE parent_category_id IS NULL
    
    UNION ALL
    
    SELECT 
        c.category_id,
        c.category_name,
        c.parent_category_id,
        CONCAT(dc.full_path, ' > ', c.category_name) AS full_path,
        dc.level + 1 AS level
    FROM categories c
    INNER JOIN дерево_категорий dc ON c.parent_category_id = dc.category_id
    WHERE dc.level < 10
)
SELECT 
    category_id,
    category_name,
    full_path,
    level
FROM дерево_категорий
ORDER BY full_path;
