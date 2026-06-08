-- Добавление нового значения в enum
ALTER TYPE order_status ADD VALUE IF NOT EXISTS 'refunded' AFTER 'delivered';

-- Удаление значения из enum (требует пересоздания типа)
-- Создаём новый тип без ненужного значения
CREATE TYPE order_status_new AS ENUM ('new', 'processing', 'shipped', 'delivered', 'cancelled');

-- Меняем тип колонки
ALTER TABLE orders 
ALTER COLUMN status TYPE order_status_new 
USING status::text::order_status_new;

-- Удаляем старый тип и переименовываем новый
DROP TYPE order_status;
ALTER TYPE order_status_new RENAME TO order_status;
