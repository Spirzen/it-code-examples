[WITH cte_name [(col, ...)] AS (SELECT ...) [, ...]]
SELECT [ALL | DISTINCT] 
       [TOP n [PERCENT]]                    -- T-SQL
       [ALL | DISTINCT ON (expr)] expr AS alias, ...  -- PostgreSQL
FROM table_source [alias]
  [JOIN another_table ON condition | USING (col)]
WHERE condition
GROUP BY expr [, ...]
HAVING group_condition
WINDOW window_name AS (window_spec) [, ...]
ORDER BY expr [ASC | DESC] [NULLS {FIRST | LAST}]  -- NULLS — PostgreSQL, Oracle
LIMIT n [OFFSET m]               -- PostgreSQL, MySQL, SQLite
FETCH {FIRST | NEXT} n {ROW | ROWS} ONLY  -- ANSI, SQL Server ≥2012, PostgreSQL
FOR {UPDATE | SHARE} [OF table [, ...]] [NOWAIT | SKIP LOCKED];  -- блокировки
