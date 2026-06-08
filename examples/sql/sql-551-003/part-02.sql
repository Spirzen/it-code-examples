WITH RECURSIVE категори_дерево AS (
    SELECT 
        category_id,
        category_name,
        parent_category_id,
        category_name AS path,
        0 AS depth
    FROM categories
    WHERE parent_category_id IS NULL
    
    UNION ALL
    
    SELECT 
        c.category_id,
        c.category_name,
        c.parent_category_id,
        CONCAT(ct.path, ' > ', c.category_name) AS path,
        ct.depth + 1 AS depth
    FROM categories c
    INNER JOIN категори_дерево ct ON c.parent_category_id = ct.category_id
)
SELECT 
    category_id,
    REPEAT('  ', depth) || category_name AS отступ_категория,
    path,
    depth
FROM категори_дерево
ORDER BY path;
