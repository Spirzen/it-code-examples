-- Исходная схема
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL
);

-- Расширение: добавляем новые поля
ALTER TABLE users ADD COLUMN first_name VARCHAR(128);
ALTER TABLE users ADD COLUMN last_name VARCHAR(128);

-- Заполнение новых полей из старых
UPDATE users 
SET first_name = SPLIT_PART(full_name, ' ', 1),
    last_name = SUBSTRING(full_name FROM POSITION(' ' IN full_name) + 1);
