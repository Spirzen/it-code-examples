CREATE KEYSPACE IF NOT EXISTS learning_cassandra
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE learning_cassandra;

CREATE TABLE sensor_readings (
    device_id TEXT,
    recorded_at TIMESTAMP,
    temperature DOUBLE,
    PRIMARY KEY (device_id, recorded_at)
) WITH CLUSTERING ORDER BY (recorded_at DESC);

INSERT INTO sensor_readings (device_id, recorded_at, temperature)
VALUES ('sensor-1', toTimestamp(now()), 22.5);

INSERT INTO sensor_readings (device_id, recorded_at, temperature)
VALUES ('sensor-1', '2025-05-20 10:00:00+0000', 21.0);

-- CONSISTENCY действует на следующие запросы в сессии cqlsh
CONSISTENCY LOCAL_ONE;

SELECT temperature, recorded_at
FROM sensor_readings
WHERE device_id = 'sensor-1'
  AND recorded_at >= '2025-05-20 00:00:00+0000';

SELECT COUNT(*) FROM sensor_readings WHERE device_id = 'sensor-1';
