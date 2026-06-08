-- Многоэтапная обработка данных
WITH исходные_транзакции AS (
    SELECT 
        transaction_id,
        account_id,
        amount,
        transaction_date,
        transaction_type
    FROM транзакции
    WHERE transaction_date >= CURRENT_DATE - INTERVAL '90 days'
    AND статус = 'завершена'
),
агрегация_по_счетам AS (
    SELECT 
        account_id,
        COUNT(*) AS transaction_count,
        SUM(amount) AS total_volume,
        AVG(amount) AS average_amount,
        MAX(transaction_date) AS last_activity
    FROM исходные_транзакции
    GROUP BY account_id
),
категоризация_активности AS (
    SELECT 
        account_id,
        transaction_count,
        total_volume,
        average_amount,
        last_activity,
        CASE 
            WHEN transaction_count > 50 THEN 'высокая'
            WHEN transaction_count > 20 THEN 'средняя'
            ELSE 'низкая'
        END AS activity_level
    FROM агрегация_по_счетам
)
SELECT 
    c.account_id,
    a.account_name,
    c.transaction_count,
    c.total_volume,
    c.average_amount,
    c.activity_level,
    c.last_activity
FROM категоризация_активности c
JOIN счета a ON c.account_id = a.account_id
WHERE c.activity_level = 'высокая'
ORDER BY c.total_volume DESC;
