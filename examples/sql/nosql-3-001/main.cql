CREATE TABLE user_events (
    user_id UUID,
    event_time TIMESTAMP,
    event_type TEXT,
    PRIMARY KEY (user_id, event_time)
) WITH CLUSTERING ORDER BY (event_time DESC);

INSERT INTO user_events (user_id, event_time, event_type)
VALUES (uuid(), toTimestamp(now()), 'login');

SELECT event_type FROM user_events
WHERE user_id = ?
  AND event_time >= ?
  AND event_time < ?;
