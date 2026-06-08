-- Пример подсказок в PostgreSQL с расширением pg_hint_plan
SELECT /*+ 
    HashJoin(e d) 
    SeqScan(e) 
    IndexScan(d dept_location_idx) 
    NestLoop(d l)
*/ 
    e.employee_id,
    e.employee_name,
    d.department_name,
    l.location_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE e.hire_date >= CURRENT_DATE - INTERVAL '1 year'
  AND l.country_id = 'US'
ORDER BY e.salary DESC;
