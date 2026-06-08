-- Пример потенциально проблемной подсказки после обновления СУБД
-- В старой версии СУБД эта подсказка была необходима для оптимизации
SELECT /*+ USE_NL(orders order_items) INDEX(orders order_date_idx) */ 
    o.order_id,
    o.order_date,
    COUNT(oi.item_id) AS item_count,
    SUM(oi.quantity * oi.unit_price) AS order_total
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
GROUP BY o.order_id, o.order_date
ORDER BY order_total DESC;

-- В новой версии СУБД оптимизатор может выбрать более эффективный план
-- без подсказки или с другой подсказкой
