SELECT 
    user_id,
    action_date,
    'clicked_link' as event_type
FROM click_events
UNION ALL
SELECT 
    user_id,
    action_date,
    'completed_order' as event_type
FROM completed_orders
WHERE user_id NOT IN (
    SELECT user_id FROM click_events WHERE action_date = '2026-05-16'
);
