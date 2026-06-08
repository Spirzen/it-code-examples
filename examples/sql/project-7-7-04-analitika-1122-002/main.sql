SELECT
    sale_date,
    region,
    amount,
    ROW_NUMBER() OVER (
        PARTITION BY sale_date, region
        ORDER BY amount DESC
    ) AS row_num,
    RANK() OVER (
        PARTITION BY sale_date, region
        ORDER BY amount DESC
    ) AS rank_pos
FROM sales
WHERE sale_date = CURRENT_DATE - 5
ORDER BY region, amount DESC;
