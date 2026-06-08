WITH базовые_данные AS (
    SELECT 
        employee_id,
        employee_name,
        department_id,
        salary,
        hire_date
    FROM employees
    WHERE status = 'active'
),
данные_отделов AS (
    SELECT 
        d.department_id,
        d.department_name,
        d.manager_id,
        COUNT(b.employee_id) AS employee_count
    FROM departments d
    LEFT JOIN базовые_данные b ON d.department_id = b.department_id
    GROUP BY d.department_id, d.department_name, d.manager_id
),
расчеты_зарплат AS (
    SELECT 
        b.employee_id,
        b.employee_name,
        b.department_id,
        b.salary,
        AVG(b.salary) OVER (PARTITION BY b.department_id) AS avg_dept_salary,
        b.salary - AVG(b.salary) OVER (PARTITION BY b.department_id) AS diff_from_avg
    FROM базовые_данные b
)
SELECT 
    r.employee_name,
    d.department_name,
    r.salary,
    r.avg_dept_salary,
    r.diff_from_avg,
    d.employee_count
FROM расчеты_зарплат r
JOIN данные_отделов d ON r.department_id = d.department_id
ORDER BY r.diff_from_avg DESC;
