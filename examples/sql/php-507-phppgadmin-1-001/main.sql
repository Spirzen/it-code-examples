-- Таблицы в схеме public (аналог дерева объектов слева)
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE';

-- Выборка с фильтром (DML)
SELECT id, customer_name, total
FROM public.orders
WHERE status = 'pending'
ORDER BY created_at DESC
LIMIT 20;

-- Sequence после INSERT (Postgres не AUTO_INCREMENT как MySQL)
INSERT INTO public.orders (customer_name, total, status)
VALUES ('Test User', 99.90, 'pending')
RETURNING id;
