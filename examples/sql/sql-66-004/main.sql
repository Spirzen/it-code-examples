SELECT
    event_id,
    jsonb_extract_path_text(payload, 'order', 'status') AS order_status,
    jsonb_object_keys(payload) AS top_level_key
FROM shop_data.events
WHERE payload ? 'order';

SELECT
    jsonb_build_object(
      'event_id', event_id,
      'order_id', payload->'order'->>'id',
      'source', source
    ) AS compact_doc
FROM shop_data.events
LIMIT 3;

SELECT event_id
FROM shop_data.events
WHERE payload @? '$.items[*] ? (@.qty > 1)';
