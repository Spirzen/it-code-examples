CREATE TABLE user_events (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id     BIGINT NOT NULL,
    event_type  VARCHAR(64) NOT NULL,
    payload     JSONB NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
)
PARTITION BY RANGE (occurred_at);

-- Автоматическое создание партиций (через функцию или cron)
SELECT create_monthly_partition('user_events', '2025-01-01'::DATE, '2025-01-31'::DATE);

-- Частичный индекс для частых фильтров
CREATE INDEX idx_user_events_type ON user_events (event_type, user_id)
WHERE event_type IN ('LOGIN', 'PAYMENT', 'ORDER_CREATED');

-- Оптимизация для агрегаций
CREATE INDEX idx_user_events_ts ON user_events (occurred_at);
