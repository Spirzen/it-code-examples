-- Пример подсказок в MySQL
SELECT /*+ 
    BKA(o) 
    NO_RANGE_OPTIMIZATION(o PRIMARY) 
    JOIN_ORDER(c, o, od, p) 
    SET_VAR(optimizer_switch='index_merge=off')
*/ 
    c.customer_name,
    o.order_date,
    od.quantity,
    od.unit_price,
    p.product_name
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_details od ON o.order_id = od.order_id
INNER JOIN products p ON od.product_id = p.product_id
WHERE o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
  AND c.country = 'USA'
ORDER BY o.order_date DESC;
