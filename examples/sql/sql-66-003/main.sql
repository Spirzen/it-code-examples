SELECT
    event_id,
    payload->'order'->>'id' AS order_id,
    payload->'flags'->>'is_priority' AS is_priority_text
FROM shop_data.events
WHERE event_type = 'order_created';

SELECT event_id, payload #>> '{customer,city}' AS customer_city
FROM shop_data.events
WHERE payload ? 'customer';

SELECT event_id, event_type
FROM shop_data.events
WHERE payload @> '{"flags":{"is_priority": true}}'::jsonb;
