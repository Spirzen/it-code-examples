-- Создание таблицы
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE
);

-- Create: добавление записи
INSERT INTO users (name, email) VALUES ('Алиса', 'alice@example.com');

-- Read: выборка всех записей
SELECT * FROM users;

-- Read: выборка одной записи по условию
SELECT * FROM users WHERE id = 1;

-- Update: изменение записи
UPDATE users SET email = 'new_alice@example.com' WHERE id = 1;

-- Delete: удаление записи
DELETE FROM users WHERE id = 1;
