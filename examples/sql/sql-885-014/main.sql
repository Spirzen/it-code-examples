-- Сброс последовательности к максимальному значению в таблице
SELECT setval(
    'products_id_seq',
    COALESCE((SELECT MAX(id) FROM products), 0) + 1,
    false
);

-- Проверка текущего значения последовательности
SELECT last_value, is_called FROM products_id_seq;

-- Просмотр всех последовательностей в схеме
SELECT 
    sequence_schema,
    sequence_name,
    last_value,
    increment_by
FROM information_schema.sequences
WHERE sequence_schema = 'public';
