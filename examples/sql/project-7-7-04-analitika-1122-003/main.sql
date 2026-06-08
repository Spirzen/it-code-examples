SELECT
    sale_date,
    region,
    amount,
    SUM(amount) OVER (
        PARTITION BY region
        ORDER BY sale_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_sum,
    LAG(amount, 1) OVER (
        PARTITION BY region
        ORDER BY sale_date
    ) AS prev_day_amount
FROM sales;
