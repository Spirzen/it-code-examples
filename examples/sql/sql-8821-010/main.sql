-- Анализ плана выполнения в различных СУБД
-- Oracle
EXPLAIN PLAN FOR
SELECT /*+ PARALLEL(employees 4) */ 
    department_id, 
    COUNT(*) 
FROM employees 
GROUP BY department_id;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);

-- PostgreSQL
EXPLAIN ANALYZE
SELECT /*+ HashJoin(e d) */ 
    d.department_name, 
    COUNT(e.employee_id)
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;

-- SQL Server
SET SHOWPLAN_ALL ON;
GO

SELECT 
    d.DepartmentName, 
    COUNT(e.EmployeeID)
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;

SET SHOWPLAN_ALL OFF;
GO

-- MySQL
EXPLAIN FORMAT=JSON
SELECT /*+ BKA(d) */ 
    d.department_name, 
    COUNT(e.employee_id)
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;
