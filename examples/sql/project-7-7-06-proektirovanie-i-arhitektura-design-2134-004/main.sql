-- Плохой ключ: все записи за день попадают в один шард
CREATE TABLE events (
    event_date DATE,
    event_id BIGINT,
    PRIMARY KEY (event_date, event_id)
) PARTITION BY HASH(event_date);

-- Хороший ключ: равномерное распределение по пользователям
CREATE TABLE events (
    user_id BIGINT,
    event_timestamp TIMESTAMP,
    event_id BIGINT,
    PRIMARY KEY ((user_id), event_timestamp, event_id)
) PARTITION BY HASH(user_id);
