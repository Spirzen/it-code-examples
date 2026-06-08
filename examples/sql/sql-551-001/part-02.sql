WITH продажи_по_регионам AS (
    SELECT 
        region,
        SUM(sales_amount) AS total_sales,
        AVG(sales_amount) AS avg_sales,
        COUNT(*) AS transaction_count
    FROM sales_data
    GROUP BY region
)
SELECT 
    region,
    total_sales,
    avg_sales,
    transaction_count,
    total_sales / transaction_count AS средний_чек
FROM продажи_по_регионам
WHERE total_sales > 100000;
