-- Оптимизация сложного аналитического запроса
WITH /*+ MATERIALIZE */ базовые_продажи AS (
    SELECT /*+ PARALLEL(s 4) PARALLEL(p 2) USE_HASH(s p) */
        s.sale_id,
        s.sale_date,
        s.customer_id,
        p.product_id,
        p.product_category,
        p.product_subcategory,
        s.quantity,
        s.unit_price,
        s.quantity * s.unit_price AS sale_amount,
        EXTRACT(YEAR FROM s.sale_date) AS sale_year,
        EXTRACT(QUARTER FROM s.sale_date) AS sale_quarter
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    WHERE s.sale_date >= DATE_SUB(CURRENT_DATE, INTERVAL 2 YEAR)
),
агрегированные_продажи AS (
    SELECT /*+ INLINE */
        sale_year,
        sale_quarter,
        product_category,
        product_subcategory,
        COUNT(*) AS transaction_count,
        SUM(quantity) AS total_quantity,
        SUM(sale_amount) AS total_sales,
        AVG(sale_amount) AS avg_transaction_value,
        MIN(sale_amount) AS min_transaction,
        MAX(sale_amount) AS max_transaction
    FROM базовые_продажи
    GROUP BY sale_year, sale_quarter, product_category, product_subcategory
),
ранжированные_категории AS (
    SELECT /*+ INLINE */
        sale_year,
        sale_quarter,
        product_category,
        product_subcategory,
        transaction_count,
        total_quantity,
        total_sales,
        avg_transaction_value,
        RANK() OVER (
            PARTITION BY sale_year, sale_quarter 
            ORDER BY total_sales DESC
        ) AS sales_rank,
        PERCENT_RANK() OVER (
            PARTITION BY sale_year, sale_quarter 
            ORDER BY total_sales DESC
        ) AS sales_percent_rank,
        SUM(total_sales) OVER (
            PARTITION BY sale_year, sale_quarter
        ) AS quarter_total_sales,
        total_sales / SUM(total_sales) OVER (
            PARTITION BY sale_year, sale_quarter
        ) * 100 AS sales_percentage
    FROM агрегированные_продажи
)
SELECT /*+ NO_PARALLEL */
    sale_year,
    sale_quarter,
    product_category,
    product_subcategory,
    transaction_count,
    total_quantity,
    total_sales,
    avg_transaction_value,
    sales_rank,
    ROUND(sales_percent_rank * 100, 2) AS percentile,
    ROUND(sales_percentage, 2) AS market_share
FROM ранжированные_категории
WHERE sales_rank <= 10
ORDER BY sale_year DESC, sale_quarter DESC, sales_rank;
