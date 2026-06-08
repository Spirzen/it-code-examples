WITH product_revenue AS (
    SELECT
        p.name,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM shop_data.order_items oi
    JOIN shop_data.products p ON p.product_id = oi.product_id
    GROUP BY p.name
),
ranked AS (
    SELECT
        name,
        revenue,
        SUM(revenue) OVER () AS total,
        SUM(revenue) OVER (ORDER BY revenue DESC) AS cumulative,
        ROUND(
            100.0 * SUM(revenue) OVER (ORDER BY revenue DESC)
            / SUM(revenue) OVER (),
            1
        ) AS cumulative_pct
    FROM product_revenue
)
SELECT name, revenue, cumulative_pct,
       CASE
           WHEN cumulative_pct <= 80 THEN 'A'
           WHEN cumulative_pct <= 95 THEN 'B'
           ELSE 'C'
       END AS abc_class
FROM ranked
ORDER BY revenue DESC;
