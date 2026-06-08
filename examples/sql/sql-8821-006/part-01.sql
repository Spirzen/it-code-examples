-- Пример комплексных подсказок в Oracle
SELECT /*+ 
    PARALLEL(e 4) 
    PARALLEL(d 4) 
    USE_HASH(e d) 
    FULL(e) 
    INDEX(d dept_location_idx) 
    LEADING(d e)
*/ 
    e.employee_id,
    e.employee_name,
    d.department_name,
    l.location_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE e.hire_date >= ADD_MONTHS(SYSDATE, -12)
  AND l.country_id = 'US'
ORDER BY e.salary DESC;
