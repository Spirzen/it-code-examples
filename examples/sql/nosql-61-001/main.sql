CREATE TABLE metrics (
  name text,
  day date,
  ts timestamp,
  host uuid,
  value double,
  PRIMARY KEY ((name, day), ts, host)
)
WITH CLUSTERING ORDER BY (ts DESC)
AND compaction = {
  'class': 'TimeWindowCompactionStrategy',
  'compaction_window_unit': 'DAYS',
  'compaction_window_size': '1'
}
AND default_time_to_live = 2592000
AND gc_grace_seconds = 86400;
