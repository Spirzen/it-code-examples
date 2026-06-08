BEGIN;

UPDATE employees
SET salary = salary * 1.05
WHERE department_id = 10;

-- контроль перед фиксацией
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
WHERE department_id = 10
GROUP BY department_id;

COMMIT;
-- ROLLBACK;  -- при неверном результате
