WITH исходные_данные AS (
    SELECT 
        transaction_id,
        customer_id,
        transaction_date,
        amount,
        transaction_type
    FROM transactions
    WHERE transaction_date >= '2025-01-01'
),
агрегированные_данные AS (
    SELECT 
        customer_id,
        COUNT(*) AS transaction_count,
        SUM(amount) AS total_amount,
        AVG(amount) AS avg_amount,
        MIN(transaction_date) AS first_transaction,
        MAX(transaction_date) AS last_transaction
    FROM исходные_данные
    GROUP BY customer_id
),
сегментация_клиентов AS (
    SELECT 
        ad.customer_id,
        ad.transaction_count,
        ad.total_amount,
        ad.avg_amount,
        ad.first_transaction,
        ad.last_transaction,
        CASE 
            WHEN ad.total_amount > 10000 THEN 'premium'
            WHEN ad.total_amount > 5000 THEN 'gold'
            WHEN ad.total_amount > 1000 THEN 'silver'
            ELSE 'bronze'
        END AS customer_segment
    FROM агрегированные_данные ad
),
статистика_сегментов AS (
    SELECT 
        customer_segment,
        COUNT(*) AS customer_count,
        SUM(total_amount) AS segment_total,
        AVG(total_amount) AS segment_avg,
        MIN(transaction_count) AS min_transactions,
        MAX(transaction_count) AS max_transactions
    FROM сегментация_клиентов
    GROUP BY customer_segment
)
SELECT 
    sc.customer_id,
    c.customer_name,
    c.email,
    sc.transaction_count,
    sc.total_amount,
    sc.avg_amount,
    sc.customer_segment,
    ss.segment_total,
    ss.segment_avg
FROM сегментация_клиентов sc
JOIN customers c ON sc.customer_id = c.customer_id
JOIN статистика_сегментов ss ON sc.customer_segment = ss.customer_segment
ORDER BY sc.total_amount DESC;
