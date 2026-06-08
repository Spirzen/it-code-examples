CREATE SCHEMA IF NOT EXISTS shop_data;

CREATE TABLE IF NOT EXISTS shop_data.accounts (
    account_id  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    account_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS shop_data.events (
    event_id     BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    account_id   BIGINT NOT NULL REFERENCES shop_data.accounts(account_id),
    event_type   TEXT NOT NULL,
    source       TEXT NOT NULL,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
    payload      JSONB NOT NULL
);
