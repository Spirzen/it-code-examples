WITH RECURSIVE ancestors AS (
    SELECT 
        id,
        name,
        parent_id,
        0 AS depth
    FROM categories
    WHERE id = 42
    
    UNION ALL
    
    SELECT 
        c.id,
        c.name,
        c.parent_id,
        a.depth + 1
    FROM categories c
    INNER JOIN ancestors a ON c.id = a.parent_id
)
SELECT name, depth FROM ancestors ORDER BY depth;
