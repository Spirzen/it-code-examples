-- Oracle синтаксис подсказок
SELECT /*+ INDEX(employees emp_dept_idx) USE_NL(departments) */ 
    e.employee_name,
    d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- SQL Server синтаксис подсказок
SELECT e.employee_name, d.department_name
FROM employees e WITH (INDEX(emp_dept_idx))
JOIN departments d ON e.department_id = d.department_id
OPTION (LOOP JOIN, FAST 100);

-- MySQL синтаксис подсказок
SELECT /*+ BKA(t1) NO_RANGE_OPTIMIZATION(t2 PRIMARY) */ 
    t1.col1, t2.col2
FROM t1
JOIN t2 ON t1.id = t2.id;
