-- На мастере: статус реплик
SELECT 
    client_addr,
    state,
    sent_lsn,
    write_lsn,
    flush_lsn,
    replay_lsn,
    NOW() - reply_time AS replication_lag
FROM pg_stat_replication;

-- На реплике: статус восстановления
SELECT 
    pg_is_in_recovery(),
    pg_last_wal_receive_lsn(),
    pg_last_wal_replay_lsn(),
    pg_last_xact_replay_timestamp();
