WITH активные_пользователи AS (
    SELECT 
        user_id,
        username,
        registration_date,
        last_login_date
    FROM users
    WHERE status = 'active'
    AND last_login_date >= CURRENT_DATE - INTERVAL '30 days'
    ORDER BY last_login_date DESC
    LIMIT 1000
),
покупки_пользователей AS (
    SELECT 
        p.user_id,
        COUNT(*) AS purchase_count,
        SUM(p.amount) AS total_spent,
        MAX(p.purchase_date) AS last_purchase_date
    FROM purchases p
    WHERE p.purchase_date >= CURRENT_DATE - INTERVAL '90 days'
    GROUP BY p.user_id
)
SELECT 
    au.user_id,
    au.username,
    au.registration_date,
    pu.purchase_count,
    pu.total_spent,
    pu.last_purchase_date
FROM активные_пользователи au
LEFT JOIN покупки_пользователей pu ON au.user_id = pu.user_id
ORDER BY pu.total_spent DESC NULLS LAST;
