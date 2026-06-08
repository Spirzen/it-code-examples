-- Извлечение скалярного значения
SELECT JSON_VALUE(doc, '$.user.name') AS name FROM logs;

-- Извлечение объекта/массива как JSON-строки
SELECT JSON_QUERY(doc, '$.items') AS items FROM orders;

-- Преобразование JSON-массива в таблицу (ANSI)
SELECT jt.*
FROM orders,
JSON_TABLE(items, '$[*]' COLUMNS (
    id INT PATH '$.id',
    name VARCHAR(50) PATH '$.name',
    price DECIMAL(10,2) PATH '$.price'
)) AS jt;
