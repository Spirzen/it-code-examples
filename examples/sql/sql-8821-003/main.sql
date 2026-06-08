-- Принудительное использование конкретного индекса
SELECT /*+ INDEX(employees emp_dept_idx) */ 
    employee_id,
    employee_name,
    department_id
FROM employees
WHERE department_id = 10;

-- Принудительное использование любого индекса по столбцу
SELECT /*+ INDEX(orders) */ 
    order_id,
    order_date,
    customer_id,
    order_total
FROM orders
WHERE order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 7 DAY)
ORDER BY order_date DESC;
