WITH RECURSIVE tree AS (
    -- Anchor member (база рекурсии)
    SELECT id, parent_id, name, 0 AS level
    FROM nodes
    WHERE parent_id IS NULL

    UNION ALL

    -- Recursive member (шаг)
    SELECT n.id, n.parent_id, n.name, t.level + 1
    FROM nodes n
    INNER JOIN tree t ON n.parent_id = t.id
)
SELECT * FROM tree ORDER BY level, name;
