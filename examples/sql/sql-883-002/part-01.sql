INSERT INTO table_name [(col1, col2, ...)]
    VALUES (val1, val2, ...),
           (val3, val4, ...);

-- Или из SELECT:
INSERT INTO table_name [(col1, col2, ...)]
    SELECT ... FROM ...;

-- Возвращаемые значения (PostgreSQL, Firebird):
INSERT INTO ... RETURNING * | column [, ...];

-- T-SQL: OUTPUT clause
INSERT INTO ...
OUTPUT inserted.col1, inserted.col2 INTO @table_var
VALUES (...);
