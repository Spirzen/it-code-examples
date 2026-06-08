-- Проверка валидности
SELECT ISJSON(json_col)

-- Извлечение
SELECT JSON_VALUE(json_col, '$.user.name')
SELECT JSON_QUERY(json_col, '$.items')  -- возвращает JSON-фрагмент

-- Преобразование в таблицу
SELECT * 
FROM OPENJSON(@json, '$.items')
WITH (
    id INT '$.id',
    name NVARCHAR(50) '$.name',
    price DECIMAL(10,2) '$.price'
);
