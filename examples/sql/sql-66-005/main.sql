-- 1) Список событий с извлечением полей
SELECT
    event_id,
    event_type,
    payload->'order'->>'id' AS order_id,
    (payload->'order'->>'total')::numeric AS total
FROM shop_data.events
WHERE payload ? 'order';

-- 2) Поиск по вхождению JSON
SELECT event_id, event_type
FROM shop_data.events
WHERE payload @> '{"payment":{"method":"card"}}'::jsonb;

-- 3) Разворот массива и расчёт по позициям
SELECT
    e.event_id,
    SUM((i.value->>'qty')::int) AS total_qty
FROM shop_data.events e
CROSS JOIN jsonb_array_elements(e.payload->'items') AS i(value)
GROUP BY e.event_id
HAVING SUM((i.value->>'qty')::int) >= 2;
